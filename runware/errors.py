"""
Runware error model.

All errors raised by the SDK are instances of `RunwareError`, with a stable
`code` attribute users can switch on. The raw server-side identifier is
intentionally not exposed — the backend error catalog is large and unstable;
users get `code` (a small enum), `parameter`, and `message`.
"""

from __future__ import annotations

from typing import Literal, TypeGuard, cast

from typing_extensions import override

from ._docs_cache import get_docs_url_for_model as _cached_docs
from .types.task_map import ModelEntry
from .types.task_map import models as _bundled_models

ErrorCode = Literal[
    "validation",
    "auth",
    "quota",
    "rateLimit",
    "safety",
    "provider",
    "timeout",
    "notFound",
    "serverError",
    "connection",
    "aborted",
    "unknown",
]

_DOCS_BASE = "https://runware.ai/docs"

_UTILITY_DOC_PATHS: dict[str, str] = {
    "modelSearch": "platform/model-search",
    "modelUpload": "platform/model-upload",
    "imageUpload": "platform/image-upload",
    "getResponse": "platform/get-response",
    "accountManagement": "platform/account-management",
}

_SDK_ERROR_DOC_PATH = "getting-started/errors"

_SDK_ONLY_RAW_CODES: set[str] = {
    "aborted",
    "unknownModel",
    "noFetchImpl",
    "noWebSocketImpl",
    "streamUnsupported",
    "notConnected",
    "notOpen",
    "reconnectionFailed",
    "sendFailed",
    "connectionFailed",
    "missingApiKey",
    "parseError",
}

_SAFETY_CODES: set[str] = {
    "contentPolicyViolation",
    "providerContentPolicyViolation",
    "sensitiveContentDetected",
    "unsafeContentDetected",
    "nsfwContentDetected",
    "promptBlocked",
    "imageBlocked",
    "moderationFailed",
}

_AUTH_CODES: set[str] = {
    "unauthorized",
    "forbidden",
    "permissionDenied",
    "insufficientPermissions",
    "authenticationFailed",
    "authFailed",
    "authTimeout",
    "invalidAuthentication",
    "invalidCredentials",
    "missingAuthentication",
    "tokenExpired",
    "tokenInvalid",
    "tokenMissing",
    "tokenRevoked",
    "accountSuspended",
    "accountDisabled",
    "organizationSuspended",
    "organizationDisabled",
    "workspaceSuspended",
    "workspaceDisabled",
}

_SERVER_ERROR_CODES: set[str] = {
    "internalServerError",
    "serviceUnavailable",
    "serverUnavailable",
    "standardError",
    "unknownError",
    "undefinedError",
    "defaultError",
    "unrecognizedResponse",
    "errorRetrievingAccountManagement",
}

_NOT_FOUND_CODES: set[str] = {
    "taskCancelled",
    "taskFailedOrNotFound",
    "unknownModel",
}

_PROVIDER_CODES: set[str] = {
    "inferenceError",
    "processingFailed",
    "taskFailed",
    "downloadFailed",
    "uploadFailed",
    "noAvailableServer",
    "modelUnavailable",
    "modelDisabled",
    "modelNotReady",
    "mediaStorageFileCouldNotBeMoved",
}

_RETRYABLE_CODES: set[ErrorCode] = {
    "provider",
    "timeout",
    "connection",
    "rateLimit",
    "serverError",
}


def is_retryable(code: ErrorCode) -> bool:
    """Return True if retrying a request that produced this error code might succeed."""
    return code in _RETRYABLE_CODES


