"""
Calling a serverless app.

``invoke`` submits a payload to one endpoint of one app and returns the
finished task. ``get_task`` reads a task by id, for callers that would rather
poll themselves.

Both routes are on the serverless API, a different origin from the inference
API, so this module does its own HTTP rather than going through a transport.
It shares the client's aiohttp session, its retry settings and its error type.
"""

from __future__ import annotations

import asyncio
import json
import re
import time
import uuid
from collections.abc import Awaitable, Callable
from typing import Any, cast

import aiohttp

from .errors import RunwareError, create_runware_error, is_runware_error
from .types.sdk import SDKConfig
from .types.serverless import (
    GetTaskOptions,
    InvokeOptions,
    ServerlessTask,
)
from .user_agent import user_agent
from .utils.retry import calculate_retry_delay, interruptible_sleep

SessionProvider = Callable[[], Awaitable[aiohttp.ClientSession]]

_APP_ID_PATTERN = re.compile(r"^[a-z][a-z0-9-]{4,28}[a-z0-9]$")
_ENDPOINT_PATH_PATTERN = re.compile(r"^[a-z]([a-z0-9-]{0,62}[a-z0-9])?$")
_TASK_ID_PATTERN = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
)

_DEFAULT_POLL_INTERVAL_S = 2.0

# A task id the platform has just accepted can miss the result store for a
# moment, so get_task answers 404 before it answers the task. Polling treats a
# 404 as transient for this long and only then gives up.
_TASK_NOT_FOUND_GRACE_S = 30.0

# Floor for a sync invocation's per-request timeout. It has to outlast the
# platform's own wait window, otherwise the client gives up on a request the
# platform was about to answer, and the answer it was about to give is the
# accepted task the SDK needs in order to poll.
_SYNC_MIN_TIMEOUT_MS = 300_000

_TERMINAL = frozenset({"completed", "failed"})


def is_terminal(status: str) -> bool:
    """Whether a task status is final."""
    return status in _TERMINAL


def _raw_code_for_status(status: int) -> str:
    return {
        400: "validationFailed",
        401: "unauthorized",
        402: "paymentRequired",
        403: "forbidden",
        404: "resourceNotFound",
        409: "conflictingState",
        413: "maxRequestSize",
        422: "validationFailed",
        429: "rateLimitExceeded",
        503: "serviceUnavailable",
    }.get(status, "internalServerError")


def _is_retryable_status(status: int) -> bool:
    return status in (408, 429) or 500 <= status < 600


def validate_app_id(app_id: object) -> str:
    """Check an app id against the platform's own pattern."""
    if not isinstance(app_id, str) or not app_id:
        raise create_runware_error(
            "missingParameter", "app_id is required", parameter="app_id",
        )
    if not _APP_ID_PATTERN.match(app_id):
        raise create_runware_error(
            "invalidParameter",
            f'app_id "{app_id}" is invalid: use 6 to 30 lowercase characters, '
            + "starting with a letter and ending with a letter or digit",
            parameter="app_id",
        )
    return app_id


def validate_endpoint_path(endpoint_path: object) -> str:
    """Check an endpoint path against ADR-034: a bare lowercase segment."""
    if not isinstance(endpoint_path, str) or not endpoint_path:
        raise create_runware_error(
            "missingParameter", "endpoint_path is required", parameter="endpoint_path",
        )
    if endpoint_path.startswith("/"):
        bare = endpoint_path.lstrip("/")
        hint = f' (e.g. "{bare}")' if _ENDPOINT_PATH_PATTERN.match(bare) else ""
        raise create_runware_error(
            "invalidParameter",
            f'endpoint_path "{endpoint_path}" must be a bare segment without a '
            + f"leading slash{hint}",
            parameter="endpoint_path",
        )
    if not _ENDPOINT_PATH_PATTERN.match(endpoint_path):
        raise create_runware_error(
            "invalidParameter",
            f'endpoint_path "{endpoint_path}" is invalid: use a lowercase segment '
            + "of 1 to 64 characters (letters, digits, hyphens)",
            parameter="endpoint_path",
        )
    return endpoint_path


def validate_task_id(task_id: object) -> str:
    """Check a task id is a canonical lowercase UUID."""
    if not isinstance(task_id, str) or not _TASK_ID_PATTERN.match(task_id):
        raise create_runware_error(
            "invalidParameter",
            f'task_id "{task_id}" is invalid: use a lowercase UUID',
            parameter="task_id",
        )
    return task_id


def _resolve_task_id(task_id: object) -> str:
    if task_id is None:
        return str(uuid.uuid4())
    return validate_task_id(task_id)


def _parse_retry_after(value: str | None) -> float | None:
    if not value:
        return None
    try:
        seconds = float(value)
    except ValueError:
        return None
    return seconds if seconds >= 0 else None


