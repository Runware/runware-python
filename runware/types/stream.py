"""Stream payload types."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TextStreamChunk:
    """One chunk parsed from an SSE frame."""

    text: str | None = None
    reasoning_content: str | None = None
    finish_reason: str | None = None
    usage: dict[str, Any] | None = None
    cost: float | None = None
    result_index: int | None = None
    task_uuid: str | None = None


@dataclass
class TextStreamResult:
    """Final accumulated state of a text stream."""

    text: str = ""
    reasoning_content: str = ""
    finish_reason: str | None = None
    usage: dict[str, Any] | None = None
    cost: float | None = None
    task_uuid: str | None = None
    raw_chunks: list[TextStreamChunk] = field(
        default_factory=lambda: list[TextStreamChunk]()
    )
