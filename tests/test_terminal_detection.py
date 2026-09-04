"""
Tests for terminal-result detection.

The collector decides a task is finished by recognising a *terminal* item. Any
result it fails to recognise is treated as a progress update and dropped, so the
call polls until `poll_timeout` and raises, even though the task succeeded and
was billed.

Two shapes were unrecognised:

- Results that are not a plain image/video/audio URL: masking (`maskImageURL`),
  preprocessing (`guideImageURL`), 3D and training (`outputs`), and structured
  captions (`structuredData`).
- Any modality requested as base64 or data URI only, where no `*URL` comes back.

The async-polling status fallback could have caught all of these, but it tested
for `"completed"`, which is not a value the API sends. The documented statuses
are `processing`, `success`, and `error`.
"""

from __future__ import annotations

from typing import Any

import pytest

from runware import RunOptions, Runware
from runware.client import _is_terminal

from .test_rest_polling import _patch_transport

# --------------------------------------------------------------- unit: status

def test_status_success_is_terminal() -> None:
    # `success` is what get-response.json actually returns; `completed` is not
    # a status the API sends.
    assert _is_terminal({"taskUUID": "u1", "status": "success"}) is True


def test_status_processing_is_not_terminal() -> None:
    assert _is_terminal({"taskUUID": "u1", "status": "processing"}) is False


# ------------------------------------------------- unit: non-URL result shapes

def test_masking_result_is_terminal() -> None:
    assert _is_terminal({
        "taskType": "imageMasking",
        "taskUUID": "u1",
        "maskImageUUID": "m-1",
        "maskImageURL": "https://im.runware.ai/mask.png",
        "detections": [{"label": "face"}],
        "inputImageUUID": "in-1",
    }) is True


def test_preprocess_guide_image_is_terminal() -> None:
    assert _is_terminal({
        "taskType": "controlNetPreprocess",
        "taskUUID": "u1",
        "guideImageUUID": "g-1",
        "guideImageURL": "https://im.runware.ai/guide.png",
    }) is True


def test_three_d_outputs_is_terminal() -> None:
    assert _is_terminal({
        "taskType": "3dInference",
        "taskUUID": "u1",
        "outputs": {"files": [{"url": "https://im.runware.ai/model.glb"}]},
    }) is True


def test_training_result_is_terminal() -> None:
    assert _is_terminal({
        "taskType": "training",
        "taskUUID": "u1",
        "air": "myorg:42@1",
        "outputs": {"files": []},
    }) is True


def test_structured_caption_is_terminal() -> None:
    assert _is_terminal({
        "taskType": "caption",
        "taskUUID": "u1",
        "structuredData": {"age": "30-40"},
    }) is True


# ----------------------------------------------------- unit: base64-only output

def test_base64_only_image_is_terminal() -> None:
    # outputType=base64Data returns no imageURL at all.
    assert _is_terminal({
        "taskUUID": "u1",
        "imageUUID": "i1",
        "imageBase64Data": "iVBORw0KGgo=",
    }) is True


def test_data_uri_only_video_is_terminal() -> None:
    assert _is_terminal({
        "taskUUID": "u1",
        "videoUUID": "v1",
        "videoDataURI": "data:video/mp4;base64,AAAA",
    }) is True


def test_base64_only_mask_is_terminal() -> None:
    assert _is_terminal({
        "taskUUID": "u1",
        "maskImageUUID": "m1",
        "maskImageBase64Data": "iVBORw0KGgo=",
    }) is True


# ------------------------------------------------------- unit: regression guards

def test_image_url_is_still_terminal() -> None:
    assert _is_terminal({"taskUUID": "u1", "imageURL": "https://x/i.jpg"}) is True


def test_text_result_is_still_terminal() -> None:
    assert _is_terminal({"taskUUID": "u1", "text": "hello"}) is True


def test_progress_item_is_not_terminal() -> None:
    # The guard rail on any fix: an in-flight progress frame carries a UUID but
    # no output payload, and must stay non-terminal or progress reporting breaks
    # and partial results get returned as final.
    assert _is_terminal({"taskUUID": "u1", "imageUUID": "i1", "progress": 25}) is False


def test_bare_ack_is_not_terminal() -> None:
    assert _is_terminal({"taskUUID": "u1", "taskType": "imageInference"}) is False


# ------------------------------------------------------ end-to-end: REST polling

@pytest.fixture
async def client() -> Any:
    """REST client with a short poll budget so an unrecognised result fails fast."""
    c = Runware(api_key="sk-test", transport="rest", timeout=2_000, poll_timeout=2_000)
    try:
        yield c
    finally:
        await c.close()


