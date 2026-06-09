"""
REST transport over aiohttp.

One POST per request. Async-task results come back via the same POST when
`deliveryMethod='sync'`; with the default `deliveryMethod='async'` the server
returns an ACK and the client polls `getResponse` until results arrive
(polling lives in `client.py`, not here).
"""

from __future__ import annotations

import asyncio
import json
from typing import Self, cast

import aiohttp

from ..errors import create_runware_error, is_runware_error, parse_api_error
from ..types.sdk import LoosePayload, SDKConfig
from ..types.transport import RequestOptions, WireFrame
from ..utils.retry import with_retry

_RETRYABLE_STATUS = {408, 429}


def _is_retryable_status(status: int) -> bool:
    return status in _RETRYABLE_STATUS or 500 <= status < 600


class RestTransport:
    """
    REST transport.

    Owns an aiohttp.ClientSession across calls. Use as an async context
    manager (`async with`) for explicit lifecycle, or call `close()` manually.
    """

    def __init__(self, config: SDKConfig) -> None:
        self._config: SDKConfig = config
        injected = config.dependencies.session if config.dependencies else None
        self._session: aiohttp.ClientSession | None = injected
        self._owned_session: bool = injected is None

    async def __aenter__(self) -> Self:
        await self._ensure_session()
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.close()

    async def close(self) -> None:
        if self._owned_session and self._session is not None:
            await self._session.close()
            self._session = None

    async def _ensure_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
            self._owned_session = True
        return self._session

    async def send_request(
        self,
        data: LoosePayload | list[LoosePayload],
        options: RequestOptions | None = None,
    ) -> WireFrame:
        """
        POST a task or batch of tasks. Returns the parsed JSON response.

        The response shape depends on delivery semantics:
          - deliveryMethod='sync'  : the full result is in the response.
          - deliveryMethod='async' : the response is an ACK; client.py polls.
        """
        payload = data if isinstance(data, list) else [data]
        url = self._config.http_base_url
        per_request_timeout = (options.timeout if options else None) or self._config.timeout
        cancel_event = options.cancel_event if options else None

        try:
            return await with_retry(
                lambda: self._do_post(url, payload, per_request_timeout, cancel_event),
                max_retries=self._config.max_retries,
                retry_delay_ms=self._config.retry_delay,
                retry_strategy=self._config.retry_strategy,
                cancel_event=cancel_event,
                should_retry=self._should_retry,
                on_retry=self._log_retry,
            )
        except TimeoutError as exc:
            raise create_runware_error(
                "timeout",
                (
                    f"REST request timed out after {per_request_timeout}ms "
                    f"(gave up after {self._config.max_retries + 1} attempts)"
                ),
            ) from exc

    async def _do_post(
        self,
        url: str,
        payload: list[LoosePayload],
        timeout_ms: int,
        cancel_event: asyncio.Event | None,
    ) -> WireFrame:
        session = await self._ensure_session()
        timeout = aiohttp.ClientTimeout(total=timeout_ms / 1000.0)

        async def do_request() -> WireFrame:
            self._config.log.send(json.dumps(payload, default=str))
            async with session.post(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self._config.api_key}",
                },
                json=payload,
                timeout=timeout,
            ) as response:
                if not response.ok:
                    body_text = await response.text()
                    body: object | None
                    try:
                        body = cast(object, json.loads(body_text))
                    except json.JSONDecodeError:
                        body = None

                    context_task_type: str | None = None
                    context_model: str | None = None
                    first_task = payload[0] if payload else None
                    if first_task:
                        context_task_type = first_task.get("taskType")
                        context_model = first_task.get("model")

                    if body:
                        err = parse_api_error(
                            body,
                            task_type=context_task_type,
                            model=context_model,
                        )
                        err.status_code = response.status
                        raise err

                    if response.status == 401:
                        raise create_runware_error(
                            "invalidApiKey",
                            (
                                f"Authentication failed: invalid API key "
                                f"(HTTP 401 {response.reason or ''})"
                            ),
                            status_code=401,
                        )

                    raise create_runware_error(
                        "httpError",
                        f"HTTP {response.status}: {response.reason or ''}",
                        status_code=response.status,
                    )

                try:
                    # aiohttp.json() is untyped (returns Any). Narrow at the
                    # boundary; downstream code reads data/errors against the
                    # WireFrame shape.
                    body_json = cast(WireFrame, await response.json())
                except (
                    aiohttp.ContentTypeError,
                    json.JSONDecodeError,
                    ValueError,
                ) as exc:
                    raise create_runware_error(
                        "parseError",
                        (
                            f"Server returned HTTP {response.status} with a "
                            f"non-JSON body ({type(exc).__name__})"
                        ),
                        status_code=response.status,
                    ) from exc
                self._config.log.receive(json.dumps(body_json, default=str))
                return body_json

        if cancel_event is None:
            return await do_request()

        request_task = asyncio.create_task(do_request())
        cancel_task = asyncio.create_task(cancel_event.wait())
        try:
            done, _pending = await asyncio.wait(
                {request_task, cancel_task}, return_when=asyncio.FIRST_COMPLETED
            )
            if cancel_task in done:
                request_task.cancel()
                raise create_runware_error("aborted", "Request aborted")
            cancel_task.cancel()
            return request_task.result()
        except asyncio.CancelledError:
            request_task.cancel()
            cancel_task.cancel()
            raise

    @staticmethod
    def _should_retry(error: BaseException) -> bool:
        if is_runware_error(error) and error.code == "aborted":
            return False
        if isinstance(error, TimeoutError):
            return True
        if (
            is_runware_error(error)
            and error.status_code is not None
            and _is_retryable_status(error.status_code)
        ):
            return True
        # Connection-level failures (TCP reset, DNS, etc.) AND payload-level
        # failures (mid-body truncation, chunked-encoding errors). Both are
        # transient and benefit from a retry.
        return isinstance(
            error, (aiohttp.ClientConnectionError, aiohttp.ClientPayloadError),
        )

    def _log_retry(self, error: BaseException, attempt: int, delay_ms: int) -> None:
        reason = "unknown"
        if isinstance(error, TimeoutError):
            reason = "timeout"
        elif is_runware_error(error) and error.status_code is not None:
            reason = f"HTTP {error.status_code}"
        elif isinstance(error, aiohttp.ClientConnectionError):
            reason = "connection error"
        max_retries = self._config.max_retries
        self._config.log.retry(
            f"Retrying after {reason}, attempt {attempt}/{max_retries} in {delay_ms}ms",
        )
