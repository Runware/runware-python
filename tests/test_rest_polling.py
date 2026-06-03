"""
Tests for REST async polling lifecycle.

Mocks the REST transport at the send_request level so we control the sequence
of poll responses without touching the network.
"""

from __future__ import annotations

import asyncio
from typing import Any
from unittest.mock import AsyncMock

import pytest

from runware import RunOptions, Runware, RunwareError
from runware.transport.rest import RestTransport


def _patch_transport(client: Runware, responses: list[Any]) -> AsyncMock:
    """Replace the client's REST transport with a mock returning queued responses."""
    mock = AsyncMock(spec=RestTransport)
    mock.send_request = AsyncMock(side_effect=responses)
    mock.close = AsyncMock()

    async def aenter(*args: object, **kwargs: object) -> AsyncMock:
        return mock

    mock.__aenter__ = aenter
    mock.__aexit__ = AsyncMock()
    client._rest_transport = mock
    return mock


@pytest.fixture
async def client() -> Any:
    """A fresh REST-mode client with no real transport opened."""
    c = Runware(
        api_key="sk-test",
        transport_type="rest",
        timeout=5_000,
        poll_timeout=5_000,
    )
    try:
        yield c
    finally:
        await c.close()


class TestSingleAsyncRun:
    @pytest.mark.asyncio
    async def test_runs_one_image_via_polling(self, client: Runware) -> None:
        # Initial POST returns ACK (no terminal items).
        # Subsequent getResponse poll returns the terminal item.
        ack_response: dict[str, Any] = {"data": []}
        poll_response: dict[str, Any] = {
            "data": [
                {"taskUUID": "u1", "imageURL": "https://x/img.jpg", "imageUUID": "img-1"}
            ]
        }
        mock = _patch_transport(client, [ack_response, poll_response])

        results = await client.run({
            "taskType": "imageInference",
            "taskUUID": "u1",
            "model": "runware:101@1",
            "positivePrompt": "ok",
            "width": 1024,
            "height": 1024,
        })

        assert len(results) == 1
        assert results[0]["imageURL"] == "https://x/img.jpg"
        # First call = original task, subsequent = getResponse poll(s).
        assert mock.send_request.call_count >= 2
        sent_first = mock.send_request.call_args_list[0].args[0]
        assert sent_first["taskType"] == "imageInference"
        sent_second = mock.send_request.call_args_list[1].args[0]
        assert sent_second["taskType"] == "getResponse"
        assert sent_second["taskUUID"] == "u1"

    @pytest.mark.asyncio
    async def test_fires_on_result_per_terminal_item(self, client: Runware) -> None:
        results_received: list[dict[str, Any]] = []
        ack_response: dict[str, Any] = {"data": []}
        poll_response: dict[str, Any] = {
            "data": [
                {"taskUUID": "u1", "imageURL": "https://x/1.jpg", "imageUUID": "i1"}
            ]
        }
        _patch_transport(client, [ack_response, poll_response])

        await client.run(
            {
                "taskType": "imageInference",
                "taskUUID": "u1",
                "model": "runware:101@1",
                "positivePrompt": "x",
                "width": 1024,
                "height": 1024,
            },
            RunOptions(on_result=results_received.append),
        )
        assert len(results_received) == 1
        assert results_received[0]["imageURL"] == "https://x/1.jpg"

    @pytest.mark.asyncio
    async def test_fires_on_progress_per_progress_update(
        self, client: Runware
    ) -> None:
        progress_seen: list[dict[str, Any]] = []
        ack_response: dict[str, Any] = {"data": []}
        # Cumulative state: progress 25, then 75, then terminal.
        poll1: dict[str, Any] = {
            "data": [{"taskUUID": "u1", "imageUUID": "i1", "progress": 25}]
        }
        poll2: dict[str, Any] = {
            "data": [{"taskUUID": "u1", "imageUUID": "i1", "progress": 75}]
        }
        poll3: dict[str, Any] = {
            "data": [
                {"taskUUID": "u1", "imageUUID": "i1", "imageURL": "https://x/done.jpg"}
            ]
        }
        _patch_transport(client, [ack_response, poll1, poll2, poll3])

        await client.run(
            {
                "taskType": "imageInference",
                "taskUUID": "u1",
                "model": "runware:101@1",
                "positivePrompt": "x",
                "width": 1024,
                "height": 1024,
            },
            RunOptions(on_progress=progress_seen.append),
        )
        # Two unique progress values were seen.
        assert len(progress_seen) == 2
        assert {p["progress"] for p in progress_seen} == {25, 75}


