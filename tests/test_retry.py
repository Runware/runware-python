"""Tests for runware/utils/retry.py — backoff, should_retry gating, callbacks."""

from __future__ import annotations

import asyncio

import pytest

from runware import RunwareError
from runware.utils.retry import with_retry


class TestSuccess:
    @pytest.mark.asyncio
    async def test_returns_immediately_on_success(self) -> None:
        calls = 0

        async def fn() -> str:
            nonlocal calls
            calls += 1
            return "result"

        result = await with_retry(
            fn,
            max_retries=3,
            retry_delay_ms=0,
            retry_strategy="exponential",
            should_retry=lambda _: True,
        )
        assert result == "result"
        assert calls == 1


class TestRetryGating:
    @pytest.mark.asyncio
    async def test_does_not_retry_when_should_retry_returns_false(self) -> None:
        calls = 0

        async def fn() -> str:
            nonlocal calls
            calls += 1
            raise RuntimeError("nope")

        with pytest.raises(RuntimeError, match="nope"):
            await with_retry(
                fn,
                max_retries=3,
                retry_delay_ms=0,
                retry_strategy="exponential",
                should_retry=lambda _: False,
            )
        assert calls == 1

    @pytest.mark.asyncio
    async def test_retries_up_to_max_retries(self) -> None:
        calls = 0

        async def fn() -> str:
            nonlocal calls
            calls += 1
            raise RuntimeError("transient")

        with pytest.raises(RuntimeError, match="transient"):
            await with_retry(
                fn,
                max_retries=2,
                retry_delay_ms=0,
                retry_strategy="linear",
                should_retry=lambda _: True,
            )
        # 1 initial + 2 retries
        assert calls == 3

    @pytest.mark.asyncio
    async def test_succeeds_after_initial_failure(self) -> None:
        calls = 0

        async def fn() -> str:
            nonlocal calls
            calls += 1
            if calls == 1:
                raise RuntimeError("first fail")
            return "ok"

        result = await with_retry(
            fn,
            max_retries=2,
            retry_delay_ms=0,
            retry_strategy="linear",
            should_retry=lambda _: True,
        )
        assert result == "ok"
        assert calls == 2


class TestOnRetryCallback:
    @pytest.mark.asyncio
    async def test_called_once_per_retry(self) -> None:
        retries: list[tuple[int, int]] = []
        calls = 0

        async def fn() -> str:
            nonlocal calls
            calls += 1
            if calls < 3:
                raise RuntimeError(f"fail {calls}")
            return "ok"

        await with_retry(
            fn,
            max_retries=3,
            retry_delay_ms=0,
            retry_strategy="linear",
            should_retry=lambda _: True,
            on_retry=lambda _exc, attempt, delay_ms: retries.append((attempt, delay_ms)),
        )
        # Two failures → two on_retry calls (after fail 1, after fail 2).
        assert len(retries) == 2
        assert [r[0] for r in retries] == [1, 2]


class TestBackoffSchedule:
    @pytest.mark.asyncio
    async def test_linear_grows_by_attempt(self) -> None:
        delays: list[int] = []
        calls = 0

        async def fn() -> str:
            nonlocal calls
            calls += 1
            raise RuntimeError("nope")

        with pytest.raises(RuntimeError):
            await with_retry(
                fn,
                max_retries=3,
                retry_delay_ms=1_000,
                retry_strategy="linear",
                should_retry=lambda _: True,
                on_retry=lambda _e, _a, d: delays.append(d),
            )
        # Jitter is 0-1000ms on top of the base. So:
        # attempt 1: 1000 + jitter ∈ [1000, 2000]
        # attempt 2: 2000 + jitter ∈ [2000, 3000]
        # attempt 3: 3000 + jitter ∈ [3000, 4000]
        assert 1000 <= delays[0] <= 2000
        assert 2000 <= delays[1] <= 3000
        assert 3000 <= delays[2] <= 4000

    @pytest.mark.asyncio
    async def test_exponential_doubles_capped_at_30s(self) -> None:
        delays: list[int] = []
        calls = 0

        async def fn() -> str:
            nonlocal calls
            calls += 1
            raise RuntimeError("nope")

        with pytest.raises(RuntimeError):
            await with_retry(
                fn,
                max_retries=6,
                retry_delay_ms=1_000,
                retry_strategy="exponential",
                should_retry=lambda _: True,
                on_retry=lambda _e, _a, d: delays.append(d),
            )
        # attempt 1: 1000  + jitter
        # attempt 2: 2000  + jitter
        # attempt 3: 4000  + jitter
        # attempt 4: 8000  + jitter
        # attempt 5: 16000 + jitter
        # attempt 6: capped at 30000 + jitter
        assert delays[0] < delays[1] < delays[2] < delays[3] < delays[4]
        assert delays[5] <= 31_000


class TestCancellation:
    @pytest.mark.asyncio
    async def test_pre_attempt_cancel_raises_aborted(self) -> None:
        cancel = asyncio.Event()
        cancel.set()

        async def fn() -> str:
            return "never reached"

        with pytest.raises(RunwareError) as exc_info:
            await with_retry(
                fn,
                max_retries=2,
                retry_delay_ms=0,
                retry_strategy="linear",
                should_retry=lambda _: True,
                cancel_event=cancel,
            )
        assert exc_info.value.code == "aborted"

    @pytest.mark.asyncio
    async def test_cancel_during_backoff_raises_aborted(self) -> None:
        cancel = asyncio.Event()
        calls = 0

        async def fn() -> str:
            nonlocal calls
            calls += 1
            if calls == 1:
                # Schedule the cancel for the upcoming backoff sleep.
                loop = asyncio.get_running_loop()
                loop.call_later(0.05, cancel.set)
            raise RuntimeError("fail")

        with pytest.raises(RunwareError) as exc_info:
            await with_retry(
                fn,
                max_retries=5,
                retry_delay_ms=2_000,
                retry_strategy="linear",
                should_retry=lambda _: True,
                cancel_event=cancel,
            )
        assert exc_info.value.code == "aborted"
        # Only the first attempt ran — the cancel fired during the backoff sleep.
        assert calls == 1
