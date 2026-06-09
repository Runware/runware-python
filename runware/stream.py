"""
LLM text streaming over SSE.

`TextStream` exposes two async iterators (`text_stream`, `reasoning_stream`)
and a final `result()` coroutine. The underlying HTTP request is shared — the
iterators consume from the same internal queue, fan-out happens in
`_chunk_pump`.
"""

from __future__ import annotations

import asyncio
import contextlib
import json
import uuid
from collections.abc import AsyncIterator, Callable
from typing import cast

import aiohttp

from .errors import create_runware_error, parse_api_error
from .types.sdk import LoosePayload, SDKConfig
from .types.stream import TextStreamChunk, TextStreamResult

_TERMINATE_SENTINEL = object()


def parse_sse_line(line: str) -> TextStreamChunk | None:
    """Parse a single SSE `data: ...` line into a chunk.

    Returns None for blank lines, comments (`:`-prefixed), and the `[DONE]`
    terminator. Raises RunwareError if the server sent an error frame.
    """
    trimmed = line.strip()
    if not trimmed or trimmed.startswith(":"):
        return None
    if not trimmed.startswith("data:"):
        return None
    payload = trimmed[5:].strip()
    if payload == "[DONE]":
        return None
    try:
        data: object = cast(object, json.loads(payload))
    except json.JSONDecodeError as exc:
        raise create_runware_error(
            "parseError", f"Failed to parse SSE data: {payload[:200]}"
        ) from exc

    if not isinstance(data, dict):
        return None
    obj = cast(LoosePayload, data)

    if isinstance(obj.get("errors"), list) or isinstance(obj.get("error"), dict):
        raise parse_api_error(obj)

    raw_delta = obj.get("delta")
    delta_dict: LoosePayload = (
        cast(LoosePayload, raw_delta) if isinstance(raw_delta, dict) else {}
    )

    return TextStreamChunk(
        text=delta_dict.get("text") if isinstance(delta_dict.get("text"), str) else None,
        reasoning_content=(
            delta_dict.get("reasoningContent")
            if isinstance(delta_dict.get("reasoningContent"), str)
            else None
        ),
        finish_reason=(
            obj.get("finishReason") if isinstance(obj.get("finishReason"), str) else None
        ),
        usage=cast(LoosePayload, obj.get("usage")) if isinstance(obj.get("usage"), dict) else None,
        cost=(
            float(cast(float, obj["cost"]))
            if isinstance(obj.get("cost"), (int, float))
            else None
        ),
        result_index=(
            int(cast(int, obj["resultIndex"]))
            if isinstance(obj.get("resultIndex"), int)
            else None
        ),
        task_uuid=obj.get("taskUUID") if isinstance(obj.get("taskUUID"), str) else None,
    )


