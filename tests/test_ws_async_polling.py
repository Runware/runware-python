"""
Tests for the two-phase WebSocket async path in ``client.py``.

Phase 1: send the original task, await an ACK frame on the same subscription.
Phase 2: send ``getResponse`` polls over the same socket until each expected
result arrives.

We mock the WebSocketTransport at the client level so we don't need a live
socket. Frames are pushed via the callback that ``subscribe_to_task`` captured.
"""

from __future__ import annotations

import asyncio
from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest

from runware import Runware, RunwareError
from runware.transport.websocket import WebSocketTransport


def _patch_ws(client: Runware) -> tuple[MagicMock, dict[str, Any]]:
    """Replace the client's WS transport with a mock; capture subscription state."""
    mock = MagicMock(spec=WebSocketTransport)
    mock.is_connected = True
    mock.connect = AsyncMock()
    mock.disconnect = AsyncMock()
    mock.send_request = AsyncMock()
    state: dict[str, Any] = {"callbacks": {}, "sent": [], "unsubscribed": []}

    def subscribe(task_uuid: str, cb: Any) -> None:
        state["callbacks"][task_uuid] = cb

    def unsubscribe(task_uuid: str) -> None:
        state["unsubscribed"].append(task_uuid)
        state["callbacks"].pop(task_uuid, None)

    async def send(data: Any) -> None:
        state["sent"].append(data)

    mock.subscribe_to_task = subscribe
    mock.unsubscribe_from_task = unsubscribe
    mock.send_request = send
    client._ws_transport = mock
    return mock, state


def _run_in_background(coro: Any) -> asyncio.Task[Any]:
    return asyncio.create_task(coro)


def _flatten_sent(sent: list[Any]) -> list[dict[str, Any]]:
    """
    Normalize captured frames into a flat list of task dicts.

    ``send_request`` accepts either a single dict or a list of dicts; the
    mock just records whatever was passed. Flatten so tests can scan for
    specific task types uniformly.
    """
    out: list[dict[str, Any]] = []
    for frame in sent:
        if isinstance(frame, list):
            out.extend(frame)
        elif isinstance(frame, dict):
            out.append(frame)
    return out


async def _wait_for_callback(state: dict[str, Any], deadline_seconds: float = 1.0) -> Any:
    """Spin until subscribe_to_task has captured a callback for any task UUID."""
    deadline = asyncio.get_running_loop().time() + deadline_seconds
    while not state["callbacks"]:
        if asyncio.get_running_loop().time() > deadline:
            raise AssertionError("Callback never registered within deadline")
        await asyncio.sleep(0.01)
    return next(iter(state["callbacks"].items()))


SAMPLE_PARAMS: dict[str, Any] = {
    "taskType": "imageInference",
    "model": "runware:101@1",
    "positivePrompt": "x",
    "width": 1024,
    "height": 1024,
    # No explicit deliveryMethod → defaults to "async" (this is what we test).
}


class TestAsyncWsHappyPath:
    @pytest.mark.asyncio
    async def test_ack_then_terminal_in_first_poll(self) -> None:
        client = Runware(api_key="sk-test", transport="websocket")
        _mock, state = _patch_ws(client)

        run_task = _run_in_background(client.run(SAMPLE_PARAMS))
        task_uuid, callback = await _wait_for_callback(state)

        # Phase 1: empty ACK frame.
        callback({"data": []})
        # Phase 2: poll result with a terminal item.
        await asyncio.sleep(0.05)
        callback(
            {
                "data": [
                    {
                        "taskUUID": task_uuid,
                        "imageURL": "https://x.jpg",
                        "imageUUID": "i1",
                    }
                ]
            }
        )

        result = await run_task
        assert len(result) == 1
        assert result[0]["imageURL"] == "https://x.jpg"
        # Wire: original task + at least one getResponse.
        wire = _flatten_sent(state["sent"])
        original = [t for t in wire if t.get("taskType") == "imageInference"]
        polls = [t for t in wire if t.get("taskType") == "getResponse"]
        assert len(original) == 1
        assert original[0]["deliveryMethod"] == "async"
        assert len(polls) >= 1
        await client.close()

    @pytest.mark.asyncio
    async def test_terminal_data_in_ack_frame_skips_polling(self) -> None:
        """If the server returns data on the first frame, no polls are needed."""
        client = Runware(api_key="sk-test", transport="websocket")
        _mock, state = _patch_ws(client)

        run_task = _run_in_background(client.run(SAMPLE_PARAMS))
        task_uuid, callback = await _wait_for_callback(state)

        callback(
            {
                "data": [
                    {
                        "taskUUID": task_uuid,
                        "imageURL": "https://x.jpg",
                        "imageUUID": "i1",
                    }
                ]
            }
        )

        result = await run_task
        assert len(result) == 1
        wire = _flatten_sent(state["sent"])
        polls = [t for t in wire if t.get("taskType") == "getResponse"]
        assert polls == []
        await client.close()


