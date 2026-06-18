"""
Integration smoke tests against the production Runware API.

Gated on the RUNWARE_API_KEY env var. Skipped (not failed) when unset, so
default `uv run pytest` runs stay hermetic. Run explicitly with:

    RUNWARE_API_KEY=... uv run pytest tests/integration/

Keep this suite tight and use the cheapest/fastest models — these tests cost
real credits and depend on a live API.
"""

from __future__ import annotations

import os

import pytest

from runware import Runware, RunwareError, is_runware_error

API_KEY = os.environ.get("RUNWARE_API_KEY")
pytestmark = pytest.mark.skipif(not API_KEY, reason="RUNWARE_API_KEY not set")

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
