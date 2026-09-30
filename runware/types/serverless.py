"""Types for calling a serverless app."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any, Literal, TypedDict

TaskStatus = Literal["pending", "completed", "failed"]
"""Lifecycle of a serverless task. ``pending`` is the only non-terminal state."""

DeliveryMethod = Literal["sync", "async"]
"""
How the caller waits for a task.

- ``async`` takes an acknowledgement and polls. No connection is held, which
  is what long jobs want and what survives a dropped connection.
- ``sync`` holds the request open until the task is terminal, one round trip.
  Best-effort: a task that outlives the platform wait window comes back
  accepted rather than failed, and the SDK polls it from there. The fast path
  for work that finishes in seconds.

Both return the finished task. The default is ``async``, the same default
``run`` takes and for the same reason.
"""


class ServerlessTask(TypedDict):
    """
    A serverless task, as both invoke routes and ``get_task`` return it.

    ``output`` and ``completedAt`` are set once ``status`` is ``completed``;
    ``error`` is set once it is ``failed``. While ``pending``, none of the
    three are.
    """

    id: str
    status: TaskStatus
    appId: str
    endpointPath: str
    output: Any  # pyright: ignore[reportExplicitAny]
    error: str | None
    createdAt: str
    completedAt: str | None


@dataclass
class InvokeOptions:
    """Per-call options for ``client.invoke()``."""

    delivery_method: DeliveryMethod = "async"
    """How to wait for the task. Ignored when ``wait`` is ``False``."""

    wait: bool = True
    """
    Whether to return the finished task.

    Set ``False`` to return as soon as the task is accepted, leaving it to run.
    Read the id off the returned task and poll ``get_task`` when you want it.

    The task goes on the ``async`` route, which is already the default, so this
    only overrides an explicit ``delivery_method="sync"``. A ``sync``
    invocation always waits, because holding a request open for a result
    nobody is going to read has nothing to offer.
    """

    poll_interval: float | None = None
    """Seconds between polls while waiting. Default: 2."""

    poll_timeout: int | None = None
    """
    End-to-end budget in ms, measured from the start of the call rather than
    from the first poll, so a long ``sync`` wait counts against it. Falls back
    to ``config.poll_timeout``. Giving up leaves the task running: poll
    ``get_task`` to pick it back up.
    """

    timeout: int | None = None
    """
    Per-request timeout in ms for one HTTP call. Falls back to
    ``config.timeout``. A ``sync`` invocation raises it to at least five
    minutes so the platform's own wait window decides the outcome rather than
    the client giving up first.
    """

    cancel_event: asyncio.Event | None = None
    """Set it to abort the call, and any polling it is doing."""


@dataclass
class GetTaskOptions:
    """Per-call options for ``client.get_task()``."""

    timeout: int | None = None
    cancel_event: asyncio.Event | None = None
