"""Tests for calling a serverless app."""

from __future__ import annotations

import asyncio
from typing import Any, cast

import aiohttp
import pytest

from runware.errors import RunwareError
from runware.serverless import ServerlessApi
from runware.types.sdk import SDKConfig
from runware.types.serverless import GetTaskOptions, InvokeOptions

from ._mocks import MockResponse, MockSession

ORIGIN = "https://serverless.test.com"
SYNC_URL = f"{ORIGIN}/v1/apps/my-app/invoke-sync/generate"
ASYNC_URL = f"{ORIGIN}/v1/apps/my-app/invoke-async/generate"
TASK_ID = "7c9e6679-7425-40de-944b-e07fc1f90ae7"
TASK_URL = f"{ORIGIN}/v1/apps/my-app/tasks/{TASK_ID}"


def make_config(**overrides: Any) -> SDKConfig:
    settings: dict[str, Any] = {
        "api_key": "test-key",
        "serverless_base_url": ORIGIN,
        "timeout": 5_000,
        "poll_timeout": 5_000,
        "max_retries": 0,
        "retry_delay": 0,
        **overrides,
    }
    return SDKConfig(**settings)


def make_api(session: MockSession, **overrides: Any) -> ServerlessApi:
    async def provider() -> aiohttp.ClientSession:
        return cast("aiohttp.ClientSession", session)

    return ServerlessApi(provider, make_config(**overrides))


def task(**over: Any) -> dict[str, Any]:
    return {
        "id": TASK_ID,
        "status": "completed",
        "appId": "my-app",
        "endpointPath": "generate",
        "output": {"image": "abc"},
        "error": None,
        "createdAt": "2026-09-29T10:00:00Z",
        "completedAt": "2026-09-29T10:00:05Z",
        **over,
    }


def pending(**over: Any) -> dict[str, Any]:
    return task(status="pending", output=None, completedAt=None, **over)


def no_wait() -> InvokeOptions:
    return InvokeOptions(poll_interval=0)


# ------------------------------------------------------------ routes and body


@pytest.mark.asyncio
async def test_posts_to_invoke_async_by_default() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=200, payload=task()))
    api = make_api(session)

    result = await api.invoke("my-app", "generate", {"prompt": "a cat"})

    assert result["output"] == {"image": "abc"}
    assert session.request_log[0].url == ASYNC_URL
    assert session.request_log[0].method == "POST"
    assert session.request_log[0].json_body["payload"] == {"prompt": "a cat"}


@pytest.mark.asyncio
async def test_posts_to_invoke_sync_when_asked() -> None:
    session = MockSession()
    session.add("POST", SYNC_URL, MockResponse(status=200, payload=task()))
    api = make_api(session)

    await api.invoke(
        "my-app", "generate", options=InvokeOptions(delivery_method="sync"),
    )

    assert session.request_log[0].url == SYNC_URL


@pytest.mark.asyncio
async def test_sends_an_empty_payload_when_none_is_given() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=200, payload=task()))
    api = make_api(session)

    await api.invoke("my-app", "generate")

    assert session.request_log[0].json_body["payload"] == {}


@pytest.mark.asyncio
async def test_authenticates_every_call() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=200, payload=task()))
    api = make_api(session)

    await api.invoke("my-app", "generate")

    assert session.request_log[0].headers["Authorization"] == "Bearer test-key"


@pytest.mark.asyncio
async def test_trims_a_trailing_slash_off_the_origin() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=200, payload=task()))
    api = make_api(session, serverless_base_url=f"{ORIGIN}/")

    await api.invoke("my-app", "generate")

    assert session.request_log[0].url == ASYNC_URL


# ------------------------------------------------------------------- task ids


@pytest.mark.asyncio
async def test_generates_a_task_id_when_none_is_given() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=200, payload=task()))
    api = make_api(session)

    await api.invoke("my-app", "generate")

    sent = session.request_log[0].json_body["taskId"]
    assert len(sent) == 36
    assert sent.islower()


@pytest.mark.asyncio
async def test_sends_a_supplied_task_id_unchanged() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=200, payload=task()))
    api = make_api(session)

    await api.invoke("my-app", "generate", task_id=TASK_ID)

    assert session.request_log[0].json_body["taskId"] == TASK_ID


@pytest.mark.asyncio
async def test_rejects_a_task_id_that_is_not_a_uuid() -> None:
    session = MockSession()
    api = make_api(session)

    with pytest.raises(RunwareError, match="lowercase UUID"):
        _ = await api.invoke("my-app", "generate", task_id="nope")
    assert session.request_log == []


# ----------------------------------------------------------- local validation


@pytest.mark.asyncio
async def test_rejects_a_leading_slash_and_suggests_the_bare_path() -> None:
    session = MockSession()
    api = make_api(session)

    with pytest.raises(RunwareError, match=r'without a leading slash \(e\.g\. "generate"\)'):
        _ = await api.invoke("my-app", "/generate")
    assert session.request_log == []


@pytest.mark.asyncio
async def test_rejects_an_endpoint_path_that_is_not_a_bare_segment() -> None:
    api = make_api(MockSession())

    with pytest.raises(RunwareError, match="lowercase segment"):
        _ = await api.invoke("my-app", "Generate Image")


