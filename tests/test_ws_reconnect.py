"""
Reconnect behavior of the WebSocket transport against a fake server.

The fake server plays the API over an injected `ws_connect`: it answers
authentication and pings, records every task it receives per socket, and can
drop a connection, refuse new ones (network down), or reply to tasks through a
per-test handler.
"""

from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any

import pytest
from websockets.exceptions import ConnectionClosed

from runware import Runware, RunwareError
from runware.errors import parse_api_error
from runware.transport.websocket import WebSocketTransport
from runware.types.sdk import RuntimeDependencies, SDKConfig

Handler = Callable[[dict[str, Any], "FakeConnection"], None]


class FakeConnection:
    def __init__(self, server: FakeServer, socket_id: int) -> None:
        self.server = server
        self.id = socket_id
        self.dead = False
        self.inbox: asyncio.Queue[str | None] = asyncio.Queue()

    async def send(self, data: str) -> None:
        if self.dead:
            raise ConnectionClosed(None, None)
        for task in json.loads(data):
            task_type = task["taskType"]
            if task_type == "authentication":
                self.server.log.append(f"s{self.id}:auth")
                asyncio.get_running_loop().call_later(self.server.auth_delay, self._auth_ok)
                continue
            if task_type == "ping":
                if self.server.silent_socket != self.id:
                    self.deliver({"data": [{"taskType": "ping", "pong": True}]})
                continue
            self.server.log.append(f"s{self.id}:{task_type}")
            self.server.received.append((self.id, task))
            self.server.handler(task, self)

    def _auth_ok(self) -> None:
        self.server.log.append(f"s{self.id}:auth-ok")
        self.deliver({"data": [{"taskType": "authentication", "connectionSessionUUID": "s-1"}]})

    def deliver(self, frame: dict[str, Any]) -> None:
        if not self.dead:
            self.inbox.put_nowait(json.dumps(frame))

    def drop(self) -> None:
        if self.dead:
            return
        self.dead = True
        self.inbox.put_nowait(None)

    async def recv(self) -> str:
        item = await self.inbox.get()
        if item is None:
            raise ConnectionClosed(None, None)
        return item

    def __aiter__(self) -> FakeConnection:
        return self

    async def __anext__(self) -> str:
        return await self.recv()

    async def close(self) -> None:
        self.drop()


class FakeServer:
    def __init__(self) -> None:
        self.sockets: list[FakeConnection] = []
        self.log: list[str] = []
        self.received: list[tuple[int, dict[str, Any]]] = []
        self.down = False
        self.silent_socket = 0
        self.auth_delay = 0.0
        self.handler: Handler = lambda task, conn: None

    async def connect(self, url: str) -> FakeConnection:
        if self.down:
            raise OSError("network down")
        conn = FakeConnection(self, len(self.sockets) + 1)
        self.sockets.append(conn)
        return conn

    def drop(self) -> None:
        self.sockets[-1].drop()

    def sent_on(self, task_type: str) -> list[int]:
        return [socket_id for socket_id, task in self.received if task["taskType"] == task_type]


def _transport(server: FakeServer) -> WebSocketTransport:
    config = SDKConfig(
        api_key="sk-test",
        transport="websocket",
        timeout=5_000,
        poll_timeout=5_000,
        auth_timeout=5_000,
        retry_delay=10,
        dependencies=RuntimeDependencies(ws_connect=server.connect),  # pyright: ignore[reportArgumentType]
    )
    return WebSocketTransport(config)


def _client(server: FakeServer, **overrides: Any) -> Runware:
    return Runware(
        api_key="sk-test",
        transport="websocket",
        retry_delay=10,
        dependencies=RuntimeDependencies(ws_connect=server.connect),  # pyright: ignore[reportArgumentType]
        **overrides,
    )


async def _wait_for(condition: Callable[[], bool], within: float = 3.0) -> None:
    deadline = asyncio.get_running_loop().time() + within
    while not condition():
        if asyncio.get_running_loop().time() > deadline:
            raise AssertionError("condition not met in time")
        await asyncio.sleep(0.005)


async def _wait_until_dropped(transport: WebSocketTransport) -> None:
    await _wait_for(lambda: not transport.is_connected)


def _conflict(task_uuid: str) -> dict[str, Any]:
    return {"errors": [{"code": "conflictTaskUUID", "message": "Conflict", "taskUUID": task_uuid}]}


def _success(task_uuid: str) -> dict[str, Any]:
    return {"data": [{
        "taskUUID": task_uuid,
        "taskType": "imageInference",
        "status": "success",
        "imageUUID": "i1",
        "imageURL": "https://example.com/img.jpg",
    }]}


IMAGE_PARAMS: dict[str, Any] = {
    "taskType": "imageInference",
    "model": "runware:101@1",
    "positivePrompt": "x",
    "width": 1024,
    "height": 1024,
}


