"""Tests for SSE parsing in runware/stream.py."""

from __future__ import annotations

import json

import pytest

from runware import RunwareError, parse_sse_line


class TestParseSseLine:
    def test_returns_none_for_blank(self) -> None:
        assert parse_sse_line("") is None
        assert parse_sse_line("   ") is None
        assert parse_sse_line("\n") is None

    def test_returns_none_for_comment(self) -> None:
        assert parse_sse_line(":heartbeat") is None
        assert parse_sse_line(": waiting") is None

    def test_returns_none_for_non_data_lines(self) -> None:
        assert parse_sse_line("event: message") is None
        assert parse_sse_line("id: 42") is None

    def test_returns_none_for_done_sentinel(self) -> None:
        assert parse_sse_line("data: [DONE]") is None
        assert parse_sse_line("data:[DONE]") is None

    def test_parses_text_delta(self) -> None:
        payload = json.dumps({"delta": {"text": "hello"}, "taskUUID": "u1"})
        chunk = parse_sse_line(f"data: {payload}")
        assert chunk is not None
        assert chunk.text == "hello"
        assert chunk.reasoning_content is None
        assert chunk.task_uuid == "u1"

    def test_parses_reasoning_delta(self) -> None:
        payload = json.dumps({"delta": {"reasoningContent": "thinking..."}})
        chunk = parse_sse_line(f"data: {payload}")
        assert chunk is not None
        assert chunk.reasoning_content == "thinking..."
        assert chunk.text is None

    def test_parses_finish_reason(self) -> None:
        payload = json.dumps({"delta": {}, "finishReason": "stop"})
        chunk = parse_sse_line(f"data: {payload}")
        assert chunk is not None
        assert chunk.finish_reason == "stop"

    def test_parses_usage_and_cost(self) -> None:
        payload = json.dumps(
            {
                "delta": {},
                "usage": {"totalTokens": 42, "promptTokens": 10},
                "cost": 0.0042,
            }
        )
        chunk = parse_sse_line(f"data: {payload}")
        assert chunk is not None
        assert chunk.usage == {"totalTokens": 42, "promptTokens": 10}
        assert chunk.cost == pytest.approx(0.0042)

    def test_raises_on_error_envelope_errors(self) -> None:
        payload = json.dumps(
            {"errors": [{"code": "invalidApiKey", "message": "no auth"}]}
        )
        with pytest.raises(RunwareError) as exc_info:
            parse_sse_line(f"data: {payload}")
        assert exc_info.value.code == "auth"

    def test_raises_on_error_envelope_error(self) -> None:
        payload = json.dumps(
            {"error": {"code": "rateLimitExceeded", "message": "slow down"}}
        )
        with pytest.raises(RunwareError) as exc_info:
            parse_sse_line(f"data: {payload}")
        assert exc_info.value.code == "rateLimit"

    def test_raises_runware_error_on_invalid_json(self) -> None:
        with pytest.raises(RunwareError) as exc_info:
            parse_sse_line("data: {not valid json}")
        assert exc_info.value.code == "unknown"  # parseError → maps to unknown

    def test_strips_whitespace_in_payload(self) -> None:
        payload = json.dumps({"delta": {"text": "x"}})
        chunk = parse_sse_line(f"data:    {payload}    ")
        assert chunk is not None
        assert chunk.text == "x"

    def test_returns_none_for_non_dict_json(self) -> None:
        assert parse_sse_line("data: 42") is None
        assert parse_sse_line('data: "string"') is None
        assert parse_sse_line("data: [1, 2, 3]") is None

    def test_result_index_preserved(self) -> None:
        payload = json.dumps({"delta": {"text": "x"}, "resultIndex": 2})
        chunk = parse_sse_line(f"data: {payload}")
        assert chunk is not None
        assert chunk.result_index == 2
