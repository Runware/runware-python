"""
Integration smoke tests against the production Runware API.

Gated on the RUNWARE_API_KEY env var. Skipped (not failed) when unset, so
default `uv run pytest` runs stay hermetic. Run explicitly with:

    RUNWARE_API_KEY=... uv run pytest tests/integration/

Keep this suite tight and use the cheapest/fastest models — these tests cost
real credits and depend on a live API.
"""

from __future__ import annotations

import asyncio
import json
import os

import pytest

from runware import InvokeOptions, Runware, RunwareError, is_runware_error

API_KEY = os.environ.get("RUNWARE_API_KEY")
pytestmark = pytest.mark.skipif(not API_KEY, reason="RUNWARE_API_KEY not set")

# Serverless invocation needs a deployed app to call, which no account has by
# default, so these carry their own gate rather than riding on the API key.
# Point them at one with:
#
#   RUNWARE_SERVERLESS_BASE_URL=... RUNWARE_SERVERLESS_TEST_APP=... \
#   RUNWARE_SERVERLESS_TEST_ENDPOINT=echo uv run pytest tests/integration/
SERVERLESS_BASE = os.environ.get("RUNWARE_SERVERLESS_BASE_URL")
SERVERLESS_APP = os.environ.get("RUNWARE_SERVERLESS_TEST_APP")
SERVERLESS_ENDPOINT = os.environ.get("RUNWARE_SERVERLESS_TEST_ENDPOINT")
SERVERLESS_PAYLOAD: dict[str, object] = json.loads(
    os.environ.get("RUNWARE_SERVERLESS_TEST_PAYLOAD") or "{}",
)
serverless = pytest.mark.skipif(
    not (API_KEY and SERVERLESS_BASE and SERVERLESS_APP and SERVERLESS_ENDPOINT),
    reason="RUNWARE_SERVERLESS_* not set",
)


def serverless_client() -> Runware:
    return Runware(serverless_base_url=SERVERLESS_BASE or "", transport="rest")

IMAGE_MODEL = "runware:400@2"  # Flux 2 Klein 9b — cheap and fast
TEXT_MODEL = "google:gemma@4-31b"  # cheap and fast

IMAGE_PARAMS: dict[str, object] = {
    "taskType": "imageInference",
    "model": IMAGE_MODEL,
    "positivePrompt": "A serene mountain lake",
    "width": 1024,
    "height": 1024,
}

TEXT_PARAMS: dict[str, object] = {
    "taskType": "textInference",
    "model": TEXT_MODEL,
    "messages": [{"role": "user", "content": "Reply with exactly: hello"}],
}


# ----------------------------------------------------------- REST x async (default)

@pytest.mark.asyncio
async def test_rest_async_one_image() -> None:
    async with Runware(transport="rest") as client:
        images = await client.run(IMAGE_PARAMS)
        assert len(images) == 1
        assert isinstance(images[0].get("imageURL"), str)


@pytest.mark.asyncio
async def test_rest_async_two_images() -> None:
    async with Runware(transport="rest") as client:
        images = await client.run({**IMAGE_PARAMS, "numberResults": 2})
        assert len(images) == 2
        for img in images:
            assert isinstance(img.get("imageURL"), str)


# ----------------------------------------------------------- REST x sync

@pytest.mark.asyncio
async def test_rest_sync_one_image() -> None:
    async with Runware(transport="rest") as client:
        images = await client.run({**IMAGE_PARAMS, "deliveryMethod": "sync"})
        assert len(images) == 1
        assert isinstance(images[0].get("imageURL"), str)


# ----------------------------------------------------------- WebSocket x async (default)

@pytest.mark.asyncio
async def test_ws_async_one_image() -> None:
    async with Runware(transport="websocket") as client:
        images = await client.run(IMAGE_PARAMS)
        assert len(images) == 1
        assert isinstance(images[0].get("imageURL"), str)


@pytest.mark.asyncio
async def test_ws_async_two_images() -> None:
    async with Runware(transport="websocket") as client:
        images = await client.run({**IMAGE_PARAMS, "numberResults": 2})
        assert len(images) == 2
        for img in images:
            assert isinstance(img.get("imageURL"), str)


