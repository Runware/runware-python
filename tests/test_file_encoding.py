"""
Tests for runware/utils/file.py — auto-encoding of local file paths to base64
when passed as inputs to client.run().
"""

from __future__ import annotations

import base64
from pathlib import Path
from typing import Any
from unittest.mock import AsyncMock

import pytest

from runware import Runware, file_to_base64
from runware.transport.rest import RestTransport
from runware.utils.file import encode_local_files


def _patch_rest(client: Runware, response: Any) -> AsyncMock:
    mock = AsyncMock(spec=RestTransport)
    mock.send_request = AsyncMock(return_value=response)
    mock.close = AsyncMock()
    client._rest_transport = mock
    return mock


class TestEncodeLocalFiles:
    def test_file_to_base64_has_no_prefix(self, tmp_path: Path) -> None:
        f = tmp_path / "photo.jpg"
        f.write_bytes(b"\xff\xd8\xff\xe0binary")
        expected = base64.b64encode(b"\xff\xd8\xff\xe0binary").decode("ascii")
        assert file_to_base64(f) == expected
        assert not file_to_base64(f).startswith("data:")

    def test_existing_file_converted(self, tmp_path: Path) -> None:
        f = tmp_path / "a.png"
        f.write_bytes(b"pixels")
        out = encode_local_files(str(f))
        assert out == base64.b64encode(b"pixels").decode("ascii")

    def test_nonexistent_path_passes_through(self) -> None:
        assert encode_local_files("./not-a-real-file.jpg") == "./not-a-real-file.jpg"

    def test_url_uuid_data_uri_prompt_pass_through(self) -> None:
        assert encode_local_files("https://x.com/a.jpg") == "https://x.com/a.jpg"
        assert encode_local_files("http://x.com/a.jpg") == "http://x.com/a.jpg"
        assert encode_local_files("data:image/png;base64,AAAA") == "data:image/png;base64,AAAA"
        assert encode_local_files("a paragraph that describes a cat") == "a paragraph that describes a cat"
        assert encode_local_files("9f3c-uuid-like-1234") == "9f3c-uuid-like-1234"

    def test_recurses_into_dicts_and_lists(self, tmp_path: Path) -> None:
        a = tmp_path / "a.jpg"
        b = tmp_path / "b.jpg"
        a.write_bytes(b"AAA")
        b.write_bytes(b"BBB")
        from typing import cast

        out = cast(
            "dict[str, Any]",
            encode_local_files(
                {
                    "inputs": {"image": str(a)},
                    "referenceImages": [str(b), "https://x.com/c.jpg"],
                    "positivePrompt": "a cat",
                    "width": 1024,
                    "flag": True,
                }
            ),
        )
        assert out["inputs"]["image"] == base64.b64encode(b"AAA").decode("ascii")
        assert out["referenceImages"][0] == base64.b64encode(b"BBB").decode("ascii")
        assert out["referenceImages"][1] == "https://x.com/c.jpg"
        assert out["positivePrompt"] == "a cat"
        assert out["width"] == 1024
        assert out["flag"] is True


class TestRunAutoEncodes:
    @pytest.mark.asyncio
    async def test_run_encodes_local_seed_image(self, tmp_path: Path) -> None:
        f = tmp_path / "seed.jpg"
        f.write_bytes(b"\x89PNG seed bytes")
        client = Runware(api_key="sk-test", transport="rest")
        mock = _patch_rest(
            client,
            {"data": [{"taskUUID": "u1", "imageURL": "https://x.jpg", "imageUUID": "i1"}]},
        )
        await client.run(
            {
                "taskType": "imageInference",
                "taskUUID": "u1",
                "model": "runware:101@1",
                "seedImage": str(f),
                "referenceImages": ["https://x.com/keep.jpg"],
                "positivePrompt": "x",
                "width": 1024,
                "height": 1024,
                "deliveryMethod": "sync",
            }
        )
        sent = mock.send_request.call_args_list[0].args[0]
        assert sent["seedImage"] == base64.b64encode(b"\x89PNG seed bytes").decode("ascii")
        assert sent["referenceImages"] == ["https://x.com/keep.jpg"]
        assert sent["positivePrompt"] == "x"
