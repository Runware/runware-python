"""
Tests for transport edge cases — WS reconnect plumbing, REST retry classification,
session ownership behavior.
"""

from __future__ import annotations

from typing import Any, cast

import aiohttp
import pytest

from runware import RuntimeDependencies, Runware, RunwareError
from runware.transport.rest import RestTransport, _is_retryable_status
from runware.transport.websocket import WebSocketTransport
from runware.types.sdk import SDKConfig

from ._mocks import MockSession


def _ws_config() -> SDKConfig:
    return SDKConfig(
        api_key="sk-test",
        transport_type="websocket",
        timeout=5_000,
        poll_timeout=5_000,
        auth_timeout=1_000,
    )


# ----------------------------------------------------------- REST retry classification


class TestIsRetryableStatus:
    @pytest.mark.parametrize("status,expected", [
        (200, False),
        (300, False),
        (400, False),
        (401, False),
        (404, False),
        (408, True),
        (429, True),
        (499, False),
        (500, True),
        (502, True),
        (503, True),
        (599, True),
        (600, False),
    ])
    def test_classification(self, status: int, expected: bool) -> None:
        assert _is_retryable_status(status) is expected


class TestRestRetryShouldRetry:
    def test_does_not_retry_aborted(self) -> None:
        err = RunwareError("aborted", "x")
        assert RestTransport._should_retry(err) is False

    def test_retries_on_timeout(self) -> None:
        assert RestTransport._should_retry(TimeoutError("timed out")) is True

    def test_retries_on_aiohttp_connection_error(self) -> None:
        assert (
            RestTransport._should_retry(aiohttp.ClientConnectionError("conn")) is True
        )

    def test_retries_on_aiohttp_payload_error(self) -> None:
        """Mid-body truncation / chunked-encoding errors should retry."""
        assert (
            RestTransport._should_retry(aiohttp.ClientPayloadError("truncated"))
            is True
        )

    def test_retries_on_retryable_http_status(self) -> None:
        err = RunwareError("serverError", "x")
        err.status_code = 503
        assert RestTransport._should_retry(err) is True

    def test_does_not_retry_non_retryable_status(self) -> None:
        err = RunwareError("validation", "x")
        err.status_code = 400
        assert RestTransport._should_retry(err) is False


# ----------------------------------------------------------- WebSocket lifecycle plumbing


class TestWebSocketLifecycle:
    def test_initial_state(self) -> None:
        t = WebSocketTransport(_ws_config())
        assert t.is_connected is False
        assert t.session_id is None
        assert t._ws is None
        assert t._receive_task is None
        assert t._heartbeat_task is None

    @pytest.mark.asyncio
    async def test_send_request_without_connect_raises_connection_error(self) -> None:
        t = WebSocketTransport(_ws_config())
        with pytest.raises(RunwareError) as exc_info:
            await t.send_request({"taskType": "imageInference", "taskUUID": "u1"})
        assert exc_info.value.code == "connection"

    def test_subscription_isolation(self) -> None:
        """Each task's subscriber only sees its own frames."""
        t = WebSocketTransport(_ws_config())
        received_a: list[dict[str, Any]] = []
        received_b: list[dict[str, Any]] = []
        t.subscribe_to_task("A", lambda r: received_a.append(cast(dict[str, Any], cast(object, r))))
        t.subscribe_to_task("B", lambda r: received_b.append(cast(dict[str, Any], cast(object, r))))
        t._dispatch({"data": [{"taskUUID": "A", "imageURL": "a"}]})
        t._dispatch({"data": [{"taskUUID": "B", "imageURL": "b"}]})
        assert len(received_a) == 1 and len(received_b) == 1
        assert received_a[0]["data"][0]["imageURL"] == "a"
        assert received_b[0]["data"][0]["imageURL"] == "b"


# ----------------------------------------------------------- Session ownership (DI)


