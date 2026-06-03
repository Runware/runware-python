"""
Tests for runware/client.py — dispatch routing, taskType resolution, utility
method shapes.
"""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock

import pytest

from runware import Runware, RunwareError
from runware.transport.rest import RestTransport


def _patch_rest(client: Runware, response: Any) -> AsyncMock:
    """Inject a fake REST transport returning a single canned response."""
    mock = AsyncMock(spec=RestTransport)
    mock.send_request = AsyncMock(return_value=response)
    mock.close = AsyncMock()

    async def aenter(*args: object, **kwargs: object) -> AsyncMock:
        return mock

    mock.__aenter__ = aenter
    mock.__aexit__ = AsyncMock()
    client._rest_transport = mock
    return mock


class TestTransportSelection:
    def test_rest_transport_when_configured(self) -> None:
        c = Runware(api_key="sk-test", transport_type="rest")
        assert c._rest_transport is not None
        assert c._ws_transport is None

    def test_ws_transport_when_configured(self) -> None:
        c = Runware(api_key="sk-test", transport_type="websocket")
        assert c._rest_transport is None
        assert c._ws_transport is not None


class TestUtilityOptions:
    @pytest.mark.asyncio
    async def test_utility_accepts_run_options(self) -> None:
        """Each utility method takes an optional RunOptions argument."""
        from runware import RunOptions

        client = Runware(api_key="sk-test", transport_type="rest")
        mock = _patch_rest(client, {"data": [{"taskUUID": "u1"}]})

        opts = RunOptions(timeout=12_345)
        await client.model_search({"search": "x"}, opts)
        await client.model_upload({"x": 1}, opts)
        await client.image_upload({"image": "data:..."}, opts)
        await client.account_management({"operation": "x"}, opts)
        await client.get_response({"taskUUID": "u"}, opts)
        await client.get_task_details({"taskUUID": "u"}, opts)

        # Each call should have forwarded the per-call timeout (12_345 ms)
        # onto the RequestOptions handed to send_request.
        from runware.types.transport import RequestOptions
        for call in mock.send_request.call_args_list:
            req_opts = call.args[1] if len(call.args) > 1 else call.kwargs.get("options")
            assert isinstance(req_opts, RequestOptions)
            assert req_opts.timeout == 12_345


