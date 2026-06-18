"""Tests for the errors module — pure logic, mirrors test/errors.test.ts patterns."""

from __future__ import annotations

import pytest

from runware import RunwareError, is_runware_error
from runware.errors import (
    build_documentation_url,
    create_runware_error,
    derive_code,
    is_retryable,
    parse_api_error,
)


class TestDeriveCode:
    @pytest.mark.parametrize(
        "raw, expected",
        [
            ("aborted", "aborted"),
            ("connectionFailed", "connection"),
            ("notConnected", "connection"),
            ("notOpen", "connection"),
            ("reconnectionFailed", "connection"),
            ("disconnected", "connection"),
            ("insufficientCredits", "quota"),
            ("quotaExceeded", "quota"),
            ("paymentRequired", "quota"),
            ("rateLimitExceeded", "rateLimit"),
            ("contentPolicyViolation", "safety"),
            ("nsfwContentDetected", "safety"),
            ("unauthorized", "auth"),
            ("invalidApiKey", "auth"),
            ("requestTimeout", "timeout"),
            ("timeout", "timeout"),
            ("taskFailedOrNotFound", "notFound"),
            ("modelNotFound", "notFound"),
            ("tokenExpired", "auth"),
            ("internalServerError", "serverError"),
            ("providerInternalError", "provider"),
            ("inferenceError", "provider"),
            ("invalidModel", "validation"),
            ("missingParameter", "validation"),
            ("validationFailed", "validation"),
            ("somethingNeverSeenBefore", "unknown"),
        ],
    )
    def test_known_codes(self, raw: str, expected: str) -> None:
        assert derive_code(raw) == expected


class TestIsRetryable:
    def test_retryable_categories(self) -> None:
        for code in ("provider", "timeout", "connection", "rateLimit", "serverError"):
            assert is_retryable(code) is True  # type: ignore[arg-type]

    def test_non_retryable_categories(self) -> None:
        for code in ("validation", "auth", "quota", "safety", "notFound", "aborted", "unknown"):
            assert is_retryable(code) is False  # type: ignore[arg-type]


class TestRunwareError:
    def test_is_exception(self) -> None:
        err = RunwareError("invalidModel", "bad")
        assert isinstance(err, Exception)

    def test_message_attribute(self) -> None:
        err = RunwareError("invalidModel", "bad model")
        assert err.message == "bad model"

    def test_code_derived(self) -> None:
        assert RunwareError("invalidModel", "bad").code == "validation"
        assert RunwareError("internalServerError", "boom").code == "serverError"

    def test_retryable_flag_matches_code(self) -> None:
        assert RunwareError("timeout", "x").retryable is True
        assert RunwareError("invalidModel", "x").retryable is False

    def test_is_runware_error_type_guard(self) -> None:
        assert is_runware_error(RunwareError("invalidModel", "x")) is True
        assert is_runware_error(ValueError("not a runware error")) is False
        assert is_runware_error("string") is False


class TestCreateRunwareError:
    def test_populates_fields(self) -> None:
        err = create_runware_error(
            "invalidModel",
            "bad model",
            parameter="model",
            task_type="imageInference",
            task_uuid="abc",
            status_code=400,
        )
        assert err.code == "validation"
        assert err.parameter == "model"
        assert err.task_type == "imageInference"
        assert err.task_uuid == "abc"
        assert err.status_code == 400

    def test_validation_errors_only_attached_when_code_validation(self) -> None:
        err = create_runware_error(
            "invalidModel", "bad", validation_errors=[{"path": "/model"}]
        )
        assert err.validation_errors == [{"path": "/model"}]

        err2 = create_runware_error(
            "internalServerError", "boom", validation_errors=[{"path": "/x"}]
        )
        assert err2.validation_errors is None

    def test_documentation_url_for_curated_model(self, monkeypatch: pytest.MonkeyPatch) -> None:
        # Inject a known curated model into the generated bundle for this test.
        from runware.errors import ModelEntry, _bundled_models
        monkeypatch.setitem(
            _bundled_models, "runware:101@1", ModelEntry(task_type="imageInference", id="flux-1-dev")
        )
        err = create_runware_error(
            "invalidParameter",
            "bad",
            parameter="positivePrompt",
            model="runware:101@1",
        )
        assert err.documentation == (
            "https://runware.ai/docs/models/flux-1-dev#request-positiveprompt"
        )

    def test_documentation_url_for_utility_task(self) -> None:
        err = create_runware_error(
            "invalidParameter",
            "bad",
            parameter="search",
            task_type="modelSearch",
        )
        assert err.documentation == (
            "https://runware.ai/docs/platform/model-search#request-search"
        )

    def test_documentation_url_for_sdk_only_raw_code(self) -> None:
        err = create_runware_error("noFetchImpl", "no fetch")
        assert err.documentation == "https://runware.ai/docs/platform/errors"


class TestParseApiError:
    def test_parses_single_object(self) -> None:
        err = parse_api_error(
            {"code": "invalidParameter", "message": "bad", "parameter": "width"}
        )
        assert err.code == "validation"
        assert err.parameter == "width"
        assert err.message == "bad"

    def test_parses_errors_array(self) -> None:
        err = parse_api_error(
            {"errors": [{"code": "invalidApiKey", "message": "no auth"}]}
        )
        assert err.code == "auth"
        assert err.message == "no auth"

    def test_parses_pre_stream_error_envelope(self) -> None:
        err = parse_api_error(
            {
                "error": {"code": "rateLimitExceeded", "message": "slow down"},
                "taskUUID": "u1",
                "taskType": "imageInference",
            },
            task_type="imageInference",
        )
        assert err.code == "rateLimit"
        assert err.task_uuid == "u1"
        assert err.task_type == "imageInference"

    def test_context_task_type_fallback(self) -> None:
        err = parse_api_error(
            {"code": "invalidParameter", "message": "bad"},
            task_type="imageInference",
        )
        assert err.task_type == "imageInference"

    def test_string_input_falls_back_to_unknown(self) -> None:
        err = parse_api_error("just a string")
        assert err.code == "unknown"
        assert err.message == "just a string"


class TestBuildDocumentationUrl:
    def test_returns_none_when_no_signals(self) -> None:
        assert build_documentation_url(None, None, None, "somethingRandom") is None

    def test_models_fallback_when_model_set_but_unknown(self) -> None:
        url = build_documentation_url(None, "civitai:1@1", None, "invalidParameter")
        assert url == "https://runware.ai/docs/models"

    def test_param_anchor_lowercases_and_dot_to_hyphen(self) -> None:
        url = build_documentation_url(
            "modelSearch", None, "filters.category", "invalidParameter"
        )
        assert url == (
            "https://runware.ai/docs/platform/model-search#request-filters-category"
        )
