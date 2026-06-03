"""
Contract tests — load JSON fixtures from `repos/schemas/fixtures/` and assert
this SDK produces the expected outputs.

The same fixtures are run against the TS SDK by `repos/sdk 2.0/test/contract.test.ts`.
If a case passes here but fails there (or vice versa), the SDKs have drifted on
that behavior and one of them needs to be fixed.

When the schemas repo is moved out-of-tree (after publish), this file should be
updated to fetch fixtures from a versioned URL instead of the local path.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from runware.errors import (
    build_documentation_url,
    derive_code,
    parse_api_error,
)

FIXTURES_DIR = (
    Path(__file__).resolve().parent.parent.parent / "schemas" / "fixtures"
)

pytestmark = pytest.mark.skipif(
    not FIXTURES_DIR.is_dir(),
    reason=f"fixtures not present at {FIXTURES_DIR}",
)


def _load(name: str) -> dict[str, Any]:
    return json.loads((FIXTURES_DIR / name).read_text())


# ----------------------------------------------------------- derive_error_code


def _derive_error_code_cases() -> list[tuple[str, str, str]]:
    if not FIXTURES_DIR.is_dir():
        return []
    fixture = _load("derive-error-codes.json")
    return [
        (case["raw_code"], case["expected_code"], fixture["name"])
        for case in fixture["cases"]
    ]


@pytest.mark.parametrize(
    "raw_code,expected_code,fixture_name", _derive_error_code_cases()
)
def test_derive_error_code(
    raw_code: str, expected_code: str, fixture_name: str
) -> None:
    assert derive_code(raw_code) == expected_code, (
        f"contract drift in {fixture_name!r}: derive_code({raw_code!r}) "
        f"returned {derive_code(raw_code)!r}, expected {expected_code!r}"
    )


# ----------------------------------------------------------- build_documentation_url


def _docs_url_cases() -> list[tuple[dict[str, Any], str | None, str]]:
    if not FIXTURES_DIR.is_dir():
        return []
    fixture = _load("build-documentation-url.json")
    return [(case["input"], case["expected"], case["name"]) for case in fixture["cases"]]


@pytest.mark.parametrize("inp,expected,case_name", _docs_url_cases())
def test_build_documentation_url(
    inp: dict[str, Any], expected: str | None, case_name: str
) -> None:
    # The fixture inlines a `models` mapping per case; inject it via monkey-patch.
    import runware.errors as errors_mod
    from runware.errors import ModelEntry

    original = errors_mod._bundled_models
    try:
        bundle = {
            air: ModelEntry(task_type=entry["task_type"], id=entry["id"])
            for air, entry in inp.get("models", {}).items()
        }
        errors_mod._bundled_models = bundle
        actual = build_documentation_url(
            inp["task_type"],
            inp["model"],
            inp["parameter"],
            inp["raw_code"],
        )
        assert actual == expected, (
            f"contract drift in {case_name!r}: got {actual!r}, expected {expected!r}"
        )
    finally:
        errors_mod._bundled_models = original


# ----------------------------------------------------------- parse_api_error


def _parse_api_error_cases() -> list[tuple[Any, dict[str, Any], str]]:
    if not FIXTURES_DIR.is_dir():
        return []
    fixture = _load("parse-api-error.json")
    return [
        (case["input"]["raw"], case["expected"], case["name"])
        for case in fixture["cases"]
    ]


@pytest.mark.parametrize("raw,expected,case_name", _parse_api_error_cases())
def test_parse_api_error(raw: Any, expected: dict[str, Any], case_name: str) -> None:
    err = parse_api_error(raw)
    for key, want in expected.items():
        actual = getattr(err, key, None) if key != "message" else err.message
        assert actual == want, (
            f"contract drift in {case_name!r}: field {key!r} was {actual!r}, "
            f"expected {want!r}"
        )
