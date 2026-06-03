"""
Model registry.

Fetches `/registry.json` from the schemas service with a 5-minute TTL and
conditional GET (ETag). When the network is unreachable, falls back to a
bundled snapshot so the SDK stays usable offline. Mirrors the TS registry's
contract.

Lifecycle parity with TS:
  - Initial fetch is bounded by a 3s timeout race; if the server is slow the
    SDK falls through to bundled data on the first lookup.
  - TTL refresh runs in the background: lookups always return the cached value
    immediately, the refresh fires fire-and-forget.
  - `notify_version(v)` triggers a background refresh when the SDK sees a
    fresh version from the API (e.g. a response header).
  - `resolve_model_air(input)` accepts either an AIR (`runware:101@1`) or a
    curated-model slug (`flux-1-dev`) and returns the canonical AIR.
"""

from __future__ import annotations

import asyncio
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from typing import Any, cast

import aiohttp

from .logger import Logger

_DEFAULT_TTL_SECONDS = 5 * 60
_DEFAULT_INITIAL_FETCH_TIMEOUT_SECONDS = 3.0


@dataclass
class RegistryModelEntry:
    task_type: str
    id: str


@dataclass
class RegistryData:
    """Parsed registry payload."""

    models: dict[str, RegistryModelEntry] = field(
        default_factory=lambda: dict[str, RegistryModelEntry]()
    )
    architecture_task_types: dict[str, str] = field(
        default_factory=lambda: dict[str, str]()
    )
    modality_task_types: dict[str, str] = field(
        default_factory=lambda: dict[str, str]()
    )
    version: str | None = None


@dataclass
class _CacheEntry:
    data: RegistryData
    expires_at: float
    etag: str | None


class Registry:
    """Async model registry with TTL + ETag + offline fallback."""

    def __init__(
        self,
        *,
        url: str,
        log: Logger,
        fallback: RegistryData | None = None,
        ttl_seconds: float = _DEFAULT_TTL_SECONDS,
        initial_fetch_timeout_seconds: float = _DEFAULT_INITIAL_FETCH_TIMEOUT_SECONDS,
        session: aiohttp.ClientSession | None = None,
    ) -> None:
        self._url = url
        self._log = log
        self._fallback = fallback if fallback is not None else RegistryData()
        self._ttl_seconds = ttl_seconds
        self._initial_fetch_timeout_seconds = initial_fetch_timeout_seconds
        self._session = session
        self._owned_session = session is None
        self._cache: _CacheEntry | None = None
        self._initial_fetch_attempted = False
        self._in_flight_fetch: asyncio.Task[tuple[RegistryData, str | None] | None] | None = None
        self._background_tasks: set[asyncio.Task[Any]] = set()
        # Slug → AIR index, lazily built from fallback + current cache.
        self._slug_to_air: dict[str, str] | None = None
        self._slug_index_source: RegistryData | None = None

    async def close(self) -> None:
        for task in list(self._background_tasks):
            task.cancel()
        self._background_tasks.clear()
        if self._owned_session and self._session is not None:
            await self._session.close()
            self._session = None

    async def _ensure_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
            self._owned_session = True
        return self._session

    # ----------------------------------------------------------- public API

    async def refresh(self) -> None:
        """
        Force a fresh fetch, bypassing TTL.

        If the fetch fails, the existing cache is kept so consumers still see
        the last known data. Re-raises only if no cache exists and the fallback
        couldn't be parsed.
        """
        self._initial_fetch_attempted = True
        result = await self._fetch_remote()
        if result is not None:
            data, etag = result
            self._cache = _CacheEntry(
                data=data,
                expires_at=time.monotonic() + self._ttl_seconds,
                etag=etag,
            )
            self._invalidate_slug_index()

    async def get_model_task_type(self, model: str) -> str | None:
        entry = await self._lookup_model(model)
        return entry.task_type if entry else None

    async def get_model_id(self, model: str) -> str | None:
        entry = await self._lookup_model(model)
        return entry.id if entry else None

    async def get_architecture_task_type(self, key: str) -> str | None:
        data = await self._ensure_fresh()
        if data.architecture_task_types.get(key):
            return data.architecture_task_types[key]
        return self._fallback.architecture_task_types.get(key)

    async def get_modality_task_type(self, key: str) -> str | None:
        data = await self._ensure_fresh()
        if data.modality_task_types.get(key):
            return data.modality_task_types[key]
        return self._fallback.modality_task_types.get(key)

    async def resolve_model_air(self, model: str) -> str | None:
        """
        Resolve a model identifier to its canonical AIR.

        Accepts either an AIR (e.g. `runware:101@1`) or a curated-model slug
        (e.g. `flux-1-dev`). Returns None for unknown identifiers.
        """
        data = await self._ensure_fresh()
        if model in data.models or model in self._fallback.models:
            return model
        return self._slug_index(data).get(model)

    def get_version(self) -> str | None:
        return self._cache.data.version if self._cache else None

    def notify_version(self, version: str) -> None:
        """
        Trigger a background refresh if the supplied version differs from
        what's cached. Used when the SDK observes a fresh version on an API
        response (e.g. a header) and wants to pick up new models without
        blocking the active request.
        """
        if self._cache is not None and self._cache.data.version == version:
            return
        self._log.info(f"Observed new registry version {version}, refreshing")
        self._spawn_background_refresh()

    # ----------------------------------------------------------- internal

    async def _lookup_model(self, model: str) -> RegistryModelEntry | None:
        air = await self.resolve_model_air(model)
        if air is None:
            return None
        data = await self._ensure_fresh()
        return data.models.get(air) or self._fallback.models.get(air)

    async def _ensure_fresh(self) -> RegistryData:
        if not self._initial_fetch_attempted:
            await self._initial_fetch()

        now = time.monotonic()
        if self._cache is not None and self._cache.expires_at > now:
            return self._cache.data

        # Either no cache, or TTL elapsed: kick off a background refresh and
        # return whatever we have. Matches TS's `refreshSilently()` path.
        self._spawn_background_refresh()

        if self._cache is not None:
            return self._cache.data
        return self._fallback

    async def _initial_fetch(self) -> None:
        self._initial_fetch_attempted = True

        async def attempt() -> tuple[RegistryData, str | None] | None:
            try:
                return await self._fetch_remote()
            except Exception as exc:
                self._log.warn(f"Initial registry fetch failed, using fallback: {exc}")
                return None

        try:
            result = await asyncio.wait_for(
                attempt(), timeout=self._initial_fetch_timeout_seconds
            )
        except TimeoutError:
            self._log.warn(
                f"Registry fetch timed out after "
                f"{int(self._initial_fetch_timeout_seconds * 1000)}ms, using fallback"
            )
            return

        if result is not None:
            data, etag = result
            self._cache = _CacheEntry(
                data=data,
                expires_at=time.monotonic() + self._ttl_seconds,
                etag=etag,
            )
            self._invalidate_slug_index()

    def _spawn_background_refresh(self) -> None:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            return

        async def background() -> None:
            try:
                result = await self._fetch_remote()
            except Exception as exc:
                self._log.warn(f"Background registry refresh failed: {exc}")
                return
            if result is None:
                return
            data, etag = result
            self._cache = _CacheEntry(
                data=data,
                expires_at=time.monotonic() + self._ttl_seconds,
                etag=etag,
            )
            self._invalidate_slug_index()

        task = loop.create_task(background())
        self._background_tasks.add(task)
        task.add_done_callback(self._background_tasks.discard)

    async def _fetch_remote(self) -> tuple[RegistryData, str | None] | None:
        """Fetch from the URL. Returns (data, etag) on success, None on failure."""
        if self._in_flight_fetch is not None and not self._in_flight_fetch.done():
            return await self._in_flight_fetch

        loop = asyncio.get_running_loop()
        self._in_flight_fetch = loop.create_task(self._do_fetch())
        try:
            return await self._in_flight_fetch
        finally:
            self._in_flight_fetch = None

    async def _do_fetch(self) -> tuple[RegistryData, str | None] | None:
        session = await self._ensure_session()
        headers: dict[str, str] = {}
        if self._cache is not None and self._cache.etag is not None:
            headers["If-None-Match"] = self._cache.etag

        try:
            async with session.get(self._url, headers=headers) as response:
                if response.status == 304 and self._cache is not None:
                    return self._cache.data, self._cache.etag
                if not response.ok:
                    self._log.warn(
                        f"Registry fetch failed: HTTP {response.status}",
                        {"url": self._url},
                    )
                    return None
                payload = cast(dict[str, Any], await response.json())
                etag = response.headers.get("ETag")
                data = _parse_registry(payload)
                self._log.info(f"Registry refreshed (version {data.version})")
                return data, etag
        except aiohttp.ClientError as exc:
            self._log.warn(f"Registry fetch error: {exc}", {"url": self._url})
            return None

    def _slug_index(self, current: RegistryData) -> dict[str, str]:
        if self._slug_to_air is not None and self._slug_index_source is current:
            return self._slug_to_air
        index: dict[str, str] = {}
        for air, entry in self._fallback.models.items():
            if entry.id:
                index[entry.id] = air
        for air, entry in current.models.items():
            if entry.id:
                index[entry.id] = air
        self._slug_to_air = index
        self._slug_index_source = current
        return index

    def _invalidate_slug_index(self) -> None:
        self._slug_to_air = None
        self._slug_index_source = None


