"""Tests for validate.py — fastjsonschema integration, dedupe."""

from __future__ import annotations

import asyncio
from typing import Any, cast

import aiohttp
import pytest

from runware import RunwareError, is_runware_error
from runware._docs_cache import get_docs_url_for_model
from runware.logger import create_logger
from runware.validate import (
    clear_validator_cache,
    validate_tasks,
)

from ._mocks import MockResponse, MockSession

SDXL_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "taskType": {"type": "string"},
        "taskUUID": {"type": "string"},
        "model": {"type": "string"},
        "positivePrompt": {"type": "string"},
        "width": {"type": "integer"},
        "height": {"type": "integer"},
    },
    "required": [
        "taskType",
        "taskUUID",
        "model",
        "positivePrompt",
        "width",
        "height",
    ],
}


@pytest.fixture(autouse=True)
def _reset_validator_cache() -> None:
    """Reset the in-process cache before each test."""
    clear_validator_cache()


def _resolve_url(model: str) -> str:
    return f"https://schemas.runware.ai/resolve/{model}"


def _session_with(
    model: str, schema: dict[str, Any] | None, *, status: int = 200, repeat: int = 1
) -> MockSession:
    session = MockSession()
    body = {"requestSchema": schema, "responseSchema": None}
    for _ in range(repeat):
        session.add("GET", _resolve_url(model), MockResponse(status=status, payload=body))
    return session


def _as_aiohttp(session: MockSession) -> aiohttp.ClientSession:
    # Bridge via object — MockSession only emulates the .get() method
    # we exercise; pyright (correctly) won't take it for the full
    # ClientSession surface, so go through object first.
    return cast(aiohttp.ClientSession, cast(object, session))


