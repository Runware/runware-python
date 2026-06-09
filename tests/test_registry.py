"""Tests for runware/registry.py — TTL, ETag, offline fallback."""

from __future__ import annotations

from typing import Any, cast

import aiohttp
import pytest

from runware.logger import create_logger
from runware.registry import (
    Registry,
    RegistryData,
    RegistryModelEntry,
    create_registry,
)

from ._mocks import MockResponse, MockSession

SAMPLE_REGISTRY: dict[str, Any] = {
    "version": "20260603T0000",
    "models": {
        "runware:101@1": {"taskType": "imageInference", "id": "flux-1-dev"},
        "runware:400@1": {"taskType": "imageInference", "id": "flux-2-dev"},
    },
    "architectureTaskTypes": {
        "sdxl": "imageInference",
        "flux-1-dev": "imageInference",
    },
    "modalityTaskTypes": {
        "image": "imageInference",
        "video": "videoInference",
    },
}

URL = "https://schemas.runware.ai/registry.json"


def _as_aiohttp(session: MockSession) -> aiohttp.ClientSession:
    # Bridge via object — MockSession only emulates the .get() method
    # we exercise; pyright (correctly) won't take it for the full
    # ClientSession surface, so go through object first.
    return cast(aiohttp.ClientSession, cast(object, session))


def _make_registry(session: MockSession, fallback: RegistryData | None = None) -> Registry:
    return create_registry(
        url=URL,
        log=create_logger(False),
        fallback=fallback,
        session=_as_aiohttp(session),
    )


