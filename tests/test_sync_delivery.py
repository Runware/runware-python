"""
Tests for ``client.run({'deliveryMethod': 'sync'})`` on the REST transport.

The async-polling path is exercised by ``test_rest_polling.py`` and
``test_ws_async_polling.py``. These tests pin the sync contract:

  - REST + sync: one HTTP call, no ``getResponse`` polling.
  - REST + sync: errors propagate without entering a polling loop.

The WebSocket sync variant requires a full mock of the websockets connection
lifecycle, which is covered by integration tests against a real server.
"""

from __future__ import annotations

from typing import Any, cast

import aiohttp
import pytest

from runware import RuntimeDependencies, Runware, RunwareError

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
