"""File → data URI helper for image/video/audio inputs."""

from __future__ import annotations

import base64
import io
import mimetypes
import os
from pathlib import Path
from typing import BinaryIO, cast

# Strings longer than this can't plausibly be a filesystem path — a base64 blob
# or data URI is far longer. Skipping them avoids hitting the disk for them.
_MAX_PATH_LEN = 4096
_REMOTE_PREFIXES = ("http://", "https://", "data:")


def _read_bytes(source: str | Path | bytes | BinaryIO) -> bytes:
    if isinstance(source, (str, Path)):
        return Path(source).read_bytes()
    if isinstance(source, bytes):
        return source
    if isinstance(source, io.IOBase) or hasattr(source, "read"):
        raw = source.read()
        # BinaryIO.read() statically returns bytes but users may pass a TextIO
        # by mistake — keep the runtime check.
        if not isinstance(raw, (bytes, bytearray)):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError("file-like source must return bytes from .read()")
        return bytes(raw)
    raise TypeError(
        f"unsupported source type {type(source).__name__}"
    )


def file_to_base64(source: str | Path | bytes | BinaryIO) -> str:
    """
    Encode a file, bytes blob, or file-like into a raw base64 string (ascii),
    with no `data:` prefix or MIME type.

    The API sniffs the real format from the bytes, so sending bare base64
    avoids extension-based MIME guessing. Accepts the same source types as
    `file_to_data_uri`.
    """
    return base64.b64encode(_read_bytes(source)).decode("ascii")


def _looks_like_local_file(value: str) -> bool:
    if value.startswith(_REMOTE_PREFIXES):
        return False
    if len(value) > _MAX_PATH_LEN:
        return False
    try:
        return os.path.isfile(value)
    except (OSError, ValueError):
        return False


def encode_local_files(value: object) -> object:
    """
    Recursively walk a params object (dicts, lists, strings) and replace any
    string that points to an existing local file with its base64 contents.

    URLs, data URIs, UUIDs, prompts, existing base64, numbers, and bools pass
    through untouched — only strings that resolve to a real file on disk are
    converted. A string that merely looks like a path but doesn't exist is left
    as-is (no error raised).
    """
    if isinstance(value, str):
        if _looks_like_local_file(value):
            return file_to_base64(value)
        return value
    if isinstance(value, dict):
        items = cast("dict[object, object]", value)
        return {k: encode_local_files(v) for k, v in items.items()}
    if isinstance(value, list):
        items_list = cast("list[object]", value)
        return [encode_local_files(item) for item in items_list]
    return value


def file_to_data_uri(source: str | Path | bytes | BinaryIO) -> str:
    """
    Encode a file, bytes blob, or file-like into a `data:<mime>;base64,...` URI.

    Accepts:
      - `str` or `pathlib.Path` — read from disk, infer MIME from extension.
      - `bytes` — encode directly with `application/octet-stream`.
      - file-like (anything with `.read()` returning bytes).
    """
    if isinstance(source, (str, Path)):
        mime, _ = mimetypes.guess_type(Path(source).name)
        mime = mime or "application/octet-stream"
    else:
        mime = "application/octet-stream"

    encoded = base64.b64encode(_read_bytes(source)).decode("ascii")
    return f"data:{mime};base64,{encoded}"
