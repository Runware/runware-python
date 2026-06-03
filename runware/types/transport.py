"""Transport protocols and shared request options."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import TypedDict


@dataclass
class RequestOptions:
    """Per-call request overrides for transports."""

    timeout: int | None = None
    cancel_event: asyncio.Event | None = None


class WireFrame(TypedDict, total=False):
    """
    Server response envelope as seen on the wire by both REST and WS transports.

    `data` carries successful task items; `errors` carries failures. Both keys
    are optional — a response may include either, both, or (rarely) neither.
    Pre-stream HTTP error responses use the singular `error` shape instead.
    Items inside are themselves loose dicts: the server's per-taskType schemas
    drive their shape, narrowed downstream against the generated Result types.
    """

    data: list[dict[str, object]]
    errors: list[dict[str, object]]
    error: dict[str, object] | list[dict[str, object]]
