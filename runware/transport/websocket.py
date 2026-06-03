"""
WebSocket transport.

Long-lived connection, per-task subscription dispatch, heartbeat, and
auto-reconnect with session resume. Mirrors the TS WebSocket transport's
behavior, ported to asyncio idioms.

Lifecycle:
  - `connect()` opens the socket and authenticates. Spins up a background
    receive task that dispatches incoming frames to per-taskUUID callbacks.
  - `send_request()` writes a JSON-encoded task batch to the open socket.
  - `subscribe_to_task(uuid, cb)` registers a callback fired for every frame
    that mentions that taskUUID. `unsubscribe_from_task(uuid)` removes it.
  - `disconnect()` stops reconnect attempts and closes the socket cleanly.
"""

from __future__ import annotations

import asyncio
import contextlib
import json
import secrets
import time
from collections.abc import Callable
from typing import Any, cast

import websockets
from websockets.asyncio.client import ClientConnection
from websockets.exceptions import ConnectionClosed

from ..errors import create_runware_error
from ..types.sdk import SDKConfig

WsResponse = dict[str, Any]
ResponseCallback = Callable[[WsResponse], None]

_HEARTBEAT_INTERVAL_SECONDS = 30.0
_HEARTBEAT_INACTIVITY_THRESHOLD_MS = 100_000
_RECONNECT_BACKOFF_CAP_MS = 30_000
_RECONNECT_JITTER_MAX_MS = 1_000


