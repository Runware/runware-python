"""
Manual mocks for aiohttp.ClientSession.

`aioresponses` is incompatible with aiohttp 3.10+ (stream_writer kwarg), so we
mock at the session level directly. Each test instantiates a MockSession with
a queue of MockResponse objects per (method, url) pair.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any


@dataclass
class MockResponse:
    """Single mocked response for an aiohttp request."""

    status: int = 200
    payload: Any = None
    headers: dict[str, str] = field(default_factory=lambda: dict[str, str]())
    exception: BaseException | None = None

    @property
    def ok(self) -> bool:
        return 200 <= self.status < 400

    @property
    def reason(self) -> str:
        return "OK" if self.ok else "ERROR"

    @property
    def content(self) -> Any:
        # Some callers iterate `response.content.iter_any()` for streaming.
        raise NotImplementedError(
            "MockResponse.content not implemented; use a richer fixture for stream tests."
        )

    async def __aenter__(self) -> MockResponse:
        if self.exception is not None:
            raise self.exception
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        return None

    async def json(self) -> Any:
        if isinstance(self.payload, BaseException):
            raise self.payload
        return self.payload

    async def text(self) -> str:
        if self.payload is None:
            return ""
        return json.dumps(self.payload)


@dataclass
class RequestLog:
    """One recorded request."""

    method: str
    url: str
    headers: dict[str, str]
    json_body: Any


class MockSession:
    """
    Minimal aiohttp.ClientSession stand-in.

    Pre-load with `add(method, url, response)` (queue of responses per key).
    Each `.get()` / `.post()` returns the next response in the queue, or raises
    if none registered. Closed sessions are tracked via `.closed`.
    """

    def __init__(self) -> None:
        self._queues: dict[tuple[str, str], list[MockResponse]] = {}
        self.closed = False
        self.request_log: list[RequestLog] = []

    def add(self, method: str, url: str, response: MockResponse) -> None:
        key = (method.upper(), url)
        self._queues.setdefault(key, []).append(response)

    def get(self, url: str, **kwargs: Any) -> MockResponse:
        return self._take("GET", url, **kwargs)

    def post(self, url: str, **kwargs: Any) -> MockResponse:
        return self._take("POST", url, **kwargs)

    def _take(self, method: str, url: str, **kwargs: Any) -> MockResponse:
        self.request_log.append(
            RequestLog(
                method=method,
                url=url,
                headers=dict(kwargs.get("headers") or {}),
                json_body=kwargs.get("json"),
            )
        )
        key = (method, url)
        queue = self._queues.get(key, [])
        if not queue:
            raise AssertionError(f"No mock response registered for {method} {url}")
        # Pop one unless it's the last and marked repeat=True (not used here).
        if len(queue) > 1:
            return queue.pop(0)
        return queue[0]

    async def close(self) -> None:
        self.closed = True

    def count(self, method: str, url: str) -> int:
        """How many times `method url` was called."""
        return sum(
            1 for r in self.request_log if r.method == method.upper() and r.url == url
        )
