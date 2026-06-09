"""
Tests for ``TextStream`` — text/reasoning fanout, result accumulation, errors,
and the public guarantees of the iterators returned by ``client.stream()``.

The HTTP pump itself is exercised in the integration tests against a real
server. Here we drive the stream's ingestion paths directly via internal
helpers and assert the public contract.
"""

from __future__ import annotations

import asyncio

import pytest

from runware import Runware, RunwareError
from runware.stream import TextStream
from runware.types.stream import TextStreamChunk


def _bare_stream() -> TextStream:
    """Construct a TextStream without firing the HTTP pump task."""
    s = TextStream.__new__(TextStream)
    s._text_queue = asyncio.Queue()
    s._reasoning_queue = asyncio.Queue()
    s._chunks = []
    s._final = None
    s._error = None
    s._done = asyncio.Event()
    s._shutdown_event = asyncio.Event()
    s._on_finish = None
    # Pretend the pump has already started so the lazy-start guard is a no-op.
    s._pump_task = asyncio.create_task(asyncio.sleep(0))
    return s


class TestIngestionAndAccumulation:
    @pytest.mark.asyncio
    async def test_text_iterator_yields_deltas(self) -> None:
        s = _bare_stream()
        s._ingest(TextStreamChunk(text="hello "))
        s._ingest(TextStreamChunk(text="world"))
        s._finish()

        received: list[str] = []
        async for chunk in s.text_stream:
            received.append(chunk)
        assert received == ["hello ", "world"]

    @pytest.mark.asyncio
    async def test_reasoning_iterator_yields_only_reasoning(self) -> None:
        s = _bare_stream()
        s._ingest(TextStreamChunk(text="visible "))
        s._ingest(TextStreamChunk(reasoning_content="hidden "))
        s._ingest(TextStreamChunk(text="more visible"))
        s._ingest(TextStreamChunk(reasoning_content="more hidden"))
        s._finish()

        text: list[str] = []
        reasoning: list[str] = []
        async for t in s.text_stream:
            text.append(t)
        async for r in s.reasoning_stream:
            reasoning.append(r)

        assert text == ["visible ", "more visible"]
        assert reasoning == ["hidden ", "more hidden"]

    @pytest.mark.asyncio
    async def test_result_accumulates_text_and_metadata(self) -> None:
        s = _bare_stream()
        s._ingest(TextStreamChunk(text="The "))
        s._ingest(
            TextStreamChunk(
                text="answer ",
                reasoning_content="thinking ",
                usage={"promptTokens": 5, "completionTokens": 10},
            )
        )
        s._ingest(
            TextStreamChunk(
                text="is 42.",
                reasoning_content="done",
                finish_reason="stop",
                cost=0.0042,
                task_uuid="u-final",
            )
        )
        s._finish()

        result = await s.result()
        assert result.text == "The answer is 42."
        assert result.reasoning_content == "thinking done"
        assert result.finish_reason == "stop"
        assert result.cost == pytest.approx(0.0042)
        assert result.task_uuid == "u-final"
        assert result.usage == {"promptTokens": 5, "completionTokens": 10}

    @pytest.mark.asyncio
    async def test_text_convenience_returns_full_text(self) -> None:
        s = _bare_stream()
        s._ingest(TextStreamChunk(text="part1 "))
        s._ingest(TextStreamChunk(text="part2"))
        s._finish()
        assert await s.text() == "part1 part2"

    @pytest.mark.asyncio
    async def test_first_finish_reason_wins(self) -> None:
        s = _bare_stream()
        s._ingest(TextStreamChunk(text="x", finish_reason="stop"))
        # A second finishReason later shouldn't overwrite the first.
        s._ingest(TextStreamChunk(text="y", finish_reason="length"))
        s._finish()
        result = await s.result()
        assert result.finish_reason == "stop"


class TestErrorPropagation:
    @pytest.mark.asyncio
    async def test_result_raises_pump_error(self) -> None:
        s = _bare_stream()
        s._finish(error=RunwareError("inferenceError", "provider crashed"))
        with pytest.raises(RunwareError) as exc_info:
            await s.result()
        assert exc_info.value.code == "provider"

    @pytest.mark.asyncio
    async def test_text_iterator_still_drains_then_ends_on_error(self) -> None:
        s = _bare_stream()
        s._ingest(TextStreamChunk(text="partial"))
        s._finish(error=RunwareError("inferenceError", "boom"))

        received: list[str] = []
        async for chunk in s.text_stream:
            received.append(chunk)
        # Matches TS: the iterator drains, then ends. The error surfaces via result().
        assert received == ["partial"]
        with pytest.raises(RunwareError):
            await s.result()