# ----------------------------------------------------------- WebSocket x sync

@pytest.mark.asyncio
async def test_ws_sync_one_image() -> None:
    async with Runware(transport="websocket") as client:
        images = await client.run({**IMAGE_PARAMS, "deliveryMethod": "sync"})
        assert len(images) == 1
        assert isinstance(images[0].get("imageURL"), str)


# ----------------------------------------------------------- Stream

@pytest.mark.asyncio
async def test_stream_text() -> None:
    async with Runware(transport="rest") as client:
        stream = await client.stream(TEXT_PARAMS)

        streamed = ""
        async for chunk in stream.text_stream:
            streamed += chunk
        assert len(streamed) > 0

        result = await stream.result()
        assert result.text == streamed
        assert result.finish_reason is not None


# ----------------------------------------------------------- Utility + error path

@pytest.mark.asyncio
async def test_model_search() -> None:
    async with Runware(transport="websocket") as client:
        results = await client.model_search({
            "search": "realistic",
            "category": "checkpoint",
            "limit": 3,
        })
        assert len(results) > 0


@pytest.mark.asyncio
async def test_invalid_params_raise_typed_error() -> None:
    async with Runware(transport="websocket") as client:
        with pytest.raises(RunwareError) as exc_info:
            await client.run({
                "taskType": "imageInference",
                "model": IMAGE_MODEL,
                "positivePrompt": "",
                "width": 1024,
                "height": 1024,
            })
        assert is_runware_error(exc_info.value)
        assert exc_info.value.code in ("validation", "unknown")


# ----------------------------------------------------------- serverless invoke

@serverless
@pytest.mark.asyncio
async def test_invoke_async_delivery() -> None:
    client = serverless_client()
    try:
        task = await client.invoke(
            SERVERLESS_APP or "", SERVERLESS_ENDPOINT or "", SERVERLESS_PAYLOAD,
        )
        assert task["status"] == "completed"
        assert task["appId"] == SERVERLESS_APP
        assert task["endpointPath"] == SERVERLESS_ENDPOINT
    finally:
        await client.close()


@serverless
@pytest.mark.asyncio
async def test_invoke_sync_delivery() -> None:
    client = serverless_client()
    try:
        task = await client.invoke(
            SERVERLESS_APP or "",
            SERVERLESS_ENDPOINT or "",
            SERVERLESS_PAYLOAD,
            options=InvokeOptions(delivery_method="sync"),
        )
        assert task["status"] == "completed"
    finally:
        await client.close()


@serverless
@pytest.mark.asyncio
async def test_invoke_without_waiting_then_get_task() -> None:
    client = serverless_client()
    try:
        accepted = await client.invoke(
            SERVERLESS_APP or "",
            SERVERLESS_ENDPOINT or "",
            SERVERLESS_PAYLOAD,
            options=InvokeOptions(wait=False),
        )
        assert accepted["status"] == "pending"

        task = accepted
        for _ in range(60):
            task = await client.get_task(SERVERLESS_APP or "", accepted["id"])
            if task["status"] != "pending":
                break
            await asyncio.sleep(2)
        assert task["status"] == "completed"

        # The same id is answered with the task it already names, so the
        # second call must not start a second run.
        again = await client.invoke(
            SERVERLESS_APP or "",
            SERVERLESS_ENDPOINT or "",
            SERVERLESS_PAYLOAD,
            task_id=accepted["id"],
        )
        assert again["id"] == accepted["id"]
        assert again["createdAt"] == task["createdAt"]
    finally:
        await client.close()


@serverless
@pytest.mark.asyncio
async def test_invoke_unknown_endpoint_raises() -> None:
    client = serverless_client()
    try:
        with pytest.raises(RunwareError) as excinfo:
            _ = await client.invoke(SERVERLESS_APP or "", "does-not-exist", {})
        assert excinfo.value.code == "notFound"
        assert excinfo.value.status_code == 404
        assert excinfo.value.parameter == "endpoint_path"
    finally:
        await client.close()
