"""Tests for the config module — defaults, env fallback, validation, DI."""

from __future__ import annotations

import math

import aiohttp
import pytest

from runware import RuntimeDependencies, RunwareError, SDKConfig, is_runware_error
from runware.config import create_config


class TestDefaults:
    def test_minimal_config_with_explicit_key(self) -> None:
        cfg = create_config(api_key="sk-test")
        assert cfg.api_key == "sk-test"
        assert cfg.transport == "websocket"
        assert cfg.http_base_url == "https://api.runware.ai/v1"
        assert cfg.ws_base_url == "wss://ws-api.runware.ai/v1"
        assert cfg.timeout == 1_200_000
        assert cfg.poll_timeout == 1_200_000
        assert cfg.auth_timeout == 15_000
        assert cfg.max_retries == 3
        assert cfg.retry_delay == 1_000
        assert cfg.retry_strategy == "exponential"
        assert math.isinf(cfg.max_reconnect_attempts)
        assert cfg.debug is False
        assert cfg.validate is False
        assert cfg.dependencies is None


class TestEnvFallback:
    def test_reads_api_key_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("RUNWARE_API_KEY", "sk-env-fallback")
        cfg = create_config()
        assert cfg.api_key == "sk-env-fallback"

    def test_explicit_overrides_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("RUNWARE_API_KEY", "sk-env")
        cfg = create_config(api_key="sk-explicit")
        assert cfg.api_key == "sk-explicit"

    def test_missing_key_raises_runware_error(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.delenv("RUNWARE_API_KEY", raising=False)
        with pytest.raises(RunwareError) as exc_info:
            create_config()
        assert is_runware_error(exc_info.value)


class TestOverrides:
    def test_user_supplied_fields_replace_defaults(self) -> None:
        cfg = create_config(
            api_key="sk-test",
            transport="rest",
            http_base_url="https://example.com/v2",
            timeout=5_000,
            max_retries=0,
            debug=True,
        )
        assert cfg.transport == "rest"
        assert cfg.http_base_url == "https://example.com/v2"
        assert cfg.timeout == 5_000
        assert cfg.max_retries == 0
        assert cfg.debug is True

    def test_unknown_field_raises(self) -> None:
        with pytest.raises(RunwareError) as exc_info:
            create_config(api_key="sk-test", unknownField=42)  # type: ignore[arg-type]
        assert "Unknown SDKConfig field" in exc_info.value.message


class TestDependencyInjection:
    def test_accepts_runtime_dependencies(self) -> None:
        deps = RuntimeDependencies()
        cfg = create_config(api_key="sk-test", dependencies=deps)
        assert cfg.dependencies is deps

    @pytest.mark.asyncio
    async def test_accepts_injected_session(self) -> None:
        session = aiohttp.ClientSession()
        try:
            cfg = create_config(
                api_key="sk-test",
                dependencies=RuntimeDependencies(session=session),
            )
            assert cfg.dependencies is not None
            assert cfg.dependencies.session is session
        finally:
            await session.close()

    @pytest.mark.asyncio
    async def test_accepts_custom_ws_connect(self) -> None:
        async def fake_connect(uri: str) -> object:
            raise NotImplementedError("never called in this test")

        cfg = create_config(
            api_key="sk-test",
            # fake_connect returns `object`, the protocol expects a
            # WebSocketClientProtocol. The test only verifies that the SDK
            # *stores* what's given; behavior under it is not exercised here.
            dependencies=RuntimeDependencies(
                ws_connect=fake_connect,  # pyright: ignore[reportArgumentType]
            ),
        )
        assert cfg.dependencies is not None
        assert cfg.dependencies.ws_connect is fake_connect


class TestConfigIsSDKConfig:
    def test_returns_dataclass_instance(self) -> None:
        cfg = create_config(api_key="sk-test")
        assert isinstance(cfg, SDKConfig)