class TestAsyncWsErrors:
    @pytest.mark.asyncio
    async def test_error_during_ack_rejects(self) -> None:
        client = Runware(api_key="sk-test", transport="websocket")
        _mock, state = _patch_ws(client)

        run_task = _run_in_background(client.run(SAMPLE_PARAMS))
        _task_uuid, callback = await _wait_for_callback(state)

        callback({"error": [{"code": "invalidPositivePrompt", "message": "bad"}]})

        with pytest.raises(RunwareError) as exc_info:
            await run_task
        assert exc_info.value.code == "validation"
        assert "bad" in exc_info.value.message
        await client.close()

    @pytest.mark.asyncio
    async def test_error_during_polling_rejects(self) -> None:
        client = Runware(api_key="sk-test", transport="websocket")
        _mock, state = _patch_ws(client)

        run_task = _run_in_background(client.run(SAMPLE_PARAMS))
        _task_uuid, callback = await _wait_for_callback(state)

        # Phase 1: clean ACK
        callback({"data": []})
        # Phase 2: error during polling
        await asyncio.sleep(0.05)
        callback({"error": [{"code": "inferenceError", "message": "provider down"}]})

        with pytest.raises(RunwareError) as exc_info:
            await run_task
        assert exc_info.value.code == "provider"
        await client.close()

    @pytest.mark.asyncio
    async def test_unsubscribes_on_completion(self) -> None:
        client = Runware(api_key="sk-test", transport="websocket")
        _mock, state = _patch_ws(client)

        run_task = _run_in_background(client.run(SAMPLE_PARAMS))
        task_uuid, callback = await _wait_for_callback(state)

        callback(
            {
                "data": [
                    {
                        "taskUUID": task_uuid,
                        "imageURL": "https://x.jpg",
                        "imageUUID": "i1",
                    }
                ]
            }
        )

        await run_task
        assert task_uuid in state["unsubscribed"]
        await client.close()

    @pytest.mark.asyncio
    async def test_unsubscribes_on_error(self) -> None:
        client = Runware(api_key="sk-test", transport="websocket")
        _mock, state = _patch_ws(client)

        run_task = _run_in_background(client.run(SAMPLE_PARAMS))
        task_uuid, callback = await _wait_for_callback(state)

        callback({"error": [{"code": "invalidPositivePrompt", "message": "bad"}]})

        with pytest.raises(RunwareError):
            await run_task
        assert task_uuid in state["unsubscribed"]
        await client.close()


class TestAsyncWsCancellation:
    @pytest.mark.asyncio
    async def test_cancel_event_during_polling_raises_aborted(self) -> None:
        from runware import RunOptions

        client = Runware(api_key="sk-test", transport="websocket")
        _mock, state = _patch_ws(client)

        cancel = asyncio.Event()
        run_task = _run_in_background(client.run(SAMPLE_PARAMS, RunOptions(cancel_event=cancel)))
        _task_uuid, callback = await _wait_for_callback(state)

        # Phase 1 ACK
        callback({"data": []})
        await asyncio.sleep(0.05)
        cancel.set()

        with pytest.raises(RunwareError) as exc_info:
            await run_task
        assert exc_info.value.code == "aborted"
        await client.close()
