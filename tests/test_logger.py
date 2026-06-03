"""Tests for runware/logger.py — entry shape, noop-when-disabled, channels."""

from __future__ import annotations

import logging

import pytest

from runware import LogCategory, LogEntry, Logger, create_logger


class TestLogEntry:
    def test_required_fields(self) -> None:
        entry = LogEntry(
            category="info", message="hi", timestamp="2026-01-01T00:00:00+00:00"
        )
        assert entry.category == "info"
        assert entry.message == "hi"
        assert entry.timestamp == "2026-01-01T00:00:00+00:00"
        assert entry.data is None

    def test_carries_arbitrary_data(self) -> None:
        entry = LogEntry(
            category="warn",
            message="x",
            timestamp="2026-01-01T00:00:00+00:00",
            data={"k": 1, "y": "z"},
        )
        assert entry.data == {"k": 1, "y": "z"}


class TestCreateLogger:
    def test_returns_logger_instance(self) -> None:
        assert isinstance(create_logger(False), Logger)

    def test_default_sink_uses_stdlib_logging(
        self, caplog: pytest.LogCaptureFixture
    ) -> None:
        log = create_logger(True)
        with caplog.at_level(logging.INFO, logger="runware"):
            log.info("hello info")
            log.warn("hello warn")
        joined = " | ".join(r.message for r in caplog.records)
        assert "hello info" in joined
        assert "hello warn" in joined


class TestNoopWhenDisabled:
    def test_no_calls_when_disabled(self) -> None:
        captured: list[LogEntry] = []
        log = create_logger(False, sink=captured.append)
        log.info("i")
        log.warn("w")
        log.error("e")
        log.connection("c")
        log.heartbeat("h")
        assert captured == []

    def test_all_calls_when_enabled(self) -> None:
        captured: list[LogEntry] = []
        log = create_logger(True, sink=captured.append)
        log.info("i")
        log.warn("w")
        log.error("e")
        assert [e.category for e in captured] == ["info", "warn", "error"]


class TestEntryShape:
    def test_timestamp_is_iso_format(self) -> None:
        captured: list[LogEntry] = []
        log = create_logger(True, sink=captured.append)
        log.info("hi")
        assert captured[0].timestamp
        # ISO 8601 with timezone offset always contains 'T' between date and time.
        assert "T" in captured[0].timestamp

    def test_data_attaches_to_entry(self) -> None:
        captured: list[LogEntry] = []
        log = create_logger(True, sink=captured.append)
        log.error("boom", {"url": "https://x", "code": 500})
        assert len(captured) == 1
        assert captured[0].data == {"url": "https://x", "code": 500}


class TestChannels:
    @pytest.mark.parametrize(
        "method,expected",
        [
            ("connection", "connection"),
            ("auth", "auth"),
            ("heartbeat", "heartbeat"),
            ("send", "send"),
            ("receive", "receive"),
            ("request", "request"),
            ("retry", "retry"),
            ("error", "error"),
            ("warn", "warn"),
            ("info", "info"),
        ],
    )
    def test_channel_sets_category(
        self, method: str, expected: LogCategory
    ) -> None:
        captured: list[LogEntry] = []
        log = create_logger(True, sink=captured.append)
        getattr(log, method)("payload")
        assert len(captured) == 1
        assert captured[0].category == expected
