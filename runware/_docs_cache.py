"""
Tiny module that owns the per-model documentation-URL cache.

Lives separately from `validate.py` (which writes it) and `errors.py` (which
reads it via `_docs_for_model`) so neither needs to import the other — that
import edge would create an `errors↔validate` cycle.
"""

from __future__ import annotations

_docs_url_cache: dict[str, str | None] = {}


def get_docs_url_for_model(model: str) -> str | None:
    """Cached documentation URL base for a model. Populated by `/resolve` calls."""
    return _docs_url_cache.get(model)


def set_docs_url_for_model(model: str, url: str) -> None:
    """Set the cached URL for a model. Called by `validate._fetch_model_schema`."""
    _docs_url_cache[model] = url


def clear_docs_url_cache() -> None:
    """Reset the docs-URL cache. Used by `clear_validator_cache`."""
    _docs_url_cache.clear()