def derive_code(raw: str) -> ErrorCode:
    """
    Map a raw server-side or SDK-internal identifier to the stable error code enum.

    The raw codes from the backend are not part of the public API surface.
    They can change at any time. Users should switch on `RunwareError.code`.
    """
    if raw == "aborted":
        return "aborted"
    if raw in ("connectionFailed", "notConnected", "notOpen", "reconnectionFailed"):
        return "connection"

    if (
        "Credits" in raw
        or "Quota" in raw
        or "Balance" in raw
        or raw == "quotaExceeded"
        or raw == "paymentRequired"
    ):
        return "quota"
    if "RateLimit" in raw or raw == "rateLimitExceeded":
        return "rateLimit"

    if raw in _SAFETY_CODES:
        return "safety"

    if raw in _AUTH_CODES or "ApiKey" in raw:
        return "auth"

    if "Timeout" in raw or raw == "timeout":
        return "timeout"

    if raw in _NOT_FOUND_CODES or raw.endswith("NotFound") or raw.endswith("Expired"):
        return "notFound"

    if raw in _SERVER_ERROR_CODES:
        return "serverError"

    # Provider auth = upstream provider's keys/auth, not the user's. Treat as
    # provider-level rather than user-facing auth failure.
    if raw in _PROVIDER_CODES or raw.startswith("provider"):
        return "provider"

    # Validation catch-all for request-shape problems.
    if (
        raw.startswith("invalid")
        or raw.startswith("missing")
        or raw.startswith("conflict")
        or raw.startswith("duplicate")
        or raw.startswith("unsupported")
        or raw.startswith("value")
        or raw.startswith("array")
        or raw == "unknownParameter"
        or raw == "incompatibleParameters"
        or raw == "mismatchProviderSettingsProvider"
        or raw == "unknownProviderSettingsProvider"
        or raw == "transparentModelMismatch"
        or raw == "modelOwnershipValidationError"
        or raw == "modelAlreadyExists"
        or raw.startswith("max")
        or raw == "validationFailed"
    ):
        return "validation"

    return "unknown"


class RunwareError(Exception):
    """
    Exception raised for all SDK errors.

    Attributes:
        code: Stable category for this error. Use this for switch/if statements.
        retryable: True if retrying the same request might succeed.
        parameter: The request parameter related to the error, if applicable.
        task_type: The task type of the request that failed.
        task_uuid: The unique identifier of the failed request.
        documentation: Link to relevant documentation.
        status_code: HTTP status code, when the error originated from an HTTP response.
        validation_errors: Structured per-field errors (only when code == "validation"
            and the failure was raised by the opt-in client-side validator).
    """

    code: ErrorCode
    retryable: bool
    parameter: str | None
    task_type: str | None
    task_uuid: str | None
    documentation: str | None
    status_code: int | None
    validation_errors: list[object] | None

    def __init__(self, raw_code: str, message: str) -> None:
        super().__init__(message)
        self.code = derive_code(raw_code)
        self.retryable = is_retryable(self.code)
        self.parameter = None
        self.task_type = None
        self.task_uuid = None
        self.documentation = None
        self.status_code = None
        self.validation_errors = None

    @property
    def message(self) -> str:
        """The human-readable error message."""
        return self.args[0] if self.args else ""

    @override
    def __repr__(self) -> str:
        bits = [f"code={self.code!r}"]
        if self.parameter:
            bits.append(f"parameter={self.parameter!r}")
        if self.task_type:
            bits.append(f"task_type={self.task_type!r}")
        if self.status_code is not None:
            bits.append(f"status_code={self.status_code!r}")
        bits.append(f"message={self.message!r}")
        return f"RunwareError({', '.join(bits)})"


def _param_anchor(parameter: str) -> str:
    return "#request-" + parameter.replace(".", "-").lower()