class WebSocketTransport:
    """Async WebSocket transport with auto-reconnect and per-task dispatch."""

    type: str = "websocket"

    def __init__(self, config: SDKConfig) -> None:
        self._config = config
        self._log = config.log
        self._ws: ClientConnection | None = None
        self._receive_task: asyncio.Task[None] | None = None
        self._heartbeat_task: asyncio.Task[None] | None = None
        self._background_tasks: set[asyncio.Task[None]] = set()
        self._task_callbacks: dict[str, ResponseCallback] = {}
        self._connected = False
        self._should_reconnect = False
        self._is_reconnecting = False
        self._reconnect_attempt = 0
        self._session_uuid: str | None = None
        self._last_activity_ms: float = time.monotonic() * 1000
        self._connect_lock = asyncio.Lock()

    @property
    def is_connected(self) -> bool:
        return self._connected

    @property
    def session_id(self) -> str | None:
        return self._session_uuid

    async def connect(self) -> None:
        """Open the WebSocket and authenticate."""
        async with self._connect_lock:
            self._should_reconnect = True
            # Reset the reconnect counter so a fresh connect() after a prior
            # give-up doesn't start already over the limit.
            self._reconnect_attempt = 0
            await self._open_once()

    async def disconnect(self) -> None:
        """Close the socket and stop reconnect attempts."""
        self._should_reconnect = False
        for cb in list(self._task_callbacks.values()):
            try:
                cb({"error": [{"code": "disconnected", "message": "Client disconnected"}]})
            except Exception as exc:
                self._log.error(f"task callback raised during disconnect: {exc}")
        self._task_callbacks.clear()
        await self._teardown_socket()

    async def send_request(
        self,
        data: dict[str, Any] | list[dict[str, Any]],
    ) -> None:
        if not self._connected or self._ws is None:
            raise create_runware_error("notConnected", "Not connected to WebSocket server")
        payload = data if isinstance(data, list) else [data]
        serialized = json.dumps(payload)
        self._log.send(_redact(payload))
        try:
            await self._ws.send(serialized)
        except (ConnectionClosed, OSError) as exc:
            raise create_runware_error(
                "sendFailed",
                f"Failed to send WebSocket message: {exc}",
            ) from exc

    def subscribe_to_task(self, task_uuid: str, callback: ResponseCallback) -> None:
        self._task_callbacks[task_uuid] = callback

    def unsubscribe_from_task(self, task_uuid: str) -> None:
        self._task_callbacks.pop(task_uuid, None)

    async def _open_once(self) -> None:
        await self._teardown_socket(close_socket=True)

        connect_factory = (
            self._config.dependencies.ws_connect
            if self._config.dependencies and self._config.dependencies.ws_connect
            else websockets.connect
        )
        try:
            self._ws = await connect_factory(self._config.ws_base_url)
        except (OSError, websockets.InvalidURI, websockets.InvalidHandshake) as exc:
            raise create_runware_error(
                "connectionFailed",
                f"WebSocket connection failed: {exc}",
            ) from exc

        self._connected = True
        self._last_activity_ms = time.monotonic() * 1000

        try:
            await self._authenticate()
        except BaseException:
            await self._teardown_socket(close_socket=True)
            raise

        self._receive_task = asyncio.create_task(self._receive_loop())
        self._heartbeat_task = asyncio.create_task(self._heartbeat_loop())

    async def _authenticate(self) -> None:
        if self._ws is None:
            raise create_runware_error("notOpen", "WebSocket not open for authentication")

        auth_message: dict[str, Any] = {
            "taskType": "authentication",
            "apiKey": self._config.api_key,
        }
        if self._session_uuid:
            auth_message["connectionSessionUUID"] = self._session_uuid

        self._log.auth(
            json.dumps(
                [{**auth_message, "apiKey": "[redacted]"}],
            )
        )
        await self._ws.send(json.dumps([auth_message]))

        # Read frames until we see the authentication response (or an error).
        # The server might emit a stray ping or unrelated data frame before
        # the auth reply; we skip those rather than failing the handshake.
        # The total budget is `auth_timeout` across however many frames we
        # have to skim.
        timeout_seconds = self._config.auth_timeout / 1000.0
        deadline = asyncio.get_running_loop().time() + timeout_seconds
        data: dict[str, Any] | None = None
        while True:
            remaining = deadline - asyncio.get_running_loop().time()
            if remaining <= 0:
                raise create_runware_error(
                    "authTimeout",
                    (
                        f"Authentication timed out after "
                        f"{self._config.auth_timeout}ms"
                    ),
                )
            try:
                raw = await asyncio.wait_for(self._ws.recv(), timeout=remaining)
            except TimeoutError as exc:
                raise create_runware_error(
                    "authTimeout",
                    (
                        f"Authentication timed out after "
                        f"{self._config.auth_timeout}ms"
                    ),
                ) from exc
            except ConnectionClosed as exc:
                raise create_runware_error(
                    "connectionFailed",
                    f"WebSocket closed during authentication: {exc}",
                ) from exc

            frame = _parse_frame(raw)
            if frame is None:
                # Unparseable bytes — skip and keep waiting.
                self._log.warn("Skipping unparseable frame during authentication")
                continue

            raw_errors = frame.get("errors") or frame.get("error")
            if raw_errors:
                errs: list[Any] = (
                    cast(list[Any], raw_errors)
                    if isinstance(raw_errors, list)
                    else [raw_errors]
                )
                first_err: dict[str, Any] = {}
                if errs and isinstance(errs[0], dict):
                    first_err = cast(dict[str, Any], errs[0])
                raise create_runware_error(
                    "authFailed",
                    first_err.get("message")
                    or "Authentication failed via API response",
                )

            items_raw = frame.get("data")
            items: list[Any] = (
                cast(list[Any], items_raw)
                if isinstance(items_raw, list)
                else []
            )
            # Skim past anything that isn't the auth response — pings,
            # stale frames, etc.
            found = False
            for item in items:
                if not isinstance(item, dict):
                    continue
                if cast(dict[str, Any], item).get("taskType") == "authentication":
                    data = frame
                    found = True
                    break
            if found:
                break
            # Not the auth frame — keep waiting.
            self._log.warn("Skipping non-auth frame during authentication handshake")

        assert data is not None  # loop only exits when data is set
        items_raw = data.get("data")
        items = (
            cast(list[Any], items_raw) if isinstance(items_raw, list) else []
        )
        first: dict[str, Any] | None = None
        for candidate in items:
            if not isinstance(candidate, dict):
                continue
            candidate_dict = cast(dict[str, Any], candidate)
            if candidate_dict.get("taskType") == "authentication":
                first = candidate_dict
                break
        if first is None:
            raise create_runware_error(
                "authFailed",
                "Authentication response did not include an authentication frame",
            )

        session_uuid = first.get("connectionSessionUUID")
        if not isinstance(session_uuid, str):
            raise create_runware_error(
                "authFailed",
                "Authentication successful but missing connectionSessionUUID",
            )
        self._session_uuid = session_uuid

    async def _receive_loop(self) -> None:
        ws = self._ws
        if ws is None:
            return
        try:
            async for raw in ws:
                self._last_activity_ms = time.monotonic() * 1000
                self._log.receive(raw if isinstance(raw, str) else raw.decode())
                frame = _parse_frame(raw)
                if frame is None:
                    self._log.warn("Failed to parse WebSocket frame")
                    continue
                self._dispatch(frame)
        except ConnectionClosed:
            pass
        except Exception as exc:
            self._log.error(f"WebSocket receive loop error: {exc}")
        finally:
            self._connected = False
            if self._should_reconnect:
                self._spawn_background(self._reconnect())

    def _safe_call(self, cb: ResponseCallback, frame: WsResponse) -> None:
        """
        Invoke a per-task callback while shielding the receive loop from any
        exception it raises. A throwing user callback must not kill the
        dispatch loop or trigger an unintended reconnect.
        """
        try:
            cb(frame)
        except Exception as exc:
            self._log.error(f"task callback raised in dispatch: {exc}")

    def _dispatch(self, frame: dict[str, Any]) -> None:
        raw_errors = frame.get("errors") or frame.get("error")
        if raw_errors:
            errors_list: list[dict[str, Any]] = (
                cast(list[dict[str, Any]], raw_errors)
                if isinstance(raw_errors, list)
                else [cast(dict[str, Any], raw_errors)]
            )
            by_task: dict[str, list[dict[str, Any]]] = {}
            unrouted: list[dict[str, Any]] = []
            for err in errors_list:
                task_uuid = err.get("taskUUID")
                if isinstance(task_uuid, str):
                    by_task.setdefault(task_uuid, []).append(err)
                else:
                    unrouted.append(err)
            delivered = False
            for task_uuid, errs in by_task.items():
                cb = self._task_callbacks.get(task_uuid)
                if cb is not None:
                    delivered = True
                    self._safe_call(cb, {"error": errs})
            if unrouted or not delivered:
                self._log.error("Unroutable WebSocket error", errors_list)
                for cb in self._task_callbacks.values():
                    self._safe_call(cb, {"error": errors_list})
            return

        data = frame.get("data")
        if not isinstance(data, list):
            return

        items_by_task: dict[str, list[dict[str, Any]]] = {}
        for item in cast(list[Any], data):
            if not isinstance(item, dict):
                continue
            item_dict = cast(dict[str, Any], item)
            task_type = item_dict.get("taskType")
            if task_type == "ping" and item_dict.get("pong") is True:
                continue
            if task_type == "authentication":
                session_uuid = item_dict.get("connectionSessionUUID")
                if isinstance(session_uuid, str):
                    self._session_uuid = session_uuid
                continue
            task_uuid = item_dict.get("taskUUID")
            if isinstance(task_uuid, str):
                items_by_task.setdefault(task_uuid, []).append(item_dict)

        for task_uuid, items in items_by_task.items():
            cb = self._task_callbacks.get(task_uuid)
            if cb is not None:
                self._safe_call(cb, {"data": items})
            else:
                self._log.warn(f"No callback for taskUUID: {task_uuid}")

    async def _heartbeat_loop(self) -> None:
        try:
            while self._connected and self._ws is not None:
                await asyncio.sleep(_HEARTBEAT_INTERVAL_SECONDS)
                ws = cast("ClientConnection | None", self._ws)
                if not self._connected or ws is None:
                    return
                try:
                    await ws.send(json.dumps([{"taskType": "ping", "ping": True}]))
                except (ConnectionClosed, OSError) as exc:
                    self._log.heartbeat(f"Ping failed, reconnecting: {exc}")
                    self._spawn_background(self._reconnect())
                    return

                inactivity_ms = time.monotonic() * 1000 - self._last_activity_ms
                if inactivity_ms > _HEARTBEAT_INACTIVITY_THRESHOLD_MS:
                    self._log.heartbeat(
                        f"No activity for {inactivity_ms:.0f}ms, reconnecting"
                    )
                    self._spawn_background(self._reconnect())
                    return
        except asyncio.CancelledError:
            return

    async def _reconnect(self) -> None:
        if not self._should_reconnect or self._is_reconnecting:
            return
        self._is_reconnecting = True
        try:
            await self._teardown_socket(close_socket=True)
            while self._should_reconnect:
                self._reconnect_attempt += 1
                if self._reconnect_attempt > self._config.max_reconnect_attempts:
                    self._log.error(
                        f"Reconnection failed after {self._reconnect_attempt - 1} "
                        "attempts, giving up"
                    )
                    error = create_runware_error(
                        "reconnectionFailed",
                        (
                            "Permanently disconnected after "
                            f"{self._reconnect_attempt - 1} reconnection attempts"
                        ),
                    )
                    for cb in list(self._task_callbacks.values()):
                        cb({"error": [{"code": "reconnectionFailed", "message": str(error)}]})
                    self._task_callbacks.clear()
                    return

                # Exponential backoff with jitter. Jitter is applied AFTER the
                # cap so a thundering herd at the ceiling still spreads out —
                # otherwise once base ≥ cap, jitter gets squashed to zero and
                # every client reconnects on the same millisecond.
                base_ms = self._config.retry_delay * (2 ** (self._reconnect_attempt - 1))
                capped_ms = min(base_ms, _RECONNECT_BACKOFF_CAP_MS)
                jitter_ms = secrets.randbelow(_RECONNECT_JITTER_MAX_MS + 1)
                delay_ms = capped_ms + jitter_ms
                self._log.connection(
                    f"Reconnect attempt {self._reconnect_attempt} in {delay_ms}ms"
                )
                await asyncio.sleep(delay_ms / 1000.0)

                if not self._should_reconnect:
                    return

                try:
                    await self._open_once()
                    self._log.connection(
                        f"Reconnected with {len(self._task_callbacks)} pending task(s)"
                    )
                    self._reconnect_attempt = 0
                    return
                except Exception as exc:
                    self._log.error(f"Reconnect failed: {exc}")
        finally:
            self._is_reconnecting = False

    async def _teardown_socket(self, *, close_socket: bool = False) -> None:
        self._connected = False
        if self._heartbeat_task is not None:
            self._heartbeat_task.cancel()
            with contextlib.suppress(asyncio.CancelledError, Exception):
                await self._heartbeat_task
            self._heartbeat_task = None
        if self._receive_task is not None:
            self._receive_task.cancel()
            with contextlib.suppress(asyncio.CancelledError, Exception):
                await self._receive_task
            self._receive_task = None
        if close_socket and self._ws is not None:
            with contextlib.suppress(Exception):
                await self._ws.close()
        self._ws = None

    def _spawn_background(self, coro: Any) -> None:
        """Fire-and-forget an async coro while keeping a strong reference."""
        task = asyncio.create_task(coro)
        self._background_tasks.add(task)
        task.add_done_callback(self._background_tasks.discard)


def _parse_frame(raw: str | bytes) -> dict[str, Any] | None:
    text = raw if isinstance(raw, str) else raw.decode("utf-8", errors="replace")
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return None
    if isinstance(parsed, dict):
        return cast(dict[str, Any], parsed)
    return None


def _redact(payload: list[dict[str, Any]]) -> str:
    redacted = [
        {**task, "apiKey": "[redacted]"}
        if task.get("taskType") == "authentication" and "apiKey" in task
        else task
        for task in payload
    ]
    return json.dumps(redacted)
