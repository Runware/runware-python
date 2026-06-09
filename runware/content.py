"""Content namespace — public read-only metadata about Runware's curated
model catalog. Hits the content service directly; no API key required at
the service level, but the SDK config supplies the HTTP session so consumers
can route through proxies / mock for tests.

For the inference surface (``run``, ``stream``, etc.), use the top-level
client methods. This namespace is purely informational.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import cast
from urllib.parse import quote, urlencode

import aiohttp

from .constants import CONTENT_BASE_URL
from .errors import create_runware_error
from .types.content import (
    Capability,
    CollectionWithModels,
    CreatorWithModels,
    ExampleMetadata,
    GetModelExamplesOptions,
    GuideMetadata,
    ListCollectionsOptions,
    ListModelsOptions,
    ModelMetadata,
    PaginatedResponse,
    PricingModelListItem,
)

SessionProvider = Callable[[], Awaitable[aiohttp.ClientSession]]


class ContentClient:
    """Async client for the Runware content service."""

    _session_provider: SessionProvider
    _base_url: str

    def __init__(self, session_provider: SessionProvider) -> None:
        self._session_provider = session_provider
        self._base_url = CONTENT_BASE_URL

    async def list_models(
        self, options: ListModelsOptions | None = None,
    ) -> list[ModelMetadata] | PaginatedResponse[ModelMetadata]:
        """List curated models. Returns a flat array by default; pass
        ``{"paginate": True}`` to get a paginated envelope instead.
        """
        params = self._build_query_params(options or {})
        query = f"?{urlencode(params)}" if params else ""
        url = f"{self._base_url}/models{query}"
        result = await self._fetch_json(url, treat_404_as_none=False)
        return cast(
            "list[ModelMetadata] | PaginatedResponse[ModelMetadata]",
            result,
        )

    async def get_model(self, model_id: str) -> ModelMetadata | None:
        """Single curated model by id. Returns ``None`` if not found."""
        url = f"{self._base_url}/models/{quote(model_id, safe='')}"
        return cast(
            "ModelMetadata | None",
            await self._fetch_json(url, treat_404_as_none=True),
        )

    async def get_model_examples(
        self, model_id: str, options: GetModelExamplesOptions | None = None,
    ) -> list[ExampleMetadata]:
        """Example outputs for a curated model, optionally filtered by capability."""
        params: dict[str, str] = {}
        if options and "capability" in options:
            params["capability"] = options["capability"]
        query = f"?{urlencode(params)}" if params else ""
        url = f"{self._base_url}/models/{quote(model_id, safe='')}/examples{query}"
        result = await self._fetch_json(url, treat_404_as_none=True)
        return cast("list[ExampleMetadata]", result or [])

    async def get_model_pricing(self, model_id: str) -> PricingModelListItem | None:
        """Pricing summary for a single curated model. Null if no pricing."""
        url = f"{self._base_url}/models/{quote(model_id, safe='')}/pricing"
        return cast(
            "PricingModelListItem | None",
            await self._fetch_json(url, treat_404_as_none=True),
        )

    async def get_model_guides(self, model_id: str) -> list[GuideMetadata]:
        """Written guides attached to a curated model."""
        url = f"{self._base_url}/models/{quote(model_id, safe='')}/guides"
        result = await self._fetch_json(url, treat_404_as_none=True)
        return cast("list[GuideMetadata]", result or [])

    async def list_collections(
        self, options: ListCollectionsOptions | None = None,
    ) -> list[CollectionWithModels]:
        """List curated collections, each with their models inlined."""
        params: dict[str, str] = {}
        if options and "category" in options:
            params["category"] = options["category"]
        query = f"?{urlencode(params)}" if params else ""
        url = f"{self._base_url}/collections{query}"
        result = await self._fetch_json(url, treat_404_as_none=False)
        return cast("list[CollectionWithModels]", result or [])

    async def get_collection(self, collection_id: str) -> CollectionWithModels | None:
        """Single collection by id."""
        url = f"{self._base_url}/collections/{quote(collection_id, safe='')}"
        return cast(
            "CollectionWithModels | None",
            await self._fetch_json(url, treat_404_as_none=True),
        )

    async def list_capabilities(self) -> list[Capability]:
        """All capability metadata (io:*, op:*, form:* taxonomies)."""
        url = f"{self._base_url}/capabilities"
        result = await self._fetch_json(url, treat_404_as_none=False)
        return cast("list[Capability]", result or [])

    async def list_creators(self) -> list[CreatorWithModels]:
        """All creators, each with their curated models inlined."""
        url = f"{self._base_url}/creators"
        result = await self._fetch_json(url, treat_404_as_none=False)
        return cast("list[CreatorWithModels]", result or [])

    async def get_creator(self, creator_id: str) -> CreatorWithModels | None:
        """Single creator by id, with their curated models inlined."""
        url = f"{self._base_url}/creators/{quote(creator_id, safe='')}"
        return cast(
            "CreatorWithModels | None",
            await self._fetch_json(url, treat_404_as_none=True),
        )

    @staticmethod
    def _build_query_params(options: ListModelsOptions) -> dict[str, str]:
        params: dict[str, str] = {}
        if "capability" in options:
            params["capability"] = options["capability"]
        if "status" in options:
            params["status"] = options["status"]
        if "category" in options:
            params["category"] = options["category"]
        if "creator" in options:
            params["creator"] = options["creator"]
        if "search" in options:
            params["q"] = options["search"]
        if "sort" in options:
            params["sort"] = options["sort"]
        if "order" in options:
            params["order"] = options["order"]
        if options.get("paginate"):
            params["paginate"] = "true"
        if "limit" in options:
            params["limit"] = str(options["limit"])
        if "offset" in options:
            params["offset"] = str(options["offset"])
        return params

    async def _fetch_json(self, url: str, *, treat_404_as_none: bool) -> object | None:
        """Fetch + parse JSON. Return value is the parsed JSON (dict, list,
        scalar, or null). Callers narrow via ``cast()`` to the specific
        endpoint's shape.
        """
        session = await self._session_provider()
        try:
            async with session.get(url) as response:
                if response.status == 404 and treat_404_as_none:
                    return None
                if response.status >= 400:
                    raise create_runware_error(
                        "httpError",
                        f"Content service responded {response.status} for {url}",
                    )
                # `aiohttp` types this as Any — narrow to object since the
                # response is genuinely "some JSON value", and callers cast.
                parsed: object = await response.json()  # pyright: ignore[reportAny]
                return parsed
        except aiohttp.ClientError as error:
            raise create_runware_error(
                "connectionFailed",
                f"Failed to reach content service: {error}",
            ) from error