def _problem_to_error(
    body: object, status: int, retry_after: float | None,
) -> RunwareError:
    """
    Turn an RFC 9457 problem document into a RunwareError.

    Field-level entries from a 422 are appended to the message, because a
    validation failure the caller cannot see the fields of is not actionable.
    """
    problem: dict[str, object] = (
        cast("dict[str, object]", body) if isinstance(body, dict) else {}
    )

    detail = problem.get("detail")
    title = problem.get("title")
    message = (
        detail if isinstance(detail, str) and detail
        else title if isinstance(title, str) and title
        else f"HTTP {status}"
    )

    raw_errors = problem.get("errors")
    lines: list[str] = []
    if isinstance(raw_errors, list):
        for entry in cast("list[object]", raw_errors):
            if not isinstance(entry, dict):
                continue
            item = cast("dict[str, object]", entry)
            text = item.get("detail")
            if not isinstance(text, str) or not text:
                continue
            pointer = item.get("pointer")
            lines.append(
                f"  {pointer}: {text}" if isinstance(pointer, str) and pointer
                else f"  {text}",
            )
    if lines:
        message = message + "\n" + "\n".join(lines)

    error = create_runware_error(
        _raw_code_for_status(status), message, status_code=status,
    )
    problem_type = problem.get("type")
    if isinstance(problem_type, str) and problem_type != "about:blank":
        error.problem_type = problem_type
    request_id = problem.get("requestId")
    if isinstance(request_id, str):
        error.request_id = request_id
    if isinstance(problem.get("endpointPath"), str):
        error.parameter = "endpoint_path"
    if retry_after is not None:
        error.retry_after = retry_after
    return error


def _to_task(body: object, context: str) -> ServerlessTask:
    ok = False
    if isinstance(body, dict):
        mapping = cast("dict[str, object]", body)
        ok = isinstance(mapping.get("id"), str) and isinstance(
            mapping.get("status"), str,
        )
    if not ok:
        raise create_runware_error(
            "parseError", f"{context}: the response carried no task",
        )
    return cast("ServerlessTask", body)