class TestMalformedJsonResponse:
    """A 2xx response with a non-JSON body should surface a RunwareError, not
    leak the raw aiohttp exception type to user code."""

    @pytest.mark.asyncio
    async def test_2xx_non_json_body_raises_runware_error(self) -> None:
        from runware import RuntimeDependencies, Runware, RunwareError
        from tests._mocks import MockResponse

        # Payload is an instance of ValueError — MockSession will raise it
        # from .json() to simulate a malformed body.
        session = MockSession()
        session.add(
            "POST",
            "https://api.runware.ai/v1",
            MockResponse(status=200, payload=ValueError("not json")),
        )
        client = Runware(
            api_key="sk-test",
            transport_type="rest",
            dependencies=RuntimeDependencies(
                session=cast(aiohttp.ClientSession, cast(object, session))
            ),
        )
        try:
            with pytest.raises(RunwareError) as exc_info:
                await client.run({
                    "taskType": "imageInference",
                    "model": "civitai:1@1",
                    "positivePrompt": "x",
                    "width": 1024, "height": 1024,
                    "deliveryMethod": "sync",
                })
            # parseError maps to 'unknown' code via derive_code; what matters
            # is that it's a RunwareError, not aiohttp.ContentTypeError.
            assert exc_info.value.message
            assert "non-JSON body" in exc_info.value.message
        finally:
            await client.close()


class TestWsRedaction:
    def test_redact_only_authentication_tasks(self) -> None:
        from runware.transport.websocket import _redact

        out = _redact([
            {"taskType": "authentication", "apiKey": "sk-secret"},
            {"taskType": "imageInference", "apiKey": "should-not-redact"},
        ])
        # Authentication frames lose their key.
        assert '"sk-secret"' not in out
        assert "[redacted]" in out
        # Non-auth frames pass through unchanged (in case some user adds an
        # apiKey field for unrelated reasons).
        assert "should-not-redact" in out


class TestSessionOwnership:
    @pytest.mark.asyncio
    async def test_injected_session_is_not_closed(self) -> None:
        injected = MockSession()
        client = Runware(
            api_key="sk-test",
            transport_type="rest",
            dependencies=RuntimeDependencies(
                session=cast(aiohttp.ClientSession, cast(object, injected))
            ),
        )
        await client.close()
        # Injected session must survive a client.close() call.
        assert injected.closed is False

    @pytest.mark.asyncio
    async def test_owned_session_is_closed(self) -> None:
        # No DI → SDK creates and owns the session.
        client = Runware(api_key="sk-test", transport_type="rest")
        await client.connect()  # opens REST transport, lazily creates session
        rest = client._rest_transport
        assert rest is not None
        await client.close()
        # Owned session should be closed after client.close().
        assert rest._session is None or rest._session.closed


class TestWsConfigPropagation:
    def test_ws_transport_reads_log_from_config(self) -> None:
        cfg = _ws_config()
        t = WebSocketTransport(cfg)
        # Transport must share the config's log instance, not a new one.
        assert t._log is cfg.log

    def test_config_default_log_is_noop(self) -> None:
        cfg = _ws_config()
        assert cfg.log.enabled is False


class TestRestRetryShouldRetryEdgeCases:
    def test_does_not_retry_validation_error(self) -> None:
        err = RunwareError("validation", "x")
        assert RestTransport._should_retry(err) is False

    def test_does_not_retry_auth_error(self) -> None:
        err = RunwareError("auth", "x")
        err.status_code = 401
        assert RestTransport._should_retry(err) is False

    def test_does_not_retry_runtime_error_without_signal(self) -> None:
        # Bare RuntimeError (not a recognized retry condition) → no retry.
        assert RestTransport._should_retry(RuntimeError("???")) is False

    def test_retries_408_status(self) -> None:
        err = RunwareError("timeout", "x")
        err.status_code = 408
        assert RestTransport._should_retry(err) is True

    def test_retries_429_status(self) -> None:
        err = RunwareError("rateLimit", "x")
        err.status_code = 429
        assert RestTransport._should_retry(err) is True
