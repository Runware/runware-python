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
from collections.abc import Callable, Coroutine
from dataclasses import dataclass
from typing import Any, cast

import websockets
from websockets.asyncio.client import ClientConnection
from websockets.exceptions import ConnectionClosed

from ..errors import RunwareError, create_runware_error
from ..logger import Logger
from ..types.sdk import LoosePayload, SDKConfig
from ..types.transport import WireFrame
from ..user_agent import user_agent

WsResponse = WireFrame
ResponseCallback = Callable[[WsResponse], None]

_HEARTBEAT_INTERVAL_SECONDS = 30.0
_HEARTBEAT_INACTIVITY_THRESHOLD_MS = 100_000
_RECONNECT_BACKOFF_CAP_MS = 30_000
_RECONNECT_JITTER_MAX_MS = 1_000
_ASYNC_RESEND_MIN_AGE_SECONDS = 1.0
_READ_ONLY_TASK_TYPES = frozenset({"getResponse", "getTaskDetails", "modelSearch", "accountManagement"})


def _can_resend(task: LoosePayload) -> bool:
    return task.get("taskType") in _READ_ONLY_TASK_TYPES or task.get("deliveryMethod") == "async"


@dataclass
class _InFlightRequest:
    task: LoosePayload
    sent: bool
    sent_at: float
    resent: bool = False
    resend_scheduled: bool = False