class ServerlessApi:
    """Invoke serverless app endpoints and read their tasks."""

    def __init__(
        self, session_provider: SessionProvider, config: SDKConfig,
    ) -> None:
        self._session_provider: SessionProvider = session_provider
        self._config: SDKConfig = config

    @property
    def _origin(self) -> str:
        return self._config.serverless_base_url.rstrip("/")

    async def invoke(
        self,
        app_id: str,
        endpoint_path: str,
        payload: dict[str, Any] | None = None,  # pyright: ignore[reportExplicitAny]
        *,
        task_id: str | None = None,
        options: InvokeOptions | None = None,
    ) -> ServerlessTask:
        """
        Call an endpoint on one of your serverless apps and return the
        finished task.

            task = await client.invoke(
                "my-app", "generate", {"prompt": "a cat"},
            )
            print(task["output"])

        ``delivery_method`` decides how the wait happens, not whether you get
        a result: ``async`` (the default) takes an acknowledgement and polls,
        ``sync`` holds one request open and is the fast path for work that
        finishes in seconds. ``wait=False`` returns the accepted task instead,
        for a job you mean to pick up later with ``get_task``.

        Every invocation carries a task id, generated unless you pass one.
        Sending the same id again returns the task it already names instead of
        starting a second, so a call whose response was lost is safe to repeat.

        Raises a ``RunwareError`` when the task fails to start. A task that
        runs and fails comes back with ``status`` ``failed`` and its ``error``
        set, because that is an outcome rather than a broken call.
        """
        options = options or InvokeOptions()
        app = validate_app_id(app_id)
        endpoint = validate_endpoint_path(endpoint_path)
        resolved_task_id = _resolve_task_id(task_id)
        delivery_method = options.delivery_method if options.wait else "async"
        route = "invoke-sync" if delivery_method == "sync" else "invoke-async"

        configured = options.timeout or self._config.timeout
        timeout_ms = (
            max(configured, _SYNC_MIN_TIMEOUT_MS)
            if delivery_method == "sync"
            else configured
        )

        body: dict[str, object] = {
            "taskId": resolved_task_id,
            "payload": payload if payload is not None else {},
        }
        self._config.log.send(json.dumps(body, default=str))

        started_at = time.monotonic()
        _status, response_body = await self._request(
            "POST",
            f"{self._origin}/v1/apps/{app}/{route}/{endpoint}",
            body,
            timeout_ms,
            options.cancel_event,
        )

        task = _to_task(response_body, f"invoke {endpoint}")

        if not options.wait or is_terminal(task["status"]):
            return task

        return await self._wait_for_task(task, options, started_at)

    async def get_task(
        self,
        app_id: str,
        task_id: str,
        options: GetTaskOptions | None = None,
    ) -> ServerlessTask:
        """
        Read one serverless task by id.

        ``invoke`` already waits for you, so reach for this when you want to
        poll yourself: after ``invoke`` with ``wait=False``, or from a
        different process than the one that submitted the task.
        """
        options = options or GetTaskOptions()
        app = validate_app_id(app_id)
        resolved = validate_task_id(task_id)
        _status, body = await self._request(
            "GET",
            f"{self._origin}/v1/apps/{app}/tasks/{resolved}",
            None,
            options.timeout or self._config.timeout,
            options.cancel_event,
        )
        return _to_task(body, "get_task")

    async def _wait_for_task(
        self,
        task: ServerlessTask,
        options: InvokeOptions,
        started_at: float,
    ) -> ServerlessTask:
        """
        Poll until the task reaches a terminal state. Never resubmits: the task
        is already running, and a second invocation would be a second charge.
        """
        interval = (
            options.poll_interval
            if options.poll_interval is not None
            else _DEFAULT_POLL_INTERVAL_S
        )
        budget_s = (options.poll_timeout or self._config.poll_timeout) / 1000.0
        not_found_since: float | None = None
        current = task

        while not is_terminal(current["status"]):
            if time.monotonic() - started_at > budget_s:
                raise create_runware_error(
                    "timeout",
                    f'Task {current["id"]} is still running after '
                    + f"{options.poll_timeout or self._config.poll_timeout}ms. "
                    + "It was not cancelled: poll "
                    + f'get_task("{current["appId"]}", "{current["id"]}") '
                    + "to pick it up.",
                    task_uuid=current["id"],
                )

            await interruptible_sleep(interval, options.cancel_event)

            try:
                current = await self.get_task(
                    current["appId"],
                    current["id"],
                    GetTaskOptions(
                        timeout=options.timeout,
                        cancel_event=options.cancel_event,
                    ),
                )
                not_found_since = None
            except RunwareError as error:
                if error.status_code != 404:
                    raise
                if not_found_since is None:
                    not_found_since = time.monotonic()
                if time.monotonic() - not_found_since > _TASK_NOT_FOUND_GRACE_S:
                    raise

        return current

    async def _request(
        self,
        method: str,
        url: str,
        body: dict[str, object] | None,
        timeout_ms: int,
        cancel_event: asyncio.Event | None,
    ) -> tuple[int, object]:
        """
        Retry transport failures and retryable statuses. Safe on an invocation
        because every one carries a task id: a retry the platform already saw
        is answered with the task it started rather than a second one.

        A response carrying ``Retry-After`` waits exactly that long. A capacity
        refusal names a wait the platform expects to need, and backing off for
        less than it just spends an attempt to be told the same thing.
        """
        last_error: BaseException | None = None

        for attempt in range(self._config.max_retries + 1):
            try:
                return await self._fetch_once(
                    method, url, body, timeout_ms, cancel_event,
                )
            except BaseException as error:
                last_error = error

                if not self._should_retry(error) or attempt == self._config.max_retries:
                    break

                retry_after = (
                    error.retry_after if is_runware_error(error) else None
                )
                delay_ms = (
                    retry_after * 1000
                    if retry_after is not None
                    else calculate_retry_delay(
                        attempt, self._config.retry_delay, self._config.retry_strategy,
                    )
                )
                self._config.log.retry(
                    f"Retrying serverless request, attempt {attempt + 1}/"
                    + f"{self._config.max_retries} in {round(delay_ms)}ms",
                )
                await interruptible_sleep(delay_ms / 1000.0, cancel_event)

        assert last_error is not None
        raise last_error

    @staticmethod
    def _should_retry(error: BaseException) -> bool:
        if is_runware_error(error):
            if error.code == "aborted":
                return False
            if error.code == "timeout":
                return True
            if error.status_code is not None:
                return _is_retryable_status(error.status_code)
            return False
        return isinstance(
            error, (aiohttp.ClientConnectionError, aiohttp.ClientPayloadError),
        )

    async def _fetch_once(
        self,
        method: str,
        url: str,
        body: dict[str, object] | None,
        timeout_ms: int,
        cancel_event: asyncio.Event | None,
    ) -> tuple[int, object]:
        session = await self._session_provider()
        timeout = aiohttp.ClientTimeout(total=timeout_ms / 1000.0)

        async def do_request() -> tuple[int, object]:
            try:
                async with session.request(
                    method,
                    url,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {self._config.api_key}",
                        "User-Agent": user_agent(self._config.user_agent_prefix),
                    },
                    json=body,
                    timeout=timeout,
                ) as response:
                    text = await response.text()
                    parsed: object | None
                    try:
                        parsed = cast(object, json.loads(text))
                    except json.JSONDecodeError:
                        parsed = None

                    if not response.ok:
                        raise _problem_to_error(
                            parsed,
                            response.status,
                            _parse_retry_after(response.headers.get("Retry-After")),
                        )

                    self._config.log.receive(text)
                    return response.status, parsed
            except TimeoutError as exc:
                raise create_runware_error(
                    "timeout",
                    f"Serverless request timed out after {timeout_ms}ms",
                ) from exc

        if cancel_event is None:
            return await do_request()

        request_task = asyncio.create_task(do_request())
        cancel_task = asyncio.create_task(cancel_event.wait())
        try:
            done, _pending = await asyncio.wait(
                {request_task, cancel_task}, return_when=asyncio.FIRST_COMPLETED,
            )
            if cancel_task in done:
                _ = request_task.cancel()
                raise create_runware_error("aborted", "Request aborted")
            _ = cancel_task.cancel()
            return request_task.result()
        except asyncio.CancelledError:
            _ = request_task.cancel()
            _ = cancel_task.cancel()
            raise