@pytest.mark.asyncio
async def test_rejects_an_app_id_that_cannot_exist() -> None:
    api = make_api(MockSession())

    with pytest.raises(RunwareError, match='app_id "No" is invalid'):
        _ = await api.invoke("No", "generate")


@pytest.mark.asyncio
async def test_names_the_offending_parameter() -> None:
    api = make_api(MockSession())

    with pytest.raises(RunwareError) as excinfo:
        _ = await api.invoke("my-app", "/generate")
    assert excinfo.value.parameter == "endpoint_path"


# ------------------------------------------------------------------- waiting


@pytest.mark.asyncio
async def test_polls_after_a_sync_wait_window_expires_and_never_resubmits() -> None:
    session = MockSession()
    session.add("POST", SYNC_URL, MockResponse(status=202, payload=pending()))
    session.add("GET", TASK_URL, MockResponse(status=200, payload=pending()))
    session.add("GET", TASK_URL, MockResponse(status=200, payload=task()))
    api = make_api(session)

    result = await api.invoke(
        "my-app",
        "generate",
        options=InvokeOptions(delivery_method="sync", poll_interval=0),
    )

    assert result["status"] == "completed"
    assert [entry.method for entry in session.request_log] == ["POST", "GET", "GET"]
    assert session.count("POST", SYNC_URL) == 1


@pytest.mark.asyncio
async def test_polls_under_the_app_the_response_names() -> None:
    other_url = f"{ORIGIN}/v1/apps/other-app/tasks/{TASK_ID}"
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=202, payload=pending(appId="other-app")))
    session.add("GET", other_url, MockResponse(status=200, payload=task(appId="other-app")))
    api = make_api(session)

    await api.invoke("my-app", "generate", options=no_wait())

    assert session.request_log[1].url == other_url


@pytest.mark.asyncio
async def test_returns_the_accepted_task_when_wait_is_false() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=202, payload=pending()))
    api = make_api(session)

    result = await api.invoke(
        "my-app",
        "generate",
        options=InvokeOptions(wait=False),
    )

    assert result["status"] == "pending"
    assert len(session.request_log) == 1


@pytest.mark.asyncio
async def test_wait_false_uses_the_async_route_whatever_was_asked_for() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=202, payload=pending()))
    api = make_api(session)

    result = await api.invoke(
        "my-app",
        "generate",
        options=InvokeOptions(delivery_method="sync", wait=False),
    )

    assert session.request_log[0].url == ASYNC_URL
    assert result["status"] == "pending"
    assert len(session.request_log) == 1


@pytest.mark.asyncio
async def test_returns_a_failed_task_rather_than_raising() -> None:
    session = MockSession()
    session.add(
        "POST",
        ASYNC_URL,
        MockResponse(status=200, payload=task(status="failed", output=None, error="handler raised")),
    )
    api = make_api(session)

    result = await api.invoke("my-app", "generate")

    assert result["status"] == "failed"
    assert result["error"] == "handler raised"


@pytest.mark.asyncio
async def test_retries_a_404_while_the_task_reaches_the_result_store() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=202, payload=pending()))
    session.add(
        "GET",
        TASK_URL,
        MockResponse(status=404, payload={"title": "Not Found", "status": 404}),
    )
    session.add("GET", TASK_URL, MockResponse(status=200, payload=task()))
    api = make_api(session)

    result = await api.invoke("my-app", "generate", options=no_wait())

    assert result["status"] == "completed"
    assert session.count("GET", TASK_URL) == 2


@pytest.mark.asyncio
async def test_gives_up_on_a_task_that_outlives_the_poll_budget() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=202, payload=pending()))
    session.add("GET", TASK_URL, MockResponse(status=200, payload=pending()))
    api = make_api(session, poll_timeout=0)

    with pytest.raises(RunwareError, match=r"still running after 0ms\. It was not cancelled"):
        _ = await api.invoke(
            "my-app",
            "generate",
            options=no_wait(),
        )


@pytest.mark.asyncio
async def test_stops_polling_when_the_cancel_event_is_set() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=202, payload=pending()))
    session.add("GET", TASK_URL, MockResponse(status=200, payload=pending()))
    api = make_api(session)
    cancel = asyncio.Event()

    async def cancel_soon() -> None:
        await asyncio.sleep(0.01)
        cancel.set()

    task_handle = asyncio.create_task(cancel_soon())
    with pytest.raises(RunwareError, match="aborted"):
        _ = await api.invoke(
            "my-app",
            "generate",
            options=InvokeOptions(
                delivery_method="async", poll_interval=0.02, cancel_event=cancel,
            ),
        )
    await task_handle


# --------------------------------------------------------- problem responses


