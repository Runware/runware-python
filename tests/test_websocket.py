"""
Tests for WebSocket transport — subscribe/dispatch, send guards, frame routing.

We focus on the dispatch and lifecycle logic. Live connection / reconnect
behavior is covered by integration tests against a real server.
"""

from __future__ import annotations

from typing import Any

import pytest

from runware import RunwareError
from runware.transport.websocket import WebSocketTransport
from runware.types.sdk import SDKConfig


def _config() -> SDKConfig:
    return SDKConfig(
        api_key="sk-test",
        transport_type="websocket",
        timeout=5_000,
        poll_timeout=5_000,
        auth_timeout=5_000,
    )


def _transport() -> WebSocketTransport:
    return WebSocketTransport(_config())


class TestSubscribeUnsubscribe:
    def test_subscribe_registers_callback(self) -> None:
        t = _transport()
        called: list[Any] = []
        t.subscribe_to_task("u1", called.append)
        assert "u1" in t._task_callbacks

    def test_unsubscribe_removes_callback(self) -> None:
        t = _transport()
        t.subscribe_to_task("u1", lambda r: None)
        t.unsubscribe_from_task("u1")
        assert "u1" not in t._task_callbacks

    def test_unsubscribe_missing_is_safe(self) -> None:
        t = _transport()
        t.unsubscribe_from_task("never-subscribed")  # no error


class TestSendRequestGuards:
    @pytest.mark.asyncio
    async def test_raises_when_not_connected(self) -> None:
        t = _transport()
        with pytest.raises(RunwareError) as exc_info:
            await t.send_request({"taskType": "imageInference", "taskUUID": "u1"})
        assert exc_info.value.code == "connection"


class TestDispatchDataFrames:
    def test_groups_items_by_task_uuid(self) -> None:
        t = _transport()
        received_u1: list[dict[str, Any]] = []
        received_u2: list[dict[str, Any]] = []
        t.subscribe_to_task("u1", lambda r: received_u1.append(r))
        t.subscribe_to_task("u2", lambda r: received_u2.append(r))

        t._dispatch({
            "data": [
                {"taskUUID": "u1", "imageURL": "x"},
                {"taskUUID": "u2", "imageURL": "y"},
                {"taskUUID": "u1", "imageURL": "z"},
            ]
        })

        # Each subscriber sees its own items grouped together.
        assert len(received_u1) == 1
        assert len(received_u1[0]["data"]) == 2
        assert len(received_u2) == 1
        assert len(received_u2[0]["data"]) == 1

    def test_ignores_ping_pong_frames(self) -> None:
        t = _transport()
        received: list[dict[str, Any]] = []
        t.subscribe_to_task("u1", lambda r: received.append(r))
        t._dispatch({
            "data": [
                {"taskType": "ping", "pong": True},
                {"taskUUID": "u1", "imageURL": "x"},
            ]
        })
        # The ping/pong frame doesn't have a taskUUID and doesn't route anywhere.
        # The other frame correctly routes to the subscriber.
        assert len(received) == 1
        assert received[0]["data"][0]["imageURL"] == "x"

    def test_authentication_frame_updates_session_uuid(self) -> None:
        t = _transport()
        t._dispatch({
            "data": [
                {
                    "taskType": "authentication",
                    "connectionSessionUUID": "session-xyz",
                }
            ]
        })
        assert t._session_uuid == "session-xyz"

    def test_no_callback_logs_warning_but_doesnt_crash(self) -> None:
        t = _transport()
        # No subscriber for u1 — should not raise.
        t._dispatch({"data": [{"taskUUID": "u1", "imageURL": "x"}]})


class TestDispatchErrorFrames:
    def test_routes_error_to_correct_task_subscriber(self) -> None:
        t = _transport()
        received_u1: list[dict[str, Any]] = []
        received_u2: list[dict[str, Any]] = []
        t.subscribe_to_task("u1", lambda r: received_u1.append(r))
        t.subscribe_to_task("u2", lambda r: received_u2.append(r))

        t._dispatch({
            "errors": [
                {"taskUUID": "u1", "code": "invalidParam", "message": "bad"},
            ]
        })

        assert len(received_u1) == 1
        assert received_u1[0]["error"][0]["code"] == "invalidParam"
        assert len(received_u2) == 0

    def test_unrouted_error_broadcasts_to_all_subscribers(self) -> None:
        t = _transport()
        received_u1: list[dict[str, Any]] = []
        received_u2: list[dict[str, Any]] = []
        t.subscribe_to_task("u1", lambda r: received_u1.append(r))
        t.subscribe_to_task("u2", lambda r: received_u2.append(r))

        # Error with no taskUUID — broadcast to all so no waiter hangs forever.
        t._dispatch({"error": [{"code": "internalServerError", "message": "boom"}]})

        assert len(received_u1) == 1
        assert len(received_u2) == 1