class TextStream:
    """
    LLM stream result.

    Exposes:
      - `text_stream` — async iterator of incremental text deltas
      - `reasoning_stream` — async iterator of incremental reasoning deltas
      - `result()` — final accumulated state once the stream completes

    The HTTP request runs in a background pump task started by the constructor.
    Iterators block until new chunks arrive. `result()` waits until the pump
    finishes.
    """

    def __init__(
        self,
        *,
        config: SDKConfig,
        session: aiohttp.ClientSession,
        task: LoosePayload,
        cancel_event: asyncio.Event | None = None,
        timeout_seconds: float | None = None,
    ) -> None:
        self._text_queue: asyncio.Queue[object] = asyncio.Queue()
        self._reasoning_queue: asyncio.Queue[object] = asyncio.Queue()
        self._chunks: list[TextStreamChunk] = []
        self._final: TextStreamResult | None = None
        self._error: BaseException | None = None
        self._done: asyncio.Event = asyncio.Event()
        # Owner-side shutdown signal. The client sets this from `close()` so
        # in-flight streams abort cleanly instead of surfacing an opaque
        # ClientConnectorError when the session is yanked from underneath.
        self._shutdown_event: asyncio.Event = asyncio.Event()
        self._on_finish: Callable[[], None] | None = None
        # Pump is started lazily on first consumption (iter / text() / result())
        # to match TS behavior: a stream that's created but never read costs
        # nothing. Spinning the HTTP request eagerly would charge credits and
        # run the model even if the user never iterates.
        self._pump_task: asyncio.Task[None] | None = None
        self._pump_config: SDKConfig = config
        self._pump_session: aiohttp.ClientSession = session
        self._pump_task_payload: LoosePayload = task
        self._pump_cancel_event: asyncio.Event | None = cancel_event
        self._pump_timeout_seconds: float | None = timeout_seconds

    def _ensure_pump_started(self) -> None:
        if self._pump_task is None:
            self._pump_task = asyncio.create_task(self._pump(
                config=self._pump_config,
                session=self._pump_session,
                task=self._pump_task_payload,
                cancel_event=self._pump_cancel_event,
                timeout_seconds=self._pump_timeout_seconds,
            ))

    def _signal_shutdown(self) -> None:
        """Owner-side signal that the parent client is closing."""
        self._shutdown_event.set()

    def _set_on_finish(self, callback: Callable[[], None]) -> None:
        """Register a one-shot callback fired after `_finish()` runs."""
        self._on_finish = callback

    @property
    def text_stream(self) -> AsyncIterator[str]:
        self._ensure_pump_started()
        return _queue_iter(self._text_queue)

    @property
    def reasoning_stream(self) -> AsyncIterator[str]:
        self._ensure_pump_started()
        return _queue_iter(self._reasoning_queue)

    async def result(self) -> TextStreamResult:
        self._ensure_pump_started()
        await self._done.wait()
        if self._error is not None:
            raise self._error
        assert self._final is not None
        return self._final

    async def text(self) -> str:
        """Convenience: await the whole stream and return its concatenated text."""
        return (await self.result()).text or ""

    def _ingest(self, chunk: TextStreamChunk) -> None:
        self._chunks.append(chunk)
        if chunk.text:
            self._text_queue.put_nowait(chunk.text)
        if chunk.reasoning_content:
            self._reasoning_queue.put_nowait(chunk.reasoning_content)

    def _finish(self, error: BaseException | None = None) -> None:
        if error is not None:
            self._error = error
        else:
            self._final = _accumulate(self._chunks)
        self._text_queue.put_nowait(_TERMINATE_SENTINEL)
        self._reasoning_queue.put_nowait(_TERMINATE_SENTINEL)
        self._done.set()
        if self._on_finish is not None:
            with contextlib.suppress(Exception):
                self._on_finish()

    async def _pump(
        self,
        *,
        config: SDKConfig,
        session: aiohttp.ClientSession,
        task: LoosePayload,
        cancel_event: asyncio.Event | None,
        timeout_seconds: float | None,
    ) -> None:
        url = config.http_base_url
        request_timeout = (
            aiohttp.ClientTimeout(total=timeout_seconds) if timeout_seconds else None
        )
        try:
            config.log.send(json.dumps([task], default=str))
            async with session.post(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {config.api_key}",
                    "Accept": "text/event-stream",
                },
                json=[task],
                timeout=request_timeout,
            ) as response:
                if not response.ok:
                    body_text = await response.text()
                    body: object | None
                    try:
                        body = cast(object, json.loads(body_text))
                    except json.JSONDecodeError:
                        body = None
                    if body:
                        err = parse_api_error(body, task_type=task.get("taskType"))
                        err.status_code = response.status
                        raise err
                    raise create_runware_error(
                        "httpError",
                        f"HTTP {response.status}: {response.reason or ''}",
                        status_code=response.status,
                    )

                buffer = ""
                # Race each read against BOTH the user cancel and the owner-
                # side shutdown so a blocked socket read (model emits nothing
                # for tens of seconds) interrupts immediately when either
                # signal fires. Without this race, `cancel_event` and
                # `_shutdown_event` are cooperative-only and won't abort a
                # stuck stream until the next chunk arrives or ClientTimeout.
                abort_tasks: list[asyncio.Task[bool]] = []
                if cancel_event is not None:
                    abort_tasks.append(asyncio.create_task(cancel_event.wait()))
                abort_tasks.append(asyncio.create_task(self._shutdown_event.wait()))
                try:
                    iterator = response.content.iter_any().__aiter__()
                    while True:
                        read_task: asyncio.Task[bytes] = asyncio.create_task(
                            iterator.__anext__()
                        )
                        done, _pending = await asyncio.wait(
                            {read_task, *abort_tasks},
                            return_when=asyncio.FIRST_COMPLETED,
                        )
                        if any(t in done for t in abort_tasks):
                            read_task.cancel()
                            raise create_runware_error(
                                "aborted", "Stream aborted",
                            )
                        try:
                            chunk_bytes = read_task.result()
                        except StopAsyncIteration:
                            break

                        buffer += chunk_bytes.decode("utf-8", errors="replace")
                        while "\n" in buffer:
                            line, buffer = buffer.split("\n", 1)
                            chunk = parse_sse_line(line)
                            if chunk is not None:
                                config.log.receive(_dump_chunk(chunk))
                                self._ingest(chunk)
                    if buffer:
                        chunk = parse_sse_line(buffer)
                        if chunk is not None:
                            config.log.receive(_dump_chunk(chunk))
                            self._ingest(chunk)
                finally:
                    for t in abort_tasks:
                        if not t.done():
                            t.cancel()
        except TimeoutError:
            self._finish(
                error=create_runware_error(
                    "timeout",
                    f"Stream timed out after {int((timeout_seconds or 0) * 1000)}ms",
                )
            )
            return
        except Exception as exc:
            self._finish(error=exc)
            return
        except BaseException:
            self._finish(
                error=create_runware_error("aborted", "Stream aborted"),
            )
            raise
        self._finish()


