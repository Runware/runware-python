"""
Tests for the rule that the SDK never reads the filesystem on its own.

Until 1.7.0 every string in the params was checked against the filesystem and
replaced with the file's base64 if it happened to name one, which made any caller
that forwarded user text into ``run()`` read local files on request. A local
file now travels only through ``file_to_base64`` or ``file_to_data_uri``, which
the caller has to reach for.

The case that matters is the one that used to leak: a prompt that is exactly a
path to a real file has to arrive at the transport as that path.
"""

from __future__ import annotations

import base64
from pathlib import Path
from typing import Any
from unittest.mock import AsyncMock

import pytest

from runware import Runware, file_to_base64, file_to_data_uri
from runware.transport.rest import RestTransport


def _patch_rest(client: Runware, response: Any) -> AsyncMock:
    mock = AsyncMock(spec=RestTransport)
    mock.send_request = AsyncMock(return_value=response)
    mock.close = AsyncMock()
    client._rest_transport = mock
    return mock


async def _sent_for(params: dict[str, Any]) -> dict[str, Any]:
    client = Runware(api_key="sk-test", transport="rest")
    mock = _patch_rest(
        client,
        {"data": [{"taskUUID": "u1", "imageURL": "https://x.jpg", "imageUUID": "i1"}]},
    )
    await client.run(params)
    return mock.send_request.call_args_list[0].args[0]


class TestTheSdkDoesNotReadTheFilesystem:
    @pytest.mark.asyncio
    async def test_a_prompt_that_is_a_real_path_is_sent_as_that_path(
        self, tmp_path: Path
    ) -> None:
        secret = tmp_path / "secrets.env"
        secret.write_bytes(b"API_KEY=leaked")

        sent = await _sent_for(
            {
                "taskType": "imageInference",
                "taskUUID": "u1",
                "model": "runware:101@1",
                "positivePrompt": str(secret),
                "width": 1024,
                "height": 1024,
                "deliveryMethod": "sync",
            }
        )

        assert sent["positivePrompt"] == str(secret)
        assert base64.b64encode(b"API_KEY=leaked").decode("ascii") not in str(sent)

    @pytest.mark.asyncio
    async def test_a_media_param_that_is_a_real_path_is_sent_as_that_path(
        self, tmp_path: Path
    ) -> None:
        f = tmp_path / "seed.jpg"
        f.write_bytes(b"\x89PNG seed bytes")

        sent = await _sent_for(
            {
                "taskType": "imageInference",
                "taskUUID": "u1",
                "model": "runware:101@1",
                "seedImage": str(f),
                "positivePrompt": "x",
                "width": 1024,
                "height": 1024,
                "deliveryMethod": "sync",
            }
        )

        assert sent["seedImage"] == str(f)

    @pytest.mark.asyncio
    async def test_a_nested_path_is_left_alone(self, tmp_path: Path) -> None:
        f = tmp_path / "nested.txt"
        f.write_bytes(b"nested bytes")

        sent = await _sent_for(
            {
                "taskType": "imageInference",
                "taskUUID": "u1",
                "model": "runware:101@1",
                "positivePrompt": "x",
                "referenceImages": [str(f)],
                "width": 1024,
                "height": 1024,
                "deliveryMethod": "sync",
            }
        )

        assert sent["referenceImages"] == [str(f)]


class TestALocalFileTravelsWhenTheCallerAsks:
    def test_file_to_base64_has_no_prefix(self, tmp_path: Path) -> None:
        f = tmp_path / "photo.jpg"
        f.write_bytes(b"\x89PNG photo bytes")

        assert file_to_base64(str(f)) == base64.b64encode(b"\x89PNG photo bytes").decode("ascii")

    def test_file_to_data_uri_carries_the_mime(self, tmp_path: Path) -> None:
        f = tmp_path / "photo.jpg"
        f.write_bytes(b"bytes")

        encoded = base64.b64encode(b"bytes").decode("ascii")
        assert file_to_data_uri(str(f)) == f"data:image/jpeg;base64,{encoded}"

    def test_bytes_the_caller_already_holds(self) -> None:
        assert file_to_base64(b"\x01\x02\x03") == base64.b64encode(b"\x01\x02\x03").decode("ascii")

    @pytest.mark.asyncio
    async def test_it_reaches_the_transport_when_encoded_first(self, tmp_path: Path) -> None:
        f = tmp_path / "seed.jpg"
        f.write_bytes(b"\x89PNG seed bytes")

        sent = await _sent_for(
            {
                "taskType": "imageInference",
                "taskUUID": "u1",
                "model": "runware:101@1",
                "seedImage": file_to_base64(str(f)),
                "positivePrompt": "x",
                "width": 1024,
                "height": 1024,
                "deliveryMethod": "sync",
            }
        )

        assert sent["seedImage"] == base64.b64encode(b"\x89PNG seed bytes").decode("ascii")