def _parse_registry(payload: dict[str, Any]) -> RegistryData:
    models_raw = cast(dict[str, Any], payload.get("models") or {})
    arch_raw = cast(dict[str, Any], payload.get("architectureTaskTypes") or {})
    modality_raw = cast(dict[str, Any], payload.get("modalityTaskTypes") or {})

    models: dict[str, RegistryModelEntry] = {}
    for air, entry in models_raw.items():
        if not isinstance(entry, dict):
            continue
        entry_dict = cast(dict[str, Any], entry)
        task_type = entry_dict.get("taskType")
        ident = entry_dict.get("id")
        if isinstance(task_type, str) and isinstance(ident, str):
            models[air] = RegistryModelEntry(task_type=task_type, id=ident)

    architecture: dict[str, str] = {
        k: v for k, v in arch_raw.items() if isinstance(v, str)
    }
    modality: dict[str, str] = {
        k: v for k, v in modality_raw.items() if isinstance(v, str)
    }

    version = payload.get("version")
    return RegistryData(
        models=models,
        architecture_task_types=architecture,
        modality_task_types=modality,
        version=version if isinstance(version, str) else None,
    )


def create_registry(
    *,
    url: str,
    log: Logger,
    fallback: RegistryData | None = None,
    ttl_seconds: float = _DEFAULT_TTL_SECONDS,
    initial_fetch_timeout_seconds: float = _DEFAULT_INITIAL_FETCH_TIMEOUT_SECONDS,
    session: aiohttp.ClientSession | None = None,
) -> Registry:
    return Registry(
        url=url,
        log=log,
        fallback=fallback,
        ttl_seconds=ttl_seconds,
        initial_fetch_timeout_seconds=initial_fetch_timeout_seconds,
        session=session,
    )


# Type alias kept for external callers building plumbing around the registry.
RegistryFetcher = Callable[[], Awaitable[tuple[RegistryData, str | None] | None]]
