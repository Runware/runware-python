"""
Config helpers.

The SDK config is a dataclass produced by `create_config`. API key falls back
to `RUNWARE_API_KEY` from the environment — same pattern as OpenAI/Anthropic/
Stripe SDKs. We don't load `.env` ourselves; the runtime (or `python-dotenv`)
is responsible for populating `os.environ`.
"""

from __future__ import annotations

import os
from typing import Any

from .errors import create_runware_error
from .logger import create_logger
from .types.sdk import SDKConfig


def _coalesce_api_key(passed: str | None) -> str:
    if passed:
        return passed
    env_key = os.environ.get("RUNWARE_API_KEY")
    if env_key:
        return env_key
    raise create_runware_error(
        "missingApiKey",
        "API key is required. Pass `api_key=...` or set RUNWARE_API_KEY in the environment.",
    )


def create_config(
    *,
    api_key: str | None = None,
    **overrides: Any,
) -> SDKConfig:
    """
    Build an SDKConfig from user-supplied values + environment fallback.

    Unknown keys raise — typos like `apikey` or `httpbaseurl` would otherwise
    silently turn into runtime bugs.
    """
    resolved_key = _coalesce_api_key(api_key)

    init_fields = {
        name for name, f in SDKConfig.__dataclass_fields__.items() if f.init
    }
    unknown = set(overrides) - init_fields
    if unknown:
        raise create_runware_error(
            "invalidConfig",
            f"Unknown SDKConfig field(s): {', '.join(sorted(unknown))}",
        )

    config = SDKConfig(api_key=resolved_key, **overrides)
    config.log = create_logger(config.debug, sink=config.log_sink)
    return config