@pytest.fixture(autouse=True)
def _no_jitter(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("runware.transport.websocket.secrets.randbelow", lambda _bound: 0)  # pyright: ignore[reportUnknownLambdaType]


class TestHoldAndResend:
    async def test_holds_a_request_sent_while_reconnecting_until_authenticated(self) -> None:
        server = FakeServer()
        transport = _transport(server)
        await transport.connect()

        server.auth_delay = 0.05
        server.drop()
        await _wait_until_dropped(transport)
        await transport.send_request({"taskType": "getResponse", "taskUUID": "t1"})

        await _wait_for(lambda: len(server.received) == 1)
        assert server.received[0][0] == 2
        assert [entry for entry in server.log if entry.startswith("s2")] == [
            "s2:auth", "s2:auth-ok", "s2:getResponse",
        ]
        await transport.disconnect()

    async def test_sends_an_unanswered_get_response_again(self) -> None:
        server = FakeServer()
        server.handler = lambda task, conn: None if conn.id == 1 else conn.deliver(
            {"data": [{"taskUUID": task["taskUUID"], "status": "processing"}]},
        )
        transport = _transport(server)
        await transport.connect()

        frames: list[Any] = []
        transport.subscribe_to_task("t1", frames.append)
        await transport.send_request({"taskType": "getResponse", "taskUUID": "t1"})
        server.drop()

        await _wait_for(lambda: len(frames) == 1)
        assert server.sent_on("getResponse") == [1, 2]
        assert frames[0]["data"][0]["status"] == "processing"
        await transport.disconnect()

    async def test_conflict_on_a_resent_async_submission_is_its_ack(self) -> None:
        server = FakeServer()
        server.handler = lambda task, conn: None if conn.id == 1 else conn.deliver(
            _conflict(task["taskUUID"]),
        )
        transport = _transport(server)
        await transport.connect()

        frames: list[Any] = []
        transport.subscribe_to_task("t1", frames.append)
        await transport.send_request(
            {"taskType": "imageInference", "taskUUID": "t1", "deliveryMethod": "async"},
        )
        server.drop()

        await _wait_for(lambda: len(frames) == 1)
        assert server.sent_on("imageInference") == [1, 2]
        assert frames[0] == {"data": [{"taskType": "imageInference", "taskUUID": "t1"}]}
        await transport.disconnect()

    async def test_conflict_on_a_single_send_stays_an_error(self) -> None:
        server = FakeServer()
        server.handler = lambda task, conn: conn.deliver(_conflict(task["taskUUID"]))
        transport = _transport(server)
        await transport.connect()

        frames: list[Any] = []
        transport.subscribe_to_task("t1", frames.append)
        await transport.send_request(
            {"taskType": "imageInference", "taskUUID": "t1", "deliveryMethod": "async"},
        )

        await _wait_for(lambda: len(frames) == 1)
        assert parse_api_error(frames[0]["error"]).code == "validation"
        await transport.disconnect()

    async def test_fails_a_sync_request_that_may_have_run_instead_of_resending(self) -> None:
        server = FakeServer()
        transport = _transport(server)
        await transport.connect()

        frames: list[Any] = []
        transport.subscribe_to_task("t1", frames.append)
        await transport.send_request({"taskType": "imageInference", "taskUUID": "t1"})
        server.drop()

        await _wait_for(lambda: len(frames) == 1)
        await asyncio.sleep(0.05)
        assert server.sent_on("imageInference") == [1]
        error = parse_api_error(frames[0]["error"])
        assert error.code == "connection"
        assert "may have been processed" in str(error)
        await transport.disconnect()

    async def test_sends_a_sync_request_held_during_the_reconnect_once(self) -> None:
        server = FakeServer()
        transport = _transport(server)
        await transport.connect()

        server.drop()
        await _wait_until_dropped(transport)
        await transport.send_request({"taskType": "imageInference", "taskUUID": "t1"})

        await _wait_for(lambda: len(server.received) == 1)
        await asyncio.sleep(0.05)
        assert server.sent_on("imageInference") == [2]
        await transport.disconnect()

    async def test_still_raises_when_no_reconnect_is_coming(self) -> None:
        server = FakeServer()
        transport = _transport(server)

        with pytest.raises(RunwareError, match="Not connected"):
            await transport.send_request({"taskType": "getResponse", "taskUUID": "t1"})

        await transport.connect()
        await transport.disconnect()
        with pytest.raises(RunwareError, match="Not connected"):
            await transport.send_request({"taskType": "getResponse", "taskUUID": "t1"})

    async def test_disconnect_releases_requests_held_during_an_outage(self) -> None:
        server = FakeServer()
        transport = _transport(server)
        await transport.connect()

        server.down = True
        server.drop()
        await _wait_until_dropped(transport)
        frames: list[Any] = []
        transport.subscribe_to_task("t1", frames.append)
        await transport.send_request({"taskType": "getResponse", "taskUUID": "t1"})
        await asyncio.sleep(0.05)

        await transport.disconnect()
        assert len(frames) == 1
        assert frames[0]["error"][0]["code"] == "disconnected"
        with pytest.raises(RunwareError, match="Not connected"):
            await transport.send_request({"taskType": "getResponse", "taskUUID": "t2"})


class TestConnectRaces:
    async def test_concurrent_connects_open_one_socket(self) -> None:
        server = FakeServer()
        transport = _transport(server)

        await asyncio.gather(transport.connect(), transport.connect())
        await asyncio.sleep(0.1)

        assert len(server.sockets) == 1
        assert transport.is_connected
        await transport.disconnect()

    async def test_background_reconnect_keeps_a_socket_opened_by_connect(self) -> None:
        server = FakeServer()
        server.handler = lambda task, conn: conn.deliver(
            {"data": [{"taskUUID": task["taskUUID"], "status": "processing"}]},
        )
        transport = _transport(server)
        await transport.connect()

        server.drop()
        await _wait_until_dropped(transport)
        await transport.connect()
        await asyncio.sleep(0.1)

        assert len(server.sockets) == 2
        assert not server.sockets[1].dead
        frames: list[Any] = []
        transport.subscribe_to_task("t1", frames.append)
        await transport.send_request({"taskType": "getResponse", "taskUUID": "t1"})
        await _wait_for(lambda: len(frames) == 1)
        await transport.disconnect()

    async def test_ensure_connected_leaves_an_ongoing_reconnect_alone(self) -> None:
        server = FakeServer()
        transport = _transport(server)
        await transport.connect()

        server.down = True
        server.drop()
        await _wait_until_dropped(transport)
        await transport.ensure_connected()
        assert len(server.sockets) == 1

        server.down = False
        await _wait_for(lambda: transport.is_connected)
        assert len(server.sockets) == 2
        await transport.disconnect()


class TestRunOverADroppingConnection:
    async def test_completes_when_the_connection_drops_before_the_ack(self) -> None:
        server = FakeServer()

        def handler(task: dict[str, Any], conn: FakeConnection) -> None:
            if task["taskType"] == "imageInference" and conn.id == 1:
                conn.drop()
            elif task["taskType"] == "imageInference":
                conn.deliver(_conflict(task["taskUUID"]))
            else:
                conn.deliver(_success(task["taskUUID"]))

        server.handler = handler
        client = _client(server)
        await client.connect()

        results = await asyncio.wait_for(client.run(IMAGE_PARAMS), timeout=10)
        assert results[0]["imageURL"] == "https://example.com/img.jpg"
        assert server.sent_on("imageInference") == [1, 2]
        await client.close()

    async def test_completes_when_the_connection_is_down_while_a_poll_is_due(self) -> None:
        server = FakeServer()

        def restore() -> None:
            server.down = False

        def handler(task: dict[str, Any], conn: FakeConnection) -> None:
            if task["taskType"] == "imageInference":
                conn.deliver({"data": [{"taskType": "imageInference", "taskUUID": task["taskUUID"]}]})
                server.down = True
                conn.drop()
                asyncio.get_running_loop().call_later(1.2, restore)
            else:
                conn.deliver(_success(task["taskUUID"]))

        server.handler = handler
        client = _client(server)
        await client.connect()

        results = await asyncio.wait_for(client.run(IMAGE_PARAMS), timeout=10)
        assert results[0]["imageURL"] == "https://example.com/img.jpg"
        assert all(socket_id > 1 for socket_id in server.sent_on("getResponse"))
        await client.close()

    async def test_keeps_waiting_for_the_ack_while_an_outage_outlasts_the_window(
        self, monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setattr("runware.client._ACK_TIMEOUT_SECONDS", 0.3, raising=False)
        server = FakeServer()

        def restore() -> None:
            server.down = False

        def handler(task: dict[str, Any], conn: FakeConnection) -> None:
            if task["taskType"] == "imageInference" and conn.id == 1:
                server.down = True
                conn.drop()
                asyncio.get_running_loop().call_later(1.0, restore)
            elif task["taskType"] == "imageInference":
                conn.deliver(_conflict(task["taskUUID"]))
            else:
                conn.deliver(_success(task["taskUUID"]))

        server.handler = handler
        client = _client(server)
        await client.connect()

        results = await asyncio.wait_for(client.run(IMAGE_PARAMS), timeout=10)
        assert results[0]["imageURL"] == "https://example.com/img.jpg"
        assert server.sent_on("imageInference") == [1, len(server.sockets)]
        await client.close()