class TestValidateTasks:
    @pytest.mark.asyncio
    async def test_passes_for_valid_task(self) -> None:
        session = _session_with("civitai:1@1", SDXL_SCHEMA)
        await validate_tasks(
            [
                {
                    "taskType": "imageInference",
                    "taskUUID": "u1",
                    "model": "civitai:1@1",
                    "positivePrompt": "ok",
                    "width": 1024,
                    "height": 1024,
                }
            ],
            log=create_logger(False),
            session=_as_aiohttp(session),
        )

    @pytest.mark.asyncio
    async def test_throws_when_required_field_missing(self) -> None:
        session = _session_with("civitai:2@1", SDXL_SCHEMA)
        with pytest.raises(RunwareError) as exc_info:
            await validate_tasks(
                [
                    {
                        "taskType": "imageInference",
                        "taskUUID": "u2",
                        "model": "civitai:2@1",
                        # positivePrompt missing
                        "width": 1024,
                        "height": 1024,
                    }
                ],
                log=create_logger(False),
                session=_as_aiohttp(session),
            )
        assert exc_info.value.code == "validation"
        assert exc_info.value.task_uuid == "u2"
        assert exc_info.value.task_type == "imageInference"
        assert exc_info.value.validation_errors is not None

    @pytest.mark.asyncio
    async def test_throws_when_type_is_wrong(self) -> None:
        session = _session_with("civitai:3@1", SDXL_SCHEMA)
        with pytest.raises(RunwareError) as exc_info:
            await validate_tasks(
                [
                    {
                        "taskType": "imageInference",
                        "taskUUID": "u3",
                        "model": "civitai:3@1",
                        "positivePrompt": "ok",
                        "width": "not-a-number",  # wrong type
                        "height": 1024,
                    }
                ],
                log=create_logger(False),
                session=_as_aiohttp(session),
            )
        assert exc_info.value.code == "validation"

    @pytest.mark.asyncio
    async def test_skips_when_resolve_returns_404(self) -> None:
        session = MockSession()
        session.add(
            "GET",
            _resolve_url("unknown:0@0"),
            MockResponse(status=404, payload={}),
        )
        # No exception — non-curated models get skipped.
        await validate_tasks(
            [
                {
                    "taskType": "imageInference",
                    "taskUUID": "u4",
                    "model": "unknown:0@0",
                    "anythingGoes": True,
                }
            ],
            log=create_logger(False),
            session=_as_aiohttp(session),
        )

    @pytest.mark.asyncio
    async def test_skips_when_network_fails(self) -> None:
        session = MockSession()
        session.add(
            "GET",
            _resolve_url("something:0@0"),
            MockResponse(exception=aiohttp.ClientConnectionError("network down")),
        )
        await validate_tasks(
            [
                {
                    "taskType": "imageInference",
                    "taskUUID": "u5",
                    "model": "something:0@0",
                    "anythingGoes": True,
                }
            ],
            log=create_logger(False),
            session=_as_aiohttp(session),
        )

    @pytest.mark.asyncio
    async def test_skips_when_task_has_no_model(self) -> None:
        session = MockSession()
        await validate_tasks(
            [{"taskType": "getResponse", "taskUUID": "u6"}],
            log=create_logger(False),
            session=_as_aiohttp(session),
        )
        # No HTTP call should have happened.
        assert len(session.request_log) == 0

    @pytest.mark.asyncio
    async def test_caches_validators_per_model(self) -> None:
        session = _session_with("civitai:cached@1", SDXL_SCHEMA)
        valid: dict[str, Any] = {
            "taskType": "imageInference",
            "taskUUID": "u-valid",
            "model": "civitai:cached@1",
            "positivePrompt": "ok",
            "width": 1024,
            "height": 1024,
        }
        log = create_logger(False)
        await validate_tasks([valid], log=log, session=_as_aiohttp(session))
        await validate_tasks([valid], log=log, session=_as_aiohttp(session))
        await validate_tasks([valid], log=log, session=_as_aiohttp(session))
        assert session.count("GET", _resolve_url("civitai:cached@1")) == 1

    @pytest.mark.asyncio
    async def test_dedupes_concurrent_first_hits(self) -> None:
        """Multiple parallel calls for the same model must share one compile."""
        session = _session_with("civitai:concurrent@1", SDXL_SCHEMA)
        tasks: list[dict[str, Any]] = [
            {
                "taskType": "imageInference",
                "taskUUID": f"u-concurrent-{i}",
                "model": "civitai:concurrent@1",
                "positivePrompt": "ok",
                "width": 1024,
                "height": 1024,
            }
            for i in range(10)
        ]
        log = create_logger(False)
        await asyncio.gather(
            *(validate_tasks([t], log=log, session=_as_aiohttp(session)) for t in tasks)
        )
        assert session.count("GET", _resolve_url("civitai:concurrent@1")) == 1

    @pytest.mark.asyncio
    async def test_caches_docs_url_from_resolve(self) -> None:
        session = MockSession()
        session.add(
            "GET",
            _resolve_url("civitai:docs@1"),
            MockResponse(
                payload={
                    "requestSchema": SDXL_SCHEMA,
                    "responseSchema": None,
                    "documentation": "https://runware.ai/docs/models/civitai-docs",
                }
            ),
        )
        await validate_tasks(
            [
                {
                    "taskType": "imageInference",
                    "taskUUID": "u-docs",
                    "model": "civitai:docs@1",
                    "positivePrompt": "ok",
                    "width": 1024,
                    "height": 1024,
                }
            ],
            log=create_logger(False),
            session=_as_aiohttp(session),
        )
        assert (
            get_docs_url_for_model("civitai:docs@1")
            == "https://runware.ai/docs/models/civitai-docs"
        )


class TestClearValidatorCache:
    @pytest.mark.asyncio
    async def test_forces_re_fetch_on_next_call(self) -> None:
        session = _session_with("civitai:reset@1", SDXL_SCHEMA, repeat=2)
        task: dict[str, Any] = {
            "taskType": "imageInference",
            "taskUUID": "u-reset",
            "model": "civitai:reset@1",
            "positivePrompt": "ok",
            "width": 1024,
            "height": 1024,
        }
        log = create_logger(False)
        await validate_tasks([task], log=log, session=_as_aiohttp(session))
        assert session.count("GET", _resolve_url("civitai:reset@1")) == 1

        clear_validator_cache()

        await validate_tasks([task], log=log, session=_as_aiohttp(session))
        assert session.count("GET", _resolve_url("civitai:reset@1")) == 2


class TestErrorIsRunwareError:
    @pytest.mark.asyncio
    async def test_error_shape_is_runware_error(self) -> None:
        session = _session_with("civitai:err@1", SDXL_SCHEMA)
        try:
            await validate_tasks(
                [
                    {
                        "taskType": "imageInference",
                        "taskUUID": "u-err",
                        "model": "civitai:err@1",
                        "width": 1024,
                        "height": 1024,
                    }
                ],
                log=create_logger(False),
                session=_as_aiohttp(session),
            )
            pytest.fail("expected to throw")
        except RunwareError as err:
            assert is_runware_error(err)
            assert err.code == "validation"
            assert err.task_type == "imageInference"
            assert err.task_uuid == "u-err"
            assert err.validation_errors is not None