class TestFetch:
    @pytest.mark.asyncio
    async def test_fetches_on_first_call(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        reg = _make_registry(session)
        try:
            assert await reg.get_model_task_type("runware:101@1") == "imageInference"
            assert session.count("GET", URL) == 1
        finally:
            await reg.close()

    @pytest.mark.asyncio
    async def test_cache_hit_within_ttl(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        reg = _make_registry(session)
        try:
            await reg.get_model_task_type("runware:101@1")
            await reg.get_model_task_type("runware:400@1")
            await reg.get_architecture_task_type("sdxl")
            await reg.get_modality_task_type("image")
            # All four lookups should share one fetch.
            assert session.count("GET", URL) == 1
        finally:
            await reg.close()


class TestEtag:
    @pytest.mark.asyncio
    async def test_sends_if_none_match_on_refresh(self) -> None:
        session = MockSession()
        session.add(
            "GET",
            URL,
            MockResponse(payload=SAMPLE_REGISTRY, headers={"ETag": '"abc123"'}),
        )
        session.add("GET", URL, MockResponse(status=304))
        reg = _make_registry(session)
        try:
            await reg.get_model_task_type("runware:101@1")
            await reg.refresh()
        finally:
            await reg.close()

        # First request: no If-None-Match. Second: the ETag we received.
        assert session.request_log[0].headers.get("If-None-Match") is None
        assert session.request_log[1].headers.get("If-None-Match") == '"abc123"'


class TestFallback:
    @pytest.mark.asyncio
    async def test_uses_fallback_when_first_fetch_fails(self) -> None:
        session = MockSession()
        session.add(
            "GET",
            URL,
            MockResponse(exception=aiohttp.ClientConnectionError("nope")),
        )
        fallback = RegistryData(
            models={
                "fallback:1@1": RegistryModelEntry(task_type="textInference", id="fb-1"),
            },
            architecture_task_types={"fb-arch": "imageInference"},
            modality_task_types={"image": "imageInference"},
        )
        reg = _make_registry(session, fallback=fallback)
        try:
            assert (
                await reg.get_model_task_type("fallback:1@1") == "textInference"
            )
            assert (
                await reg.get_architecture_task_type("fb-arch") == "imageInference"
            )
        finally:
            await reg.close()

    @pytest.mark.asyncio
    async def test_returns_none_for_unknown_when_fallback_empty(self) -> None:
        session = MockSession()
        session.add(
            "GET",
            URL,
            MockResponse(exception=aiohttp.ClientConnectionError("nope")),
        )
        reg = _make_registry(session)
        try:
            assert await reg.get_model_task_type("not-in-fallback") is None
        finally:
            await reg.close()

    @pytest.mark.asyncio
    async def test_stale_on_error_returns_cached(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        session.add(
            "GET",
            URL,
            MockResponse(exception=aiohttp.ClientConnectionError("nope")),
        )
        reg = _make_registry(session)
        try:
            await reg.get_model_task_type("runware:101@1")
            await reg.refresh()
            # After refresh fails, the cached data should still answer.
            assert (
                await reg.get_model_task_type("runware:101@1") == "imageInference"
            )
        finally:
            await reg.close()


class TestRefresh:
    @pytest.mark.asyncio
    async def test_refresh_forces_re_fetch(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        reg = _make_registry(session)
        try:
            await reg.get_model_task_type("runware:101@1")
            await reg.refresh()
            assert session.count("GET", URL) == 2
        finally:
            await reg.close()


class TestModelLookup:
    @pytest.mark.asyncio
    async def test_get_model_id_returns_curated_slug(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        reg = _make_registry(session)
        try:
            assert await reg.get_model_id("runware:101@1") == "flux-1-dev"
            assert await reg.get_model_id("not-known") is None
        finally:
            await reg.close()

    @pytest.mark.asyncio
    async def test_resolve_model_air_with_air_returns_air(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        reg = _make_registry(session)
        try:
            assert await reg.resolve_model_air("runware:101@1") == "runware:101@1"
        finally:
            await reg.close()

    @pytest.mark.asyncio
    async def test_resolve_model_air_with_slug_returns_air(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        reg = _make_registry(session)
        try:
            assert await reg.resolve_model_air("flux-1-dev") == "runware:101@1"
            assert await reg.resolve_model_air("flux-2-dev") == "runware:400@1"
        finally:
            await reg.close()

    @pytest.mark.asyncio
    async def test_resolve_model_air_unknown_returns_none(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        reg = _make_registry(session)
        try:
            assert await reg.resolve_model_air("never-heard-of-this") is None
        finally:
            await reg.close()

    @pytest.mark.asyncio
    async def test_get_model_task_type_resolves_via_slug(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        reg = _make_registry(session)
        try:
            assert (
                await reg.get_model_task_type("flux-1-dev") == "imageInference"
            )
        finally:
            await reg.close()


class TestVersion:
    @pytest.mark.asyncio
    async def test_get_version_returns_cached_version(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        reg = _make_registry(session)
        try:
            assert reg.get_version() is None
            await reg.get_model_task_type("runware:101@1")
            assert reg.get_version() == SAMPLE_REGISTRY["version"]
        finally:
            await reg.close()

    @pytest.mark.asyncio
    async def test_notify_version_same_is_noop(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        reg = _make_registry(session)
        try:
            await reg.get_model_task_type("runware:101@1")
            assert session.count("GET", URL) == 1
            reg.notify_version(cast(str, SAMPLE_REGISTRY["version"]))
            # Wait one tick for any background work; none should have fired.
            import asyncio
            await asyncio.sleep(0.05)
            assert session.count("GET", URL) == 1
        finally:
            await reg.close()


class TestParsedShapes:
    @pytest.mark.asyncio
    async def test_models_dict_is_typed(self) -> None:
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=SAMPLE_REGISTRY))
        reg = _make_registry(session)
        try:
            assert (
                await reg.get_model_task_type("runware:400@1") == "imageInference"
            )
        finally:
            await reg.close()

    @pytest.mark.asyncio
    async def test_skips_malformed_model_entries(self) -> None:
        bad: dict[str, Any] = {
            "version": "x",
            "models": {
                "good:1@1": {"taskType": "imageInference", "id": "g"},
                "bad:1@1": {"taskType": 42, "id": "b"},  # invalid type
            },
            "architectureTaskTypes": {},
            "modalityTaskTypes": {},
        }
        session = MockSession()
        session.add("GET", URL, MockResponse(payload=bad))
        reg = _make_registry(session)
        try:
            assert await reg.get_model_task_type("good:1@1") == "imageInference"
            assert await reg.get_model_task_type("bad:1@1") is None
        finally:
            await reg.close()
