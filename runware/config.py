"""
Config helpers.

The SDK config is a dataclass produced by `create_config`. API key falls back
to `RUNWARE_API_KEY` from the environment — same pattern as OpenAI/Anthropic/
Stripe SDKs. We don't load `.env` ourselves; the runtime (or `python-dotenv`)
is responsible for populating `os.environ`.
"""

from __future__ import annotations

import os

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
    **overrides: object,
) -> SDKConfig:
    """
    Build an SDKConfig from user-supplied values + environment fallback.

    Unknown keys raise — typos like `apikey` or `httpbaseurl` would otherwise
    silently turn into runtime bugs.
    """
    resolved_key = _coalesce_api_key(api_key)

    # dataclasses stubs type Field as Any; safe to iterate but typed loosely.
    init_fields = {
        name
        for name, f in SDKConfig.__dataclass_fields__.items()  # pyright: ignore[reportAny]
        if f.init  # pyright: ignore[reportAny]
    }
    unknown = set(overrides) - init_fields
    if unknown:
        raise create_runware_error(
            "invalidConfig",
            f"Unknown SDKConfig field(s): {', '.join(sorted(unknown))}",
        )

    # Each override is typed `object` because **kwargs are inherently dynamic;
    # SDKConfig's __init__ enforces per-field types at instantiation time.
    config = SDKConfig(api_key=resolved_key, **overrides)  # pyright: ignore[reportArgumentType]
    config.log = create_logger(config.debug, sink=config.log_sink)
    return config