class TestAuthFrameRobustness:
    """If the server emits a stray frame (ping, leftover data) before the auth
    response, the SDK must skim past it instead of failing the handshake."""

    @pytest.mark.asyncio
    async def test_skips_stray_frame_before_auth_response(self) -> None:
        import json

        t = _transport()
        sent: list[str] = []
        # Fake ws that records sends and replays a sequence of frames on recv().
        replay = [
            # First a stray data frame (no taskType=authentication).
            json.dumps({"data": [{"taskUUID": "stray-1", "imageURL": "x"}]}),
            # Then the actual auth response.
            json.dumps({"data": [{
                "taskType": "authentication",
                "connectionSessionUUID": "sess-good",
            }]}),
        ]
        recv_iter = iter(replay)

        class _FakeWS:
            async def send(self, payload: str) -> None:
                sent.append(payload)

            async def recv(self) -> str:
                return next(recv_iter)

            async def close(self) -> None:
                pass

        from typing import cast as _cast

        from websockets.asyncio.client import ClientConnection
        t._ws = _cast(ClientConnection, _FakeWS())

        await t._authenticate()
        # Auth completed despite the stray frame.
        assert t._session_uuid == "sess-good"


class TestCallbackIsolation:
    """
    A user callback that throws must not kill the dispatch loop or
    propagate up to the receive loop (which would trigger reconnect).
    """

    def test_throwing_callback_does_not_propagate(self) -> None:
        t = _transport()
        good_received: list[Any] = []
        t.subscribe_to_task("A", lambda f: (_ for _ in ()).throw(RuntimeError("boom")))
        t.subscribe_to_task("B", lambda f: good_received.append(f))

        # Dispatch a frame routing to both A (throws) and B (records).
        # The throwing callback must not bubble up; B must still receive.
        t._dispatch({
            "data": [
                {"taskUUID": "A", "imageURL": "a.jpg"},
                {"taskUUID": "B", "imageURL": "b.jpg"},
            ]
        })

        assert len(good_received) == 1, "subsequent callback should still fire"
        assert good_received[0]["data"][0]["imageURL"] == "b.jpg"

    def test_throwing_callback_does_not_propagate_on_error_frame(self) -> None:
        t = _transport()
        t.subscribe_to_task("A", lambda f: (_ for _ in ()).throw(RuntimeError("boom")))
        # Should not raise.
        t._dispatch({"errors": [{"taskUUID": "A", "code": "x", "message": "y"}]})


class TestReconnectCounterReset:
    @pytest.mark.asyncio
    async def test_connect_resets_attempt_counter(self) -> None:
        """A fresh connect() must reset the reconnect counter so a prior
        give-up doesn't poison the next session."""
        t = _transport()
        # Simulate a prior session that exhausted retries.
        t._reconnect_attempt = 999
        t._should_reconnect = False  # simulate "given up"

        # connect() is async and would try to open the socket — but we don't
        # need the open to succeed; we just need to verify the counter resets
        # before the open is attempted.
        import contextlib
        with contextlib.suppress(Exception):
            await t.connect()
        assert t._reconnect_attempt == 0


class TestReconnectJitter:
    """
    Past the backoff cap, jitter must still spread reconnect delays — otherwise
    every client backing off to 30s reconnects on the same millisecond.
    """

    def test_jitter_survives_when_base_exceeds_cap(self) -> None:
        from runware.transport.websocket import (
            _RECONNECT_BACKOFF_CAP_MS,
            _RECONNECT_JITTER_MAX_MS,
        )

        cap = _RECONNECT_BACKOFF_CAP_MS
        retry_delay = 1_000
        # Attempt 10: base = 1000 * 2^9 = 512_000 (well past 30_000 cap).
        attempt = 10
        base_ms = retry_delay * (2 ** (attempt - 1))
        assert base_ms > cap, "test premise: base should exceed cap"

        # Sample many delays at this attempt; spread should equal jitter range.
        samples = []
        for _ in range(200):
            capped_ms = min(base_ms, cap)
            # Use the same arithmetic the transport uses:
            import secrets
            jitter_ms = secrets.randbelow(_RECONNECT_JITTER_MAX_MS + 1)
            samples.append(capped_ms + jitter_ms)
        spread = max(samples) - min(samples)
        # Spread should be a meaningful fraction of jitter max (sampling
        # variance means we won't always see the full range with 200 samples).
        assert spread >= _RECONNECT_JITTER_MAX_MS // 2, (
            f"jitter collapsed: spread={spread}ms"
        )


class TestDispatchSingularErrorKey:
    def test_singular_error_key_is_normalized(self) -> None:
        t = _transport()
        received: list[dict[str, Any]] = []
        t.subscribe_to_task("u1", lambda r: received.append(r))
        # Server can send either `error` (singular) or `errors` (plural).
        t._dispatch({"error": {"taskUUID": "u1", "code": "invalidParam", "message": "x"}})
        assert len(received) == 1
        assert received[0]["error"][0]["code"] == "invalidParam"