@pytest.mark.asyncio
async def test_maps_a_404_onto_a_not_found_error_with_the_problem_type() -> None:
    session = MockSession()
    session.add(
        "POST",
        ASYNC_URL,
        MockResponse(
            status=404,
            payload={
                "type": "https://docs.runware.ai/serverless/errors#not-found",
                "title": "Not Found",
                "status": 404,
                "detail": "No app 'my-app' exists for the authenticated organization.",
                "requestId": "req-42",
            },
        ),
    )
    api = make_api(session)

    with pytest.raises(RunwareError) as excinfo:
        _ = await api.invoke("my-app", "generate")

    error = excinfo.value
    assert error.code == "notFound"
    assert error.status_code == 404
    assert error.problem_type == "https://docs.runware.ai/serverless/errors#not-found"
    assert error.request_id == "req-42"
    assert "No app 'my-app' exists" in error.message


@pytest.mark.asyncio
async def test_spells_out_the_offending_fields_of_a_422() -> None:
    session = MockSession()
    session.add(
        "POST",
        ASYNC_URL,
        MockResponse(
            status=422,
            payload={
                "title": "Unprocessable Entity",
                "status": 422,
                "detail": "The request body failed validation.",
                "errors": [
                    {"pointer": "/payload/prompt", "detail": "is required"},
                    {"pointer": "/payload/steps", "detail": "must be at most 50"},
                ],
            },
        ),
    )
    api = make_api(session)

    with pytest.raises(RunwareError) as excinfo:
        _ = await api.invoke("my-app", "generate")

    assert "/payload/prompt: is required" in excinfo.value.message
    assert "/payload/steps: must be at most 50" in excinfo.value.message


@pytest.mark.asyncio
async def test_carries_retry_after_off_a_capacity_refusal() -> None:
    session = MockSession()
    session.add(
        "POST",
        ASYNC_URL,
        MockResponse(
            status=503,
            headers={"Retry-After": "30"},
            payload={
                "type": "https://docs.runware.ai/serverless/errors#capacity-unavailable",
                "title": "Service Unavailable",
                "status": 503,
            },
        ),
    )
    api = make_api(session)

    with pytest.raises(RunwareError) as excinfo:
        _ = await api.invoke("my-app", "generate")

    assert excinfo.value.retry_after == 30
    assert "capacity-unavailable" in (excinfo.value.problem_type or "")


@pytest.mark.asyncio
async def test_falls_back_to_the_status_when_the_body_is_not_a_problem() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=500, payload=None))
    api = make_api(session)

    with pytest.raises(RunwareError) as excinfo:
        _ = await api.invoke("my-app", "generate")

    assert excinfo.value.code == "serverError"
    assert excinfo.value.message == "HTTP 500"


@pytest.mark.asyncio
async def test_maps_401_onto_an_auth_error() -> None:
    session = MockSession()
    session.add(
        "POST",
        ASYNC_URL,
        MockResponse(status=401, payload={"title": "Unauthorized", "status": 401}),
    )
    api = make_api(session)

    with pytest.raises(RunwareError) as excinfo:
        _ = await api.invoke("my-app", "generate")

    assert excinfo.value.code == "auth"


# ------------------------------------------------------------------- retries


@pytest.mark.asyncio
async def test_retries_a_retryable_status_with_the_same_task_id() -> None:
    session = MockSession()
    session.add("POST", ASYNC_URL, MockResponse(status=500, payload={"status": 500}))
    session.add("POST", ASYNC_URL, MockResponse(status=200, payload=task()))
    api = make_api(session, max_retries=2)

    result = await api.invoke("my-app", "generate", task_id=TASK_ID)

    assert result["status"] == "completed"
    assert session.count("POST", ASYNC_URL) == 2
    sent = [entry.json_body["taskId"] for entry in session.request_log]
    assert sent == [TASK_ID, TASK_ID]


@pytest.mark.asyncio
async def test_does_not_retry_a_request_the_app_refused() -> None:
    session = MockSession()
    session.add(
        "POST",
        ASYNC_URL,
        MockResponse(status=409, payload={"status": 409, "detail": "App is stopped."}),
    )
    session.add("POST", ASYNC_URL, MockResponse(status=200, payload=task()))
    api = make_api(session, max_retries=2)

    with pytest.raises(RunwareError, match="App is stopped"):
        _ = await api.invoke("my-app", "generate")

    assert session.count("POST", ASYNC_URL) == 1


# ------------------------------------------------------------------ get_task


@pytest.mark.asyncio
async def test_get_task_reads_one_task_by_id() -> None:
    session = MockSession()
    session.add("GET", TASK_URL, MockResponse(status=200, payload=task()))
    api = make_api(session)

    result = await api.get_task("my-app", TASK_ID)

    assert result["status"] == "completed"
    assert session.request_log[0].method == "GET"


@pytest.mark.asyncio
async def test_get_task_rejects_an_id_that_is_not_a_uuid() -> None:
    session = MockSession()
    api = make_api(session)

    with pytest.raises(RunwareError, match="lowercase UUID"):
        _ = await api.get_task("my-app", "nope")
    assert session.request_log == []


@pytest.mark.asyncio
async def test_get_task_honors_a_per_call_timeout_option() -> None:
    session = MockSession()
    session.add("GET", TASK_URL, MockResponse(status=200, payload=task()))
    api = make_api(session)

    result = await api.get_task("my-app", TASK_ID, GetTaskOptions(timeout=1_000))

    assert result["id"] == TASK_ID
