"""File → data URI helper for image/video/audio inputs."""

from __future__ import annotations

import base64
import io
import mimetypes
from pathlib import Path
from typing import BinaryIO


def file_to_data_uri(source: str | Path | bytes | BinaryIO) -> str:
    """
    Encode a file, bytes blob, or file-like into a `data:<mime>;base64,...` URI.

    Accepts:
      - `str` or `pathlib.Path` — read from disk, infer MIME from extension.
      - `bytes` — encode directly with `application/octet-stream`.
      - file-like (anything with `.read()` returning bytes).
    """
    if isinstance(source, (str, Path)):
        path = Path(source)
        data = path.read_bytes()
        mime, _ = mimetypes.guess_type(path.name)
        mime = mime or "application/octet-stream"
    elif isinstance(source, bytes):
        data = source
        mime = "application/octet-stream"
    elif isinstance(source, io.IOBase) or hasattr(source, "read"):
        raw = source.read()
        # BinaryIO.read() statically returns bytes but users may pass a TextIO
        # by mistake — keep the runtime check.
        if not isinstance(raw, (bytes, bytearray)):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError("file-like source must return bytes from .read()")
        data = bytes(raw)
        mime = "application/octet-stream"
    else:
        raise TypeError(
            f"file_to_data_uri: unsupported source type {type(source).__name__}"
        )

    encoded = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{encoded}"
