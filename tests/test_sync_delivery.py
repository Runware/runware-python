"""
Tests for ``client.run({'deliveryMethod': 'sync'})`` on the REST transport.

The async-polling path is exercised by ``test_rest_polling.py`` and
``test_ws_async_polling.py``. These tests pin the sync contract:

  - REST + sync: one HTTP call, no ``getResponse`` polling.
  - REST + sync: errors propagate without entering a polling loop.
  - REST + sync: a task still processing after the server wait is polled
    with ``getResponse`` until it finishes.

The WebSocket sync variant requires a full mock of the websockets connection
lifecycle, which is covered by integration tests against a real server.
"""

from __future__ import annotations

from typing import Any, cast

import aiohttp
import pytest

from runware import RunOptions, RuntimeDependencies, Runware, RunwareError

from ._mocks import MockResponse, MockSession

SAMPLE_PARAMS: dict[str, Any] = {
    "taskType": "imageInference",
    "model": "civitai:1@1",
    "positivePrompt": "x",
    "width": 512,
    "height": 512,
    "deliveryMethod": "sync",
}

URL = "https://api.runware.ai/v1"


def _client_with(session: MockSession) -> Runware:
    return Runware(
        api_key="sk-test",
        transport="rest",
        dependencies=RuntimeDependencies(
            session=cast(aiohttp.ClientSession, cast(object, session))
        ),
    )


class TestRestSyncSuccess:
    @pytest.mark.asyncio
    async def test_returns_result_in_single_call(self) -> None:
        session = MockSession()
        session.add(
            "POST",
            URL,
            MockResponse(
                payload={
                    "data": [{"taskUUID": "sync-1", "imageURL": "https://result.jpg"}]
                }
            ),
        )
        client = _client_with(session)
        try:
            result = await client.run(SAMPLE_PARAMS)
            assert len(result) == 1
            assert result[0]["imageURL"] == "https://result.jpg"
            # Exactly one POST — no getResponse polling fires.
            assert session.count("POST", URL) == 1
        finally:
            await client.close()

    @pytest.mark.asyncio
    async def test_delivery_method_sync_on_wire(self) -> None:
        session = MockSession()
        session.add(
            "POST",
            URL,
            MockResponse(
                payload={
                    "data": [{"taskUUID": "sync-2", "imageURL": "https://x.jpg"}]
                }
            ),
        )
        client = _client_with(session)
        try:
            await client.run(SAMPLE_PARAMS)
        finally:
            await client.close()
        sent = session.request_log[0].json_body
        assert isinstance(sent, list)
        assert sent[0]["deliveryMethod"] == "sync"
        assert sent[0]["taskType"] == "imageInference"

    @pytest.mark.asyncio
    async def test_no_getresponse_polling(self) -> None:
        session = MockSession()
        session.add(
            "POST",
            URL,
            MockResponse(
                payload={
                    "data": [
                        {"taskUUID": "sync-3", "imageURL": "https://x.jpg"}
                    ]
                }
            ),
        )
        client = _client_with(session)
        try:
            await client.run(SAMPLE_PARAMS)
        finally:
            await client.close()
        # No request body ever contains a getResponse task.
        for log in session.request_log:
            sent = log.json_body
            assert isinstance(sent, list)
            for task in sent:
                assert task.get("taskType") != "getResponse"


class TestRestSyncErrors:
    @pytest.mark.asyncio
    async def test_propagates_error_without_polling(self) -> None:
        session = MockSession()
        session.add(
            "POST",
            URL,
            MockResponse(
                status=400,
                payload={
                    "errors": [
                        {
                            "code": "invalidPositivePrompt",
                            "message": "bad prompt",
                            "taskUUID": "sync-err",
                        }
                    ]
                },
            ),
        )
        client = _client_with(session)
        try:
            with pytest.raises(RunwareError) as exc_info:
                await client.run(SAMPLE_PARAMS)
            assert "bad prompt" in exc_info.value.message
            # Only the initial POST fired — no polling loop entered.
            assert session.count("POST", URL) == 1
        finally:
            await client.close()


def _handoff_row(**fields: Any) -> dict[str, Any]:
    return {"taskType": "imageInference", "taskUUID": "handoff-1", **fields}


def _sent_task_types(session: MockSession) -> list[str]:
    task_types: list[str] = []
    for log in session.request_log:
        sent = cast(list[dict[str, Any]], log.json_body)
        task_types.append(sent[0]["taskType"])
    return task_types


HANDOFF_PARAMS: dict[str, Any] = {**SAMPLE_PARAMS, "taskUUID": "handoff-1"}
PROCESSING_ROW = _handoff_row(status="processing")


class TestRestSyncHandoff:
    @pytest.mark.asyncio
    async def test_polls_getresponse_for_the_late_result(self) -> None:
        success = _handoff_row(
            status="success", imageUUID="img-1", imageURL="https://result.jpg",
        )
        session = MockSession()
        session.add("POST", URL, MockResponse(payload={"data": [PROCESSING_ROW]}))
        session.add("POST", URL, MockResponse(payload={"data": [PROCESSING_ROW]}))
        session.add("POST", URL, MockResponse(payload={"data": [success]}))
        results: list[dict[str, Any]] = []
        client = _client_with(session)
        try:
            result = await client.run(
                HANDOFF_PARAMS, RunOptions(on_result=results.append),
            )
        finally:
            await client.close()
        assert result == [success]
        assert results == [success]
        assert _sent_task_types(session) == ["imageInference", "getResponse", "getResponse"]
        poll = cast(list[dict[str, Any]], session.request_log[1].json_body)
        assert poll[0]["taskUUID"] == "handoff-1"

    @pytest.mark.asyncio
    async def test_returns_every_result_once_when_some_arrived_first(self) -> None:
        first = _handoff_row(imageUUID="img-1", imageURL="https://one.jpg")
        polled = [
            {**first, "status": "success"},
            _handoff_row(status="success", imageUUID="img-2", imageURL="https://two.jpg"),
        ]
        session = MockSession()
        session.add("POST", URL, MockResponse(payload={"data": [first, PROCESSING_ROW]}))
        session.add("POST", URL, MockResponse(payload={"data": polled}))
        client = _client_with(session)
        try:
            result = await client.run({**HANDOFF_PARAMS, "numberResults": 2})
        finally:
            await client.close()
        assert result == polled

    @pytest.mark.asyncio
    async def test_raises_the_error_the_task_ends_in(self) -> None:
        failed = {
            "errors": [
                _handoff_row(code="timeoutProvider", message="The provider did not respond"),
            ],
        }
        session = MockSession()
        session.add("POST", URL, MockResponse(payload={"data": [PROCESSING_ROW]}))
        session.add("POST", URL, MockResponse(payload=failed))
        client = _client_with(session)
        try:
            with pytest.raises(RunwareError) as exc_info:
                await client.run(HANDOFF_PARAMS)
        finally:
            await client.close()
        assert "did not respond" in exc_info.value.message

    @pytest.mark.asyncio
    async def test_leaves_a_getresponse_processing_row_untouched(self) -> None:
        session = MockSession()
        session.add("POST", URL, MockResponse(payload={"data": [PROCESSING_ROW]}))
        client = _client_with(session)
        try:
            result = await client.get_response({"taskUUID": "handoff-1"})
        finally:
            await client.close()
        assert result == [PROCESSING_ROW]
        assert session.count("POST", URL) == 1
