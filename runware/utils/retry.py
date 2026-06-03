"""Retry helper with linear/exponential backoff + jitter, cancellation-aware."""

from __future__ import annotations

import asyncio
import random
from collections.abc import Awaitable, Callable
from typing import TypeVar

from ..errors import create_runware_error
from ..types.sdk import RetryStrategy

T = TypeVar("T")


async def with_retry(
    fn: Callable[[], Awaitable[T]],
    *,
    max_retries: int,
    retry_delay_ms: int,
    retry_strategy: RetryStrategy,
    should_retry: Callable[[BaseException], bool],
    cancel_event: asyncio.Event | None = None,
    on_retry: Callable[[BaseException, int, int], None] | None = None,
) -> T:
    """
    Run `fn` with retry on exceptions matching `should_retry`.

    Delay schedule (ms):
      linear      : retry_delay_ms * attempt
      exponential : retry_delay_ms * 2 ** (attempt - 1), capped at 30_000, + jitter

    Honors `cancel_event` between attempts and during the backoff sleep.
    """
    attempt = 0
    last_exc: BaseException | None = None

    while True:
        if cancel_event is not None and cancel_event.is_set():
            raise create_runware_error("aborted", "Request aborted")
        try:
            return await fn()
        except BaseException as exc:
            last_exc = exc
            if not should_retry(exc):
                raise
            if attempt >= max_retries:
                raise

            attempt += 1
            if retry_strategy == "linear":
                delay_ms = retry_delay_ms * attempt
            else:
                delay_ms = min(retry_delay_ms * (2 ** (attempt - 1)), 30_000)
            delay_ms += random.randint(0, 1_000)

            if on_retry is not None:
                on_retry(exc, attempt, delay_ms)

            try:
                await _interruptible_sleep(delay_ms / 1000.0, cancel_event)
            except asyncio.CancelledError:
                raise create_runware_error("aborted", "Request aborted") from last_exc


async def _interruptible_sleep(seconds: float, cancel_event: asyncio.Event | None) -> None:
    if cancel_event is None:
        await asyncio.sleep(seconds)
        return

    sleep_task = asyncio.create_task(asyncio.sleep(seconds))
    cancel_task = asyncio.create_task(cancel_event.wait())
    try:
        done, pending = await asyncio.wait(
            {sleep_task, cancel_task}, return_when=asyncio.FIRST_COMPLETED
        )
        for task in pending:
            task.cancel()
        if cancel_task in done:
            raise create_runware_error("aborted", "Request aborted")
    except asyncio.CancelledError:
        sleep_task.cancel()
        cancel_task.cancel()
        raise
