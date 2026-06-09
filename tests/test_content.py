"""Tests for the content namespace.

Mock at the aiohttp.ClientSession boundary so we exercise URL building,
query construction, and error mapping without hitting the network.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any
from unittest.mock import AsyncMock, MagicMock

import aiohttp
import pytest

from runware import RunwareError
from runware.content import ContentClient


def _mock_session(
    *,
    status: int = 200,
    body: object = None,
    raises: Exception | None = None,
) -> tuple[MagicMock, list[str]]:
    """Build a fake aiohttp.ClientSession that records every URL it was asked
    for. ``raises`` simulates network-level failures; otherwise the response
    yields ``body`` with ``status``.
    """
    calls: list[str] = []

    response = MagicMock()
    response.status = status
    response.json = AsyncMock(return_value=body)

    @asynccontextmanager
    async def fake_get(url: str):  # type: ignore[no-untyped-def]
        calls.append(url)
        if raises is not None:
            raise raises
        yield response

    session = MagicMock()
    session.get = fake_get
    return session, calls


def _client(session: MagicMock) -> ContentClient:
    async def provider() -> aiohttp.ClientSession:
        return session  # type: ignore[return-value]

    return ContentClient(provider)


@pytest.mark.asyncio
class TestListModels:
    async def test_hits_models_endpoint(self):
        session, calls = _mock_session(body=[{"air": "runware:101@1", "name": "FLUX.1 dev"}])
        result = await _client(session).list_models()
        assert calls[0] == "https://content.runware.ai/models"
        assert isinstance(result, list)
        assert result[0].get("air") == "runware:101@1"

    async def test_forwards_filters_to_query_string(self):
        session, calls = _mock_session(body=[])
        _ = await _client(session).list_models({
            "capability": "io:text-to-image",
            "category": "image",
            "creator": "google",
            "search": "flux",
            "sort": "releasedAt",
            "order": "desc",
            "limit": 25,
            "offset": 50,
        })
        url = calls[0]
        assert "capability=io%3Atext-to-image" in url
        assert "category=image" in url
        assert "creator=google" in url
        assert "q=flux" in url
        assert "sort=releasedAt" in url
        assert "order=desc" in url
        assert "limit=25" in url
        assert "offset=50" in url

    async def test_paginate_true_encodes_param(self):
        envelope: dict[str, Any] = {"total": 100, "limit": 20, "offset": 0, "items": []}
        session, calls = _mock_session(body=envelope)
        result = await _client(session).list_models({"paginate": True})
        assert "paginate=true" in calls[0]
        assert result == envelope


@pytest.mark.asyncio
class TestGetModel:
    async def test_url_encodes_id(self):
        session, calls = _mock_session(body={"air": "runware:101@1"})
        _ = await _client(session).get_model("flux 1/dev")
        assert calls[0] == "https://content.runware.ai/models/flux%201%2Fdev"

    async def test_returns_none_on_404(self):
        session, _ = _mock_session(status=404)
        result = await _client(session).get_model("does-not-exist")
        assert result is None

    async def test_raises_on_non_404_error(self):
        session, _ = _mock_session(status=500)
        with pytest.raises(RunwareError):
            _ = await _client(session).get_model("flux-1-dev")

    async def test_raises_on_network_failure_with_code_connection(self):
        session, _ = _mock_session(raises=aiohttp.ClientConnectionError("network down"))
        with pytest.raises(RunwareError) as exc_info:
            _ = await _client(session).get_model("flux-1-dev")
        # Maps to ErrorCode 'connection' — keep aligned with TS SDK so
        # cross-language callers can branch on the same code.
        assert exc_info.value.code == "connection"


@pytest.mark.asyncio
class TestGetModelExamples:
    async def test_hits_examples_endpoint(self):
        session, calls = _mock_session(body=[])
        _ = await _client(session).get_model_examples("flux-1-dev")
        assert calls[0] == "https://content.runware.ai/models/flux-1-dev/examples"

    async def test_forwards_capability_filter(self):
        session, calls = _mock_session(body=[])
        _ = await _client(session).get_model_examples(
            "flux-1-dev", {"capability": "io:text-to-image"},
        )
        assert "capability=io%3Atext-to-image" in calls[0]

    async def test_returns_empty_list_on_404_instead_of_raising(self):
        session, _ = _mock_session(status=404)
        result = await _client(session).get_model_examples("not-found")
        assert result == []


@pytest.mark.asyncio
class TestGetModelGuides:
    async def test_returns_array(self):
        body = [{"slug": "g1", "title": "Guide", "description": "...", "url": "https://x"}]
        session, _ = _mock_session(body=body)
        result = await _client(session).get_model_guides("flux-1-dev")
        assert len(result) == 1
        assert result[0].get("slug") == "g1"

    async def test_returns_empty_list_on_404_instead_of_raising(self):
        session, _ = _mock_session(status=404)
        result = await _client(session).get_model_guides("not-found")
        assert result == []


@pytest.mark.asyncio
class TestGetModelPricing:
    async def test_returns_payload(self):
        body: dict[str, Any] = {"air": "runware:101@1", "pricingOverview": "$0.0025/MP"}
        session, calls = _mock_session(body=body)
        result = await _client(session).get_model_pricing("flux-1-dev")
        assert calls[0] == "https://content.runware.ai/models/flux-1-dev/pricing"
        assert result is not None
        assert result.get("pricingOverview") == "$0.0025/MP"

    async def test_returns_none_on_404(self):
        session, _ = _mock_session(status=404)
        result = await _client(session).get_model_pricing("no-pricing")
        assert result is None


@pytest.mark.asyncio
class TestListCollections:
    async def test_forwards_category_filter(self):
        session, calls = _mock_session(body=[])
        _ = await _client(session).list_collections({"category": "image"})
        assert "category=image" in calls[0]


@pytest.mark.asyncio
class TestGetCollection:
    async def test_returns_payload(self):
        body: dict[str, Any] = {"id": "best-image", "name": "Best Image", "models": []}
        session, calls = _mock_session(body=body)
        result = await _client(session).get_collection("best-image")
        assert calls[0] == "https://content.runware.ai/collections/best-image"
        assert result is not None
        assert result.get("id") == "best-image"

    async def test_returns_none_on_404(self):
        session, _ = _mock_session(status=404)
        result = await _client(session).get_collection("does-not-exist")
        assert result is None


@pytest.mark.asyncio
class TestListCapabilities:
    async def test_returns_array(self):
        body = [{"id": "io:text-to-image", "label": "Text to Image"}]
        session, _ = _mock_session(body=body)
        result = await _client(session).list_capabilities()
        assert len(result) == 1
        assert result[0]["id"] == "io:text-to-image"


@pytest.mark.asyncio
class TestListCreators:
    async def test_returns_creators_with_their_models(self):
        body: list[dict[str, Any]] = [{
            "id": "google",
            "name": "Google",
            "models": [{"air": "google:1@1", "name": "Veo"}],
        }]
        session, calls = _mock_session(body=body)
        result = await _client(session).list_creators()
        assert calls[0] == "https://content.runware.ai/creators"
        assert result[0].get("id") == "google"
        assert len(result[0].get("models", [])) == 1


@pytest.mark.asyncio
class TestGetCreator:
    async def test_returns_payload(self):
        body: dict[str, Any] = {"id": "google", "name": "Google", "models": []}
        session, calls = _mock_session(body=body)
        result = await _client(session).get_creator("google")
        assert calls[0] == "https://content.runware.ai/creators/google"
        assert result is not None
        assert result.get("id") == "google"

    async def test_returns_none_on_404(self):
        session, _ = _mock_session(status=404)
        result = await _client(session).get_creator("mystery-co")
        assert result is None


@pytest.mark.asyncio
class TestSpecialCharsInFilters:
    async def test_url_encodes_colon_in_capability(self):
        session, calls = _mock_session(body=[])
        _ = await _client(session).list_models({"capability": "io:text-to-image"})
        assert "capability=io%3Atext-to-image" in calls[0]