class TestBatch:
    @pytest.mark.asyncio
    async def test_waits_for_all_results_in_batch(self, client: Runware) -> None:
        ack_response: dict[str, Any] = {"data": []}
        poll1: dict[str, Any] = {
            "data": [{"taskUUID": "u1", "imageURL": "https://x/1.jpg", "imageUUID": "i1"}]
        }
        # Cumulative state — i1 again plus the new i2.
        poll2: dict[str, Any] = {
            "data": [
                {"taskUUID": "u1", "imageURL": "https://x/1.jpg", "imageUUID": "i1"},
                {"taskUUID": "u1", "imageURL": "https://x/2.jpg", "imageUUID": "i2"},
            ]
        }
        _patch_transport(client, [ack_response, poll1, poll2])

        results = await client.run({
            "taskType": "imageInference",
            "taskUUID": "u1",
            "model": "runware:101@1",
            "positivePrompt": "x",
            "width": 1024,
            "height": 1024,
            "numberResults": 2,
        })
        assert len(results) == 2
        # Deduped — no duplicate i1.
        assert {r["imageUUID"] for r in results} == {"i1", "i2"}


class TestCancellation:
    @pytest.mark.asyncio
    async def test_cancel_event_aborts_polling(self, client: Runware) -> None:
        ack_response: dict[str, Any] = {"data": []}
        # All polls return no terminal items — would loop forever without cancel.
        empty_poll: dict[str, Any] = {"data": []}
        _patch_transport(
            client, [ack_response] + [empty_poll] * 50
        )

        cancel = asyncio.Event()

        async def cancel_soon() -> None:
            await asyncio.sleep(0.05)
            cancel.set()

        cancel_task = asyncio.create_task(cancel_soon())

        with pytest.raises(RunwareError) as exc_info:
            await client.run(
                {
                    "taskType": "imageInference",
                    "taskUUID": "u1",
                    "model": "runware:101@1",
                    "positivePrompt": "x",
                    "width": 1024,
                    "height": 1024,
                },
                RunOptions(cancel_event=cancel),
            )
        assert exc_info.value.code == "aborted"
        await cancel_task


class TestPerItemErrors:
    """When polling returns an item with status='error', the call must reject
    (not hang waiting for `expected_count`), and on_result callbacks must fire
    for both success and error items before the raise."""

    @pytest.mark.asyncio
    async def test_partial_failure_raises_immediately(
        self, client: Runware
    ) -> None:
        ack_response: dict[str, Any] = {"data": []}
        # numberResults=3: 1 success + 1 error item on the first poll.
        # Without the fix, the SDK would wait for a 3rd item forever.
        poll_response: dict[str, Any] = {
            "data": [
                {
                    "taskUUID": "u-multi",
                    "imageURL": "https://x/ok.jpg",
                    "imageUUID": "ok-1",
                    "status": "success",
                },
                {
                    "taskUUID": "u-multi",
                    "imageUUID": "fail-2",
                    "status": "error",
                    "error": {
                        "code": "inferenceError",
                        "message": "one of N failed",
                    },
                },
            ]
        }
        _patch_transport(client, [ack_response, poll_response])

        seen: list[str] = []

        def on_result(item: dict[str, Any]) -> None:
            seen.append(item.get("status") or "success")

        with pytest.raises(RunwareError) as exc_info:
            await client.run(
                {
                    "taskType": "imageInference",
                    "taskUUID": "u-multi",
                    "model": "runware:101@1",
                    "positivePrompt": "x",
                    "width": 1024,
                    "height": 1024,
                    "numberResults": 3,
                },
                RunOptions(on_result=on_result),
            )
        assert exc_info.value.code == "provider"
        assert "one of N failed" in exc_info.value.message
        # Callback fired for BOTH the success and the error item
        # (in TS terms: "Fire callbacks BEFORE throwing").
        assert "success" in seen
        assert "error" in seen


class TestSyncDelivery:
    @pytest.mark.asyncio
    async def test_sync_returns_immediately(self, client: Runware) -> None:
        # Sync delivery: server returns the terminal item in the same POST.
        sync_response: dict[str, Any] = {
            "data": [{"taskUUID": "u1", "imageURL": "https://x/sync.jpg", "imageUUID": "s1"}]
        }
        mock = _patch_transport(client, [sync_response])
        results = await client.run({
            "taskType": "imageInference",
            "taskUUID": "u1",
            "model": "runware:101@1",
            "positivePrompt": "x",
            "width": 1024,
            "height": 1024,
            "deliveryMethod": "sync",
        })
        assert len(results) == 1
        assert results[0]["imageURL"] == "https://x/sync.jpg"
        # Only one HTTP call — no polling for sync.
        assert mock.send_request.call_count == 1
        sent = mock.send_request.call_args.args[0]
        assert sent["deliveryMethod"] == "sync"