def build_documentation_url(
    task_type: str | None,
    model: str | None,
    parameter: str | None,
    raw_code: str,
    *,
    cached_docs_for_model: str | None = None,
) -> str | None:
    """
    Derive a documentation URL for an error.

    Looks up curated models in the generated `models` dict; falls back to the
    docs URL cached by validate.py for non-curated models (when validate=True
    ran for them). The cached-docs lookup is performed automatically — callers
    only need to pass `cached_docs_for_model` to override the auto-lookup.
    """
    if model:
        entry: ModelEntry | None = _bundled_models.get(model)
        if entry is not None:
            base = f"{_DOCS_BASE}/models/{entry.id}"
            return f"{base}{_param_anchor(parameter)}" if parameter else base

    if model:
        # Auto-pickup of validator-cached docs for non-curated models. The
        # cache lives in its own `_docs_cache` module so neither side of the
        # erstwhile errors↔validate cycle imports the other.
        if cached_docs_for_model is None:
            cached_docs_for_model = _cached_docs(model)
        if cached_docs_for_model:
            return (
                f"{cached_docs_for_model}{_param_anchor(parameter)}"
                if parameter
                else cached_docs_for_model
            )

    if task_type and task_type in _UTILITY_DOC_PATHS:
        base = f"{_DOCS_BASE}/{_UTILITY_DOC_PATHS[task_type]}"
        return f"{base}{_param_anchor(parameter)}" if parameter else base

    if raw_code in _SDK_ONLY_RAW_CODES:
        return f"{_DOCS_BASE}/{_SDK_ERROR_DOC_PATH}"

    if model:
        return f"{_DOCS_BASE}/models"

    return None


def create_runware_error(
    raw_code: str,
    message: str,
    *,
    parameter: str | None = None,
    task_type: str | None = None,
    task_uuid: str | None = None,
    status_code: int | None = None,
    validation_errors: list[object] | None = None,
    model: str | None = None,
    cached_docs_for_model: str | None = None,
) -> RunwareError:
    """Construct a RunwareError with optional context fields filled in."""
    error = RunwareError(raw_code, message)
    if parameter:
        error.parameter = parameter
    if task_type:
        error.task_type = task_type
    if task_uuid:
        error.task_uuid = task_uuid
    if status_code is not None:
        error.status_code = status_code
    if validation_errors is not None and error.code == "validation":
        error.validation_errors = validation_errors

    url = build_documentation_url(
        error.task_type,
        model,
        error.parameter,
        raw_code,
        cached_docs_for_model=cached_docs_for_model,
    )
    if url:
        error.documentation = url

    return error


def parse_api_error(
    raw: object,
    *,
    task_type: str | None = None,
    model: str | None = None,
) -> RunwareError:
    """
    Parse a server error response into a RunwareError.

    Accepts the various shapes the API can return: a single error dict, a list
    of errors, an `errors` envelope, or a `{ error: {...}, taskUUID, taskType }`
    envelope from pre-stream HTTP errors.
    """
    if not isinstance(raw, (dict, list)):
        return create_runware_error("unknown", str(raw))

    first: dict[str, object] = {}

    if isinstance(raw, list):
        raw_list = cast(list[object], raw)
        if raw_list and isinstance(raw_list[0], dict):
            first = cast(dict[str, object], raw_list[0])
    else:
        obj = cast(dict[str, object], raw)
        errors_val = obj.get("errors")
        error_val = obj.get("error")
        if isinstance(errors_val, list):
            errors_list = cast(list[object], errors_val)
            if errors_list and isinstance(errors_list[0], dict):
                first = cast(dict[str, object], errors_list[0])
        elif isinstance(error_val, dict):
            err = dict(cast(dict[str, object], error_val))
            err.setdefault("taskUUID", obj.get("taskUUID"))
            err.setdefault("taskType", obj.get("taskType"))
            first = err
        else:
            first = obj

    return create_runware_error(
        _str_or_default(first.get("code"), "unknown"),
        _str_or_default(first.get("message"), "An unknown API error occurred"),
        parameter=_str_or_none(first.get("parameter")),
        task_type=_str_or_none(first.get("taskType")) or task_type,
        task_uuid=_str_or_none(first.get("taskUUID")),
        model=_str_or_none(first.get("model")) or model,
    )


def _str_or_none(value: object) -> str | None:
    return value if isinstance(value, str) else None


def _str_or_default(value: object, default: str) -> str:
    return value if isinstance(value, str) else default


def is_runware_error(error: object) -> TypeGuard[RunwareError]:
    """Type guard for RunwareError."""
    return isinstance(error, RunwareError)