class TestMaskingOverPolling:
    @pytest.mark.asyncio
    async def test_masking_completes_via_polling(self, client: Runware) -> None:
        # The reported bug: a YOLO mask task polls to timeout instead of returning.
        ack: dict[str, Any] = {"data": []}
        poll: dict[str, Any] = {
            "data": [{
                "taskType": "imageMasking",
                "taskUUID": "u1",
                "status": "success",
                "maskImageUUID": "m-1",
                "maskImageURL": "https://im.runware.ai/mask.png",
                "detections": [{"label": "face"}],
                "inputImageUUID": "in-1",
            }]
        }
        _patch_transport(client, [ack, poll])

        results = await client.run({
            "taskType": "imageMasking",
            "taskUUID": "u1",
            "model": "runware:35@1",
            "inputImage": "in-1",
        })

        assert len(results) == 1
        assert results[0]["maskImageURL"] == "https://im.runware.ai/mask.png"

    @pytest.mark.asyncio
    async def test_masking_without_status_completes(self, client: Runware) -> None:
        # Sync-shaped frames carry no status, so the result keys alone must be
        # enough to recognise completion.
        ack: dict[str, Any] = {"data": []}
        poll: dict[str, Any] = {
            "data": [{
                "taskType": "imageMasking",
                "taskUUID": "u1",
                "maskImageUUID": "m-1",
                "maskImageURL": "https://im.runware.ai/mask.png",
                "detections": [],
                "inputImageUUID": "in-1",
            }]
        }
        _patch_transport(client, [ack, poll])

        results = await client.run({
            "taskType": "imageMasking",
            "taskUUID": "u1",
            "model": "runware:35@1",
            "inputImage": "in-1",
        })
        assert results[0]["maskImageUUID"] == "m-1"


class TestBase64OnlyOverPolling:
    @pytest.mark.asyncio
    async def test_base64_only_image_completes(self, client: Runware) -> None:
        ack: dict[str, Any] = {"data": []}
        poll: dict[str, Any] = {
            "data": [{
                "taskType": "imageInference",
                "taskUUID": "u1",
                "imageUUID": "i1",
                "imageBase64Data": "iVBORw0KGgo=",
            }]
        }
        _patch_transport(client, [ack, poll])

        results = await client.run({
            "taskType": "imageInference",
            "taskUUID": "u1",
            "model": "runware:101@1",
            "positivePrompt": "x",
            "width": 1024,
            "height": 1024,
            "outputType": "base64Data",
        })
        assert results[0]["imageBase64Data"] == "iVBORw0KGgo="


class TestProgressStillWorks:
    """The fix must not turn in-flight progress frames into terminal results."""

    @pytest.mark.asyncio
    async def test_progress_frames_do_not_end_the_run(self, client: Runware) -> None:
        ack: dict[str, Any] = {"data": []}
        p1: dict[str, Any] = {"data": [{"taskUUID": "u1", "imageUUID": "i1", "progress": 25}]}
        p2: dict[str, Any] = {"data": [{"taskUUID": "u1", "imageUUID": "i1", "progress": 75}]}
        done: dict[str, Any] = {
            "data": [{"taskUUID": "u1", "imageUUID": "i1", "imageURL": "https://x/done.jpg"}]
        }
        _patch_transport(client, [ack, p1, p2, done])

        seen: list[dict[str, Any]] = []
        results = await client.run(
            {
                "taskType": "imageInference",
                "taskUUID": "u1",
                "model": "runware:101@1",
                "positivePrompt": "x",
                "width": 1024,
                "height": 1024,
            },
            RunOptions(on_progress=seen.append),
        )
        assert {p["progress"] for p in seen} == {25, 75}
        assert results[0]["imageURL"] == "https://x/done.jpg"


class TestStableIds:
    """Masking and preprocessing UUIDs must key results, or a multi-result batch
    collapses onto the shared taskUUID and dedupes to a single item."""

    @pytest.mark.asyncio
    async def test_two_masks_are_not_deduped(self, client: Runware) -> None:
        ack: dict[str, Any] = {"data": []}
        poll: dict[str, Any] = {
            "data": [
                {"taskUUID": "u1", "status": "success", "maskImageUUID": "m-1",
                 "maskImageURL": "https://x/1.png"},
                {"taskUUID": "u1", "status": "success", "maskImageUUID": "m-2",
                 "maskImageURL": "https://x/2.png"},
            ]
        }
        _patch_transport(client, [ack, poll])

        results = await client.run({
            "taskType": "imageMasking",
            "taskUUID": "u1",
            "model": "runware:35@1",
            "inputImage": "in-1",
            "numberResults": 2,
        })
        assert {r["maskImageUUID"] for r in results} == {"m-1", "m-2"}
