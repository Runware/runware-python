"""Configuration and call-option types."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    import aiohttp
    from websockets.asyncio.client import ClientConnection

from ..logger import Logger, LogSink, create_logger

TransportType = Literal["websocket", "rest"]
RetryStrategy = Literal["linear", "exponential"]

WebSocketConnectFactory = Callable[[str], Awaitable["ClientConnection"]]

# Loose wire-task / response-item shape: keys are arbitrary, values are
# per-taskType (the schema-derived TypedDicts under types/task_map.py narrow
# them at the public API boundary). Equivalent of TS's `Record<string, any>`
# at request/response boundaries — the single point that opts out of the
# explicit-Any rule, used as the alias everywhere a loose payload is plumbed.
# Note: not declared with `TypeAlias` — that form is nominal in pyright and
# breaks TypedDict-overload subtyping. The implicit alias form preserves the
# structural `dict[str, Any]` shape the overloads need to be subtypes of.
LoosePayload = dict[str, Any]  # pyright: ignore[reportExplicitAny]


@dataclass
class RuntimeDependencies:
    """
    Inject custom runtime dependencies.

    - `session`: a pre-configured `aiohttp.ClientSession` reused for REST
      transport, validation `/resolve` calls, registry fetches, and SSE
      streaming. If you provide one, the SDK won't close it on shutdown — you
      own its lifecycle. If omitted, the SDK manages its own.
    - `ws_connect`: a callable that opens a WebSocket. Defaults to
      `websockets.connect`. Override for custom subprotocols, headers, or
      proxy settings.
    """

    session: aiohttp.ClientSession | None = None
    ws_connect: WebSocketConnectFactory | None = None


@dataclass
class SDKConfig:
    """SDK configuration. Construct via `create_config()`."""

    api_key: str
    transport: TransportType = "websocket"
    ws_base_url: str = "wss://ws-api.runware.ai/v1"
    http_base_url: str = "https://api.runware.ai/v1"

    timeout: int = 1_200_000
    poll_timeout: int = 1_200_000
    auth_timeout: int = 15_000

    max_retries: int = 3
    retry_delay: int = 1_000
    retry_strategy: RetryStrategy = "exponential"
    max_reconnect_attempts: float = float("inf")

    debug: bool = False
    validate: bool = False

    dependencies: RuntimeDependencies | None = None
    log_sink: LogSink | None = None
    # Populated by create_config. Transports read it via `config.log`.
    # The default factory yields a noop logger so users who construct an
    # SDKConfig directly (tests, advanced setups) still get a working object.
    log: Logger = field(
        init=False, default_factory=lambda: create_logger(False)
    )


@dataclass
class RunOptions:
    """Per-call options for `client.run()`."""

    on_result: Callable[[LoosePayload], None] | None = None
    on_progress: Callable[[LoosePayload], None] | None = None
    timeout: int | None = None
    cancel_event: asyncio.Event | None = None
    validate: bool | None = None


@dataclass
class StreamOptions:
    """Per-call options for `client.stream()`."""

    timeout: int | None = None
    cancel_event: asyncio.Event | None = None
    validate: bool | None = None


@dataclass
class TaskPayload:
    """Internal representation of a single task on the wire."""

    task_type: str
    task_uuid: str
    extra: LoosePayload = field(default_factory=lambda: LoosePayload())

    def to_wire(self) -> LoosePayload:
        """Serialize to the camelCase shape the API expects."""
        return {"taskType": self.task_type, "taskUUID": self.task_uuid, **self.extra}