class TestStreamCancellation:
    """A cancel_event must interrupt a blocked socket read promptly — not wait
    for the next chunk to arrive or for the HTTP timeout to fire."""

    @pytest.mark.asyncio
    async def test_cancel_during_blocked_read_aborts_promptly(self) -> None:
        """
        Build a TextStream whose pump is sitting on a never-arriving chunk.
        Setting cancel_event should make the pump raise within a small window.
        """
        from runware.stream import TextStream
        from runware.types.sdk import SDKConfig

        cancel = asyncio.Event()

        # Fake response.content.iter_any() that yields one initial chunk then
        # blocks forever on the next read. Simulates a stalled model stream.
        class _FakeContentIter:
            def __init__(self) -> None:
                self._yielded = False

            def __aiter__(self) -> _FakeContentIter:
                return self

            async def __anext__(self) -> bytes:
                if not self._yielded:
                    self._yielded = True
                    return b""
                await asyncio.sleep(60)
                return b""

        class _FakeContent:
            def iter_any(self) -> _FakeContentIter:
                return _FakeContentIter()


        class _FakeResp:
            ok = True
            status = 200
            content = _FakeContent()

            async def __aenter__(self) -> _FakeResp:
                return self

            async def __aexit__(self, *args: object) -> None:
                pass

        class _FakeSession:
            def post(self, *args: object, **kwargs: object) -> _FakeResp:
                return _FakeResp()

        config = SDKConfig(api_key="sk-test", transport_type="rest")
        from typing import cast

        import aiohttp
        stream = TextStream(
            config=config,
            session=cast(aiohttp.ClientSession, cast(object, _FakeSession())),
            task={"taskUUID": "u", "taskType": "textInference"},
            cancel_event=cancel,
        )

        # Give the pump a moment to start and hit the blocking read.
        await asyncio.sleep(0.1)

        # Fire the cancel. The pump should abort within a small window —
        # NOT wait for the next chunk (which would never arrive).
        cancel.set()

        # If the bug was present, this would hang for 60s. With the fix it
        # raises within tens of ms.
        with pytest.raises(RunwareError) as exc_info:
            await asyncio.wait_for(stream.result(), timeout=2.0)
        assert exc_info.value.code == "aborted"


class TestLazyPump:
    """A TextStream that's created but never consumed must not start the HTTP
    pump — same behavior as the TS SDK. Spinning the pump eagerly would charge
    credits and run the model even when the user never iterates."""

    @pytest.mark.asyncio
    async def test_pump_does_not_start_until_first_consumption(self) -> None:
        from typing import cast as _cast

        import aiohttp

        from runware.stream import TextStream
        from runware.types.sdk import SDKConfig

        post_called = [False]

        class _FakeSession:
            def post(self, *args: object, **kwargs: object) -> object:
                post_called[0] = True
                raise AssertionError("HTTP call fired without consumption")

        config = SDKConfig(api_key="sk-test", transport_type="rest")
        stream = TextStream(
            config=config,
            session=_cast(aiohttp.ClientSession, _cast(object, _FakeSession())),
            task={"taskUUID": "u", "taskType": "textInference"},
        )

        # Give any scheduled task a chance to run.
        await asyncio.sleep(0.05)
        assert post_called[0] is False
        assert stream._pump_task is None


class TestCloseShutdownSignal:
    """Runware.close() must signal in-flight streams to abort cleanly instead
    of letting them surface opaque ClientConnectorErrors when the underlying
    session is yanked from underneath."""

    @pytest.mark.asyncio
    async def test_client_close_sets_stream_shutdown(self) -> None:
        from runware import Runware

        client = Runware(api_key="sk-test", transport_type="rest")
        s = _bare_stream()
        client._active_streams.add(s)
        assert not s._shutdown_event.is_set()
        await client.close()
        assert s._shutdown_event.is_set()

    @pytest.mark.asyncio
    async def test_finish_callback_removes_from_active_streams(self) -> None:
        """When a stream finishes naturally, it deregisters itself from
        the parent's `_active_streams` so the set doesn't leak."""
        from runware import Runware

        client = Runware(api_key="sk-test", transport_type="rest")
        s = _bare_stream()
        client._active_streams.add(s)
        # Mirror what client.stream() does — register the cleanup callback.
        s._set_on_finish(lambda: client._active_streams.discard(s))

        assert s in client._active_streams
        s._finish()
        assert s not in client._active_streams

        await client.close()


class TestNumberResultsGuard:
    @pytest.mark.asyncio
    async def test_stream_rejects_number_results_gt_1(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        try:
            with pytest.raises(RunwareError) as exc_info:
                await client.stream(
                    {
                        "taskType": "textInference",
                        "model": "google:gemma@4-31b",
                        "messages": [{"role": "user", "content": "hi"}],
                        "numberResults": 2,
                    }
                )
            assert "numberResults" in exc_info.value.message
        finally:
            await client.close()

