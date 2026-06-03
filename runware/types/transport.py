"""Transport protocols and shared request options."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass


@dataclass
class RequestOptions:
    """Per-call request overrides for transports."""

    timeout: int | None = None
    cancel_event: asyncio.Event | None = None