class WebSocketTransport:
    """Async WebSocket transport with auto-reconnect and per-task dispatch."""

    type: str = "websocket"

    def __init__(self, config: SDKConfig) -> None:
        self._config: SDKConfig = config
        self._log: Logger = config.log
        self._ws: ClientConnection | None = None
        self._receive_task: asyncio.Task[None] | None = None
        self._heartbeat_task: asyncio.Task[None] | None = None
        self._background_tasks: set[asyncio.Task[None]] = set()
        self._task_callbacks: dict[str, ResponseCallback] = {}
        self._in_flight: dict[str, _InFlightRequest] = {}
        self._connected: bool = False
        self._connected_at: float | None = None
        self._key_rejected: bool = False
        self._should_reconnect: bool = False
        self._is_reconnecting: bool = False
        self._reconnect_attempt: int = 0
        self._session_uuid: str | None = None
        self._last_activity_ms: float = time.monotonic() * 1000
        self._connect_lock: asyncio.Lock = asyncio.Lock()

    @property
    def is_connected(self) -> bool:
        return self._connected

    @property
    def session_id(self) -> str | None:
        return self._session_uuid

    @property
    def connected_at(self) -> float | None:
        """`time.monotonic()` of the last successful authentication."""
        return self._connected_at

    async def connect(self) -> None:
        """Open the WebSocket and authenticate. No-op when already connected."""
        async with self._connect_lock:
            self._should_reconnect = True
            if self._connected:
                return
            # Reset the reconnect counter so a fresh connect() after a prior
            # give-up doesn't start already over the limit.
            self._reconnect_attempt = 0
            self._key_rejected = False
            await self._open_once()

    async def ensure_connected(self) -> None:
        """Connect unless connected, or unless a reconnect is already under way."""
        if self._connected or self._will_reconnect():
            return
        await self.connect()

    async def disconnect(self) -> None:
        """Close the socket and stop reconnect attempts."""
        self._should_reconnect = False
        for cb in list(self._task_callbacks.values()):
            try:
                cb({"error": [{"code": "disconnected", "message": "Client disconnected"}]})
            except Exception as exc:
                self._log.error(f"task callback raised during disconnect: {exc}")
        self._task_callbacks.clear()
        self._in_flight.clear()
        await self._teardown_socket(close_socket=True)

    async def send_request(
        self,
        data: LoosePayload | list[LoosePayload],
    ) -> None:
        if not self._connected and not self._will_reconnect():
            raise create_runware_error("notConnected", "Not connected to WebSocket server")
        payload = data if isinstance(data, list) else [data]
        for task in payload:
            task_uuid = task.get("taskUUID")
            if isinstance(task_uuid, str):
                self._in_flight[task_uuid] = _InFlightRequest(
                    task=task, sent=self._connected, sent_at=time.monotonic(),
                )
        if not self._connected:
            self._log.connection(
                f"Reconnecting, holding {len(payload)} request(s) until the connection is back"
            )
            return
        await self._send(payload)

    def subscribe_to_task(self, task_uuid: str, callback: ResponseCallback) -> None:
        self._task_callbacks[task_uuid] = callback

    def unsubscribe_from_task(self, task_uuid: str) -> None:
        self._task_callbacks.pop(task_uuid, None)
        self._in_flight.pop(task_uuid, None)

    def _will_reconnect(self) -> bool:
        return self._should_reconnect and self._is_reconnecting

    async def _send(self, payload: list[LoosePayload]) -> None:
        ws = self._ws
        if ws is None:
            raise create_runware_error("notConnected", "Not connected to WebSocket server")
        self._log.send(_redact(payload))
        try:
            await ws.send(json.dumps(payload))
        except (ConnectionClosed, OSError) as exc:
            if not self._should_reconnect:
                raise create_runware_error(
                    "sendFailed",
                    f"Failed to send WebSocket message: {exc}",
                ) from exc
            for task in payload:
                request = self._in_flight.get(cast(str, task.get("taskUUID")))
                if request is not None:
                    request.sent = False
            self._log.connection(f"Send failed, holding {len(payload)} request(s): {exc}")
            if self._ws is ws:
                self._connected = False
                self._schedule_reconnect()

    async def _resend_later(self, task_uuid: str, delay: float) -> None:
        await asyncio.sleep(delay)
        request = self._in_flight.get(task_uuid)
        if request is None:
            return
        request.resend_scheduled = False
        if not self._connected:
            return
        request.resent = True
        request.sent_at = time.monotonic()
        with contextlib.suppress(RunwareError):
            await self._send([request.task])

    async def _send_in_flight(self) -> None:
        pending: list[LoosePayload] = []
        for task_uuid, request in list(self._in_flight.items()):
            if request.sent and not _can_resend(request.task):
                del self._in_flight[task_uuid]
                cb = self._task_callbacks.get(task_uuid)
                if cb is not None:
                    self._safe_call(cb, {"error": [{
                        "code": "connectionLost",
                        "message": (
                            "Connection lost before the response arrived. "
                            "The request may have been processed."
                        ),
                        "taskUUID": task_uuid,
                    }]})
                continue
            age = time.monotonic() - request.sent_at
            if (
                request.sent
                and request.task.get("deliveryMethod") == "async"
                and age < _ASYNC_RESEND_MIN_AGE_SECONDS
            ):
                if not request.resend_scheduled:
                    request.resend_scheduled = True
                    self._spawn_background(
                        self._resend_later(task_uuid, _ASYNC_RESEND_MIN_AGE_SECONDS - age),
                    )
                continue
            if request.sent:
                request.resent = True
            request.sent = True
            request.sent_at = time.monotonic()
            pending.append(request.task)
        if not pending:
            return
        self._log.connection(f"Sending {len(pending)} pending request(s) after reconnect")
        await self._send(pending)

    async def _default_connect(self, url: str) -> ClientConnection:
        # Identify the client on the handshake. `additional_headers` is the
        # modern websockets kwarg (asyncio client, >=14); older releases (13)
        # spell it `extra_headers`, so fall back on the arg-name TypeError.
        headers = {"User-Agent": user_agent(self._config.user_agent_prefix)}
        try:
            return await websockets.connect(url, additional_headers=headers)
        except TypeError:
            return await websockets.connect(url, extra_headers=headers)

    async def _open_once(self) -> None:
        await self._teardown_socket(close_socket=True)

        custom_connect = (
            self._config.dependencies.ws_connect
            if self._config.dependencies and self._config.dependencies.ws_connect
            else None
        )
        try:
            # An injected `ws_connect` owns its own headers (see its docstring);
            # the default connect carries the client identifier on the handshake.
            if custom_connect is not None:
                self._ws = await custom_connect(self._config.ws_base_url)
            else:
                self._ws = await self._default_connect(self._config.ws_base_url)
        except (OSError, websockets.InvalidURI, websockets.InvalidHandshake) as exc:
            raise create_runware_error(
                "connectionFailed",
                f"WebSocket connection failed: {exc}",
            ) from exc

        try:
            await self._authenticate()
        except BaseException:
            await self._teardown_socket(close_socket=True)
            raise

        self._connected = True
        self._connected_at = time.monotonic()
        self._last_activity_ms = time.monotonic() * 1000
        self._receive_task = asyncio.create_task(self._receive_loop())
        self._heartbeat_task = asyncio.create_task(self._heartbeat_loop())
        await self._send_in_flight()

    async def _authenticate(self) -> None:
        if self._ws is None:
            raise create_runware_error("notOpen", "WebSocket not open for authentication")

        auth_message: LoosePayload = {
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
        data: LoosePayload | None = None
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
                errs: list[object] = (
                    cast(list[object], raw_errors)
                    if isinstance(raw_errors, list)
                    else [raw_errors]
                )
                first_err: LoosePayload = {}
                if errs and isinstance(errs[0], dict):
                    first_err = cast(LoosePayload, errs[0])
                self._key_rejected = True
                raise create_runware_error(
                    "authFailed",
                    first_err.get("message")
                    or "Authentication failed via API response",
                )

            items_raw = frame.get("data")
            items: list[object] = (
                cast(list[object], items_raw)
                if isinstance(items_raw, list)
                else []
            )
            # Skim past anything that isn't the auth response — pings,
            # stale frames, etc.
            found = False
            for item in items:
                if not isinstance(item, dict):
                    continue
                if cast(LoosePayload, item).get("taskType") == "authentication":
                    data = frame
                    found = True
                    break
            if found:
                break
            # Not the auth frame — keep waiting.
            self._log.warn("Skipping non-auth frame during authentication handshake")

        if data is None:
            raise RuntimeError("Authentication loop exited without receiving an auth frame")
        items_raw = data.get("data")
        items = (
            cast(list[object], items_raw) if isinstance(items_raw, list) else []
        )
        first: LoosePayload | None = None
        for candidate in items:
            if not isinstance(candidate, dict):
                continue
            candidate_dict = cast(LoosePayload, candidate)
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
        self._key_rejected = False

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
            if self._ws is ws:
                self._connected = False
                self._schedule_reconnect()

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

    def _dispatch(self, frame: LoosePayload) -> None:
        raw_errors = frame.get("errors") or frame.get("error")
        if raw_errors:
            errors_list: list[LoosePayload] = (
                cast(list[LoosePayload], raw_errors)
                if isinstance(raw_errors, list)
                else [cast(LoosePayload, raw_errors)]
            )
            by_task: dict[str, list[LoosePayload]] = {}
            unrouted: list[LoosePayload] = []
            for err in errors_list:
                task_uuid = err.get("taskUUID")
                if isinstance(task_uuid, str):
                    by_task.setdefault(task_uuid, []).append(err)
                else:
                    unrouted.append(err)
            delivered = False
            for task_uuid, errs in by_task.items():
                request = self._in_flight.pop(task_uuid, None)
                cb = self._task_callbacks.get(task_uuid)
                if cb is None:
                    continue
                delivered = True
                if (
                    request is not None
                    and request.resent
                    and request.task.get("deliveryMethod") == "async"
                    and all(err.get("code") == "conflictTaskUUID" for err in errs)
                ):
                    ack_item: dict[str, object] = {
                        "taskType": request.task.get("taskType"),
                        "taskUUID": task_uuid,
                    }
                    self._safe_call(cb, {"data": [ack_item]})
                else:
                    self._safe_call(cb, {"error": errs})
            if unrouted or not delivered:
                self._log.error("Unroutable WebSocket error", errors_list)
                for cb in self._task_callbacks.values():
                    self._safe_call(cb, {"error": errors_list})
            return

        data = frame.get("data")
        if not isinstance(data, list):
            return

        items_by_task: dict[str, list[LoosePayload]] = {}
        for item in cast(list[object], data):
            if not isinstance(item, dict):
                continue
            item_dict = cast(LoosePayload, item)
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
            self._in_flight.pop(task_uuid, None)
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
                    self._schedule_reconnect()
                    return

                inactivity_ms = time.monotonic() * 1000 - self._last_activity_ms
                if inactivity_ms > _HEARTBEAT_INACTIVITY_THRESHOLD_MS:
                    self._log.heartbeat(
                        f"No activity for {inactivity_ms:.0f}ms, reconnecting"
                    )
                    self._schedule_reconnect()
                    return
        except asyncio.CancelledError:
            return

    def _schedule_reconnect(self) -> None:
        if not self._should_reconnect or self._is_reconnecting:
            return
        self._is_reconnecting = True
        self._spawn_background(self._reconnect())

    async def _reconnect(self) -> None:
        try:
            async with self._connect_lock:
                await self._teardown_socket(close_socket=True)
            while self._should_reconnect:
                self._reconnect_attempt += 1
                if self._reconnect_attempt > self._config.max_reconnect_attempts:
                    attempts = self._reconnect_attempt - 1
                    self._log.error(f"Reconnection failed after {attempts} attempts, giving up")
                    error = create_runware_error(
                        "reconnectionFailed",
                        f"Permanently disconnected after {attempts} reconnection attempts",
                    )
                    for cb in list(self._task_callbacks.values()):
                        self._safe_call(
                            cb, {"error": [{"code": "reconnectionFailed", "message": str(error)}]},
                        )
                    self._task_callbacks.clear()
                    self._in_flight.clear()
                    return

                # Exponential backoff with jitter. Jitter is applied AFTER the
                # cap so a thundering herd at the ceiling still spreads out —
                # otherwise once base ≥ cap, jitter gets squashed to zero and
                # every client reconnects on the same millisecond.
                # pow(2, n) returns int for non-negative n; cast to silence the
                # type stubs' int|float widening.
                base_ms: int = self._config.retry_delay * cast(
                    int, 2 ** (self._reconnect_attempt - 1),
                )
                capped_ms: int = min(base_ms, _RECONNECT_BACKOFF_CAP_MS)
                jitter_ms: int = secrets.randbelow(_RECONNECT_JITTER_MAX_MS + 1)
                delay_ms: int = capped_ms + jitter_ms
                self._log.connection(
                    f"Reconnect attempt {self._reconnect_attempt} in {delay_ms}ms"
                )
                await asyncio.sleep(delay_ms / 1000.0)

                if not self._should_reconnect:
                    return

                async with self._connect_lock:
                    if self._connected:
                        self._reconnect_attempt = 0
                        return
                    try:
                        await self._open_once()
                    except Exception as exc:
                        self._log.error(f"Reconnect failed: {exc}")
                        if self._key_rejected:
                            self._log.error("The server rejected the API key on reconnect, giving up")
                            for cb in list(self._task_callbacks.values()):
                                self._safe_call(
                                    cb, {"error": [{"code": "authFailed", "message": str(exc)}]},
                                )
                            self._task_callbacks.clear()
                            self._in_flight.clear()
                            return
                        continue
                self._log.connection(
                    f"Reconnected with {len(self._task_callbacks)} pending task(s)"
                )
                self._reconnect_attempt = 0
                return
        finally:
            self._is_reconnecting = False

    async def _teardown_socket(self, *, close_socket: bool = False) -> None:
        self._connected = False
        ws = self._ws
        self._ws = None
        heartbeat_task, self._heartbeat_task = self._heartbeat_task, None
        receive_task, self._receive_task = self._receive_task, None
        if heartbeat_task is not None:
            heartbeat_task.cancel()
            with contextlib.suppress(asyncio.CancelledError, Exception):
                await heartbeat_task
        if receive_task is not None:
            receive_task.cancel()
            with contextlib.suppress(asyncio.CancelledError, Exception):
                await receive_task
        if close_socket and ws is not None:
            with contextlib.suppress(Exception):
                await ws.close()

    def _spawn_background(
        self,
        coro: Coroutine[Any, Any, None],  # pyright: ignore[reportExplicitAny]
    ) -> None:
        """Fire-and-forget an async coro while keeping a strong reference."""
        task = asyncio.create_task(coro)
        self._background_tasks.add(task)
        task.add_done_callback(self._background_tasks.discard)


def _parse_frame(raw: str | bytes) -> LoosePayload | None:
    text = raw if isinstance(raw, str) else raw.decode("utf-8", errors="replace")
    try:
        parsed: object = cast(object, json.loads(text))
    except json.JSONDecodeError:
        return None
    if isinstance(parsed, dict):
        return cast(LoosePayload, parsed)
    return None


def _redact(payload: list[LoosePayload]) -> str:
    redacted = [
        {**task, "apiKey": "[redacted]"}
        if task.get("taskType") == "authentication" and "apiKey" in task
        else task
        for task in payload
    ]
    return json.dumps(redacted)
