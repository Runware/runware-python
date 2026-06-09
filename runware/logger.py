"""
Logger module.

Each entry is a structured `{category, message, data, timestamp}` record — same
shape as the TS SDK so a sink written for one runs against the other unchanged.
`create_logger(enabled=False)` returns a noop logger: the SDK is silent unless
the user opts into `debug=True`.
"""

from __future__ import annotations

import json
import logging
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Literal

LogCategory = Literal[
    "connection",
    "auth",
    "heartbeat",
    "send",
    "receive",
    "request",
    "retry",
    "error",
    "warn",
    "info",
]


@dataclass
class LogEntry:
    """One structured log line emitted by the SDK."""

    category: LogCategory
    message: str
    timestamp: str
    data: object = None


LogSink = Callable[[LogEntry], None]


def _format_data(data: object) -> str:
    if data is None:
        return ""
    if isinstance(data, str):
        return data
    try:
        return json.dumps(data, indent=2, default=str)
    except (TypeError, ValueError):
        return "[unserializable]"


def _default_sink(entry: LogEntry) -> None:
    logger = logging.getLogger("runware")
    line = f"[RUNWARE] [{entry.category.upper()}] {entry.timestamp} {entry.message}"
    output = f"{line}\n{_format_data(entry.data)}" if entry.data is not None else line
    if entry.category == "error":
        logger.error(output)
    elif entry.category == "warn":
        logger.warning(output)
    else:
        logger.info(output)


class Logger:
    """Pluggable-sink logger. Construct via `create_logger`."""

    def __init__(self, enabled: bool, sink: LogSink) -> None:
        self._enabled: bool = enabled
        self._sink: LogSink = sink

    @property
    def enabled(self) -> bool:
        return self._enabled

    def _emit(self, category: LogCategory, message: str, data: object = None) -> None:
        if not self._enabled:
            return
        entry = LogEntry(
            category=category,
            message=message,
            timestamp=datetime.now(UTC).isoformat(),
            data=data,
        )
        self._sink(entry)

    def connection(self, message: str, data: object = None) -> None:
        self._emit("connection", message, data)

    def auth(self, message: str, data: object = None) -> None:
        self._emit("auth", message, data)

    def heartbeat(self, message: str, data: object = None) -> None:
        self._emit("heartbeat", message, data)

    def send(self, message: str, data: object = None) -> None:
        self._emit("send", message, data)

    def receive(self, message: str, data: object = None) -> None:
        self._emit("receive", message, data)

    def request(self, message: str, data: object = None) -> None:
        self._emit("request", message, data)

    def retry(self, message: str, data: object = None) -> None:
        self._emit("retry", message, data)

    def error(self, message: str, data: object = None) -> None:
        self._emit("error", message, data)

    def warn(self, message: str, data: object = None) -> None:
        self._emit("warn", message, data)

    def info(self, message: str, data: object = None) -> None:
        self._emit("info", message, data)


def create_logger(enabled: bool, sink: LogSink | None = None) -> Logger:
    """Construct a Logger. When `enabled=False`, all log calls drop silently."""
    return Logger(enabled=enabled, sink=sink if sink is not None else _default_sink)