async def _queue_iter(queue: asyncio.Queue[object]) -> AsyncIterator[str]:
    while True:
        item = await queue.get()
        if item is _TERMINATE_SENTINEL:
            return
        yield cast(str, item)


def _accumulate(chunks: list[TextStreamChunk]) -> TextStreamResult:
    result = TextStreamResult(raw_chunks=list(chunks))
    text_parts: list[str] = []
    reasoning_parts: list[str] = []
    for c in chunks:
        if c.text:
            text_parts.append(c.text)
        if c.reasoning_content:
            reasoning_parts.append(c.reasoning_content)
        if c.finish_reason and result.finish_reason is None:
            result.finish_reason = c.finish_reason
        if c.usage is not None:
            result.usage = c.usage
        if c.cost is not None:
            result.cost = c.cost
        if c.task_uuid and result.task_uuid is None:
            result.task_uuid = c.task_uuid
    result.text = "".join(text_parts)
    result.reasoning_content = "".join(reasoning_parts)
    return result


def _dump_chunk(chunk: TextStreamChunk) -> str:
    payload: LoosePayload = {}
    if chunk.text:
        payload["text"] = chunk.text
    if chunk.reasoning_content:
        payload["reasoningContent"] = chunk.reasoning_content
    if chunk.finish_reason:
        payload["finishReason"] = chunk.finish_reason
    if chunk.usage is not None:
        payload["usage"] = chunk.usage
    if chunk.cost is not None:
        payload["cost"] = chunk.cost
    return json.dumps(payload, default=str)


async def create_text_stream(
    *,
    config: SDKConfig,
    session: aiohttp.ClientSession,
    params: LoosePayload,
    cancel_event: asyncio.Event | None = None,
    timeout_seconds: float | None = None,
) -> TextStream:
    """
    Open a streaming POST to the configured base URL and return a TextStream.

    The background pump task runs until the SSE stream ends or an error fires.
    Cancel via the supplied `cancel_event`. `timeout_seconds` caps the whole
    streaming HTTP call end-to-end (matches TS's `StreamOptions.timeout`).
    """
    if isinstance(params.get("numberResults"), int) and params["numberResults"] > 1:
        raise create_runware_error(
            "notImplemented",
            (
                "stream() with numberResults > 1 is not supported "
                "(the backend doesn't emit resultIndex on stream chunks)."
            ),
        )

    # User-supplied passthrough: values are Any by per-taskType design.
    task_payload: LoosePayload = {
        k: v
        for k, v in params.items()  # pyright: ignore[reportAny]
        if k not in ("taskUUID",)
    }
    task_payload.setdefault("taskUUID", str(uuid.uuid4()))

    return TextStream(
        config=config,
        session=session,
        task=task_payload,
        cancel_event=cancel_event,
        timeout_seconds=timeout_seconds,
    )