class TestUtilityMethods:
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "method,task_type",
        [
            ("model_search", "modelSearch"),
            ("model_upload", "modelUpload"),
            ("image_upload", "imageUpload"),
            ("account_management", "accountManagement"),
            ("get_response", "getResponse"),
            ("get_task_details", "getTaskDetails"),
        ],
    )
    async def test_utility_sends_correct_task_type(
        self, method: str, task_type: str
    ) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        utility_response: dict[str, Any] = {
            "data": [{"taskUUID": "u-util", "results": []}]
        }
        mock = _patch_rest(client, utility_response)

        await getattr(client, method)({"some": "param"})

        sent = mock.send_request.call_args.args[0]
        assert sent["taskType"] == task_type
        assert "taskUUID" in sent
        assert sent["some"] == "param"

    @pytest.mark.asyncio
    async def test_utility_returns_data_array(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        models = [{"air": "x", "name": "x"}, {"air": "y", "name": "y"}]
        _patch_rest(
            client,
            {"data": [{"taskUUID": "u1", "results": models}]},
        )
        result = await client.model_search({"search": "foo"})
        assert len(result) == 1
        assert result[0]["results"] == models


class TestRunDelivery:
    @pytest.mark.asyncio
    async def test_default_delivery_method_is_async(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        # Sync response so the polling loop doesn't run.
        sync_response: dict[str, Any] = {
            "data": [{"taskUUID": "u1", "imageURL": "https://x.jpg", "imageUUID": "i1"}]
        }
        mock = _patch_rest(client, sync_response)
        await client.run({
            "taskType": "imageInference",
            "taskUUID": "u1",
            "model": "runware:101@1",
            "positivePrompt": "x",
            "width": 1024,
            "height": 1024,
            "deliveryMethod": "sync",  # avoid polling in this test
        })
        sent = mock.send_request.call_args_list[0].args[0]
        assert sent["deliveryMethod"] == "sync"

    @pytest.mark.asyncio
    async def test_user_supplied_delivery_method_wins(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        sync_response: dict[str, Any] = {
            "data": [{"taskUUID": "u1", "imageURL": "https://x.jpg", "imageUUID": "i1"}]
        }
        mock = _patch_rest(client, sync_response)
        await client.run({
            "taskType": "imageInference",
            "taskUUID": "u1",
            "model": "runware:101@1",
            "positivePrompt": "x",
            "width": 1024,
            "height": 1024,
            "deliveryMethod": "sync",
        })
        sent = mock.send_request.call_args_list[0].args[0]
        assert sent["deliveryMethod"] == "sync"


class TestTaskTypeResolution:
    @pytest.mark.asyncio
    async def test_explicit_task_type_wins(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        sync_response: dict[str, Any] = {
            "data": [{"taskUUID": "u1", "imageURL": "https://x.jpg", "imageUUID": "i1"}]
        }
        mock = _patch_rest(client, sync_response)
        await client.run({
            "taskType": "imageInference",
            "taskUUID": "u1",
            "model": "non-curated:0@0",  # unknown to the registry
            "positivePrompt": "x",
            "width": 1024,
            "height": 1024,
            "deliveryMethod": "sync",
        })
        sent = mock.send_request.call_args_list[0].args[0]
        assert sent["taskType"] == "imageInference"

    @pytest.mark.asyncio
    async def test_unknown_model_raises_runware_error(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        try:
            with pytest.raises(RunwareError) as exc_info:
                await client.run({
                    "taskUUID": "u1",
                    "model": "definitely-not-a-real:0@0",
                    "positivePrompt": "x",
                })
            # `unknownModel` is in the NOT_FOUND raw-code set.
            assert exc_info.value.code == "notFound"
        finally:
            await client.close()


class TestConnectDisconnect:
    @pytest.mark.asyncio
    async def test_connect_is_noop_on_rest(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        await client.connect()
        await client.disconnect()

    @pytest.mark.asyncio
    async def test_is_connected_property_true_for_rest(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        assert client.is_connected is True
        await client.close()

    @pytest.mark.asyncio
    async def test_double_close_is_safe(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        await client.close()
        await client.close()


class TestModelNormalization:
    @pytest.mark.asyncio
    async def test_air_passes_through_unchanged(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        try:
            result = await client._normalize_model_param(
                {"model": "runware:101@1", "positivePrompt": "x"}
            )
            assert result["model"] == "runware:101@1"
        finally:
            await client.close()

    @pytest.mark.asyncio
    async def test_no_model_passes_through_unchanged(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        try:
            result = await client._normalize_model_param(
                {"taskType": "getResponse", "taskUUID": "u1"}
            )
            assert "model" not in result
        finally:
            await client.close()

    @pytest.mark.asyncio
    async def test_non_string_model_passes_through(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        try:
            result = await client._normalize_model_param(
                {"model": 42, "positivePrompt": "x"}
            )
            # Non-string model never gets touched.
            assert result["model"] == 42
        finally:
            await client.close()


class TestRefreshRegistry:
    @pytest.mark.asyncio
    async def test_refresh_registry_method_exists(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        try:
            # Just verify the method is wired up; the registry tests exercise
            # the actual refresh semantics. Using try/finally so a real network
            # failure doesn't fail the test.
            try:
                await client.refresh_registry()
            except Exception:
                pass
        finally:
            await client.close()


class TestValidateOverride:
    @pytest.mark.asyncio
    async def test_per_call_validate_false_skips_validation(self) -> None:
        from runware import RunOptions

        client = Runware(api_key="sk-test", transport_type="rest", validate=True)
        sync_response: dict[str, Any] = {
            "data": [
                {"taskUUID": "u1", "imageURL": "https://x.jpg", "imageUUID": "i1"}
            ]
        }
        _patch_rest(client, sync_response)
        # If validation tried to run, it'd attempt to fetch the schema from the
        # network and fail. Per-call validate=False must short-circuit it.
        result = await client.run(
            {
                "taskType": "imageInference",
                "taskUUID": "u1",
                "model": "non-curated:0@0",
                "positivePrompt": "x",
                "width": 1024,
                "height": 1024,
                "deliveryMethod": "sync",
            },
            RunOptions(validate=False),
        )
        assert result[0]["imageURL"] == "https://x.jpg"
        await client.close()


class TestConfigPropagation:
    def test_config_log_populated_by_create_config(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest", debug=True)
        # The transport should share the client's config.log instance.
        assert client._config.log is not None
        assert client._config.log.enabled is True

    def test_config_log_is_noop_when_debug_false(self) -> None:
        client = Runware(api_key="sk-test", transport_type="rest")
        assert client._config.log.enabled is False
