"""
Client identifier for outgoing requests.

Lets Runware attribute traffic to the SDK, its version, the host runtime, and
the schemas snapshot it was built against.

Base format: ``runware-python/<version> (<runtime>) schemas/<schemas-version>``
  e.g. ``runware-python/1.4.1 (python/3.12.1; Darwin arm64) schemas/20260623192341``

A ``prefix`` (from ``config.user_agent_prefix``) is prepended so wrappers —
higher-level apps, servers — identify themselves ahead of the SDK token.

Only takes effect where the transport can set an HTTP header: the REST calls
and the WebSocket handshake (``additional_headers``).
"""

from __future__ import annotations

import platform
from importlib.metadata import PackageNotFoundError, version

from ._schemas_version import SCHEMAS_VERSION


def _resolve_sdk_version() -> str:
    try:
        return version("runware-sdk")
    except PackageNotFoundError:  # running from an uninstalled source tree
        return "0.0.0"


_SDK_VERSION = _resolve_sdk_version()
_base: str | None = None


def _base_user_agent() -> str:
    global _base
    if _base is None:
        runtime = (
            f"python/{platform.python_version()}; "
            f"{platform.system()} {platform.machine()}"
        )
        _base = f"runware-python/{_SDK_VERSION} ({runtime}) schemas/{SCHEMAS_VERSION}"
    return _base


def user_agent(prefix: str | None = None) -> str:
    base = _base_user_agent()
    return f"{prefix} {base}" if prefix else base
