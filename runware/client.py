"""Runware async client."""

from __future__ import annotations

import asyncio
import contextlib
import time
import uuid
from typing import Any, Self, cast, overload

import aiohttp

from .config import create_config
from .constants import SCHEMAS_BASE_URL
from .errors import create_runware_error, parse_api_error
from .registry import Registry, RegistryData, create_registry
from .stream import TextStream, create_text_stream
from .transport.rest import RestTransport
from .transport.websocket import WebSocketTransport
from .types.sdk import LoosePayload, RunOptions, SDKConfig, StreamOptions
from .types.task_map import (
    AccountManagementParams,
    AccountManagementResult,
    AudioInferenceParams,
    AudioInferenceResult,
    CaptionImageParams,
    CaptionParams,
    CaptionResult,
    CaptionVideoParams,
    ControlnetPreprocessParams,
    ControlNetPreprocessResult,
    GetResponseParams,
    GetResponseResult,
    GetTaskDetailsParams,
    GetTaskDetailsResult,
    ImageInferenceParams,
    ImageInferenceResult,
    ImageMaskingResult,
    ImageUploadParams,
    ImageUploadResult,
    MaskingParams,
    ModelSearchParams,
    ModelSearchResult,
    ModelUploadParams,
    ModelUploadResult,
    PromptEnhanceParams,
    PromptEnhanceResult,
    RemoveBackgroundImageParams,
    RemoveBackgroundParams,
    RemoveBackgroundResult,
    RemoveBackgroundVideoParams,
    TextInferenceParams,
    TextInferenceResult,
    ThreeDInferenceParams,
    ThreeDInferenceResult,
    TrainingParams,
    TrainingResult,
    UpscaleImageParams,
    UpscaleParams,
    UpscaleResult,
    UpscaleVideoParams,
    VectorizeParams,
    VectorizeResult,
    VideoInferenceParams,
    VideoInferenceResult,
)
from .types.task_map import (
    architecture_task_types as _bundled_arch_task_types,
)
from .types.task_map import (
    modality_task_types as _bundled_modality_task_types,
)
from .types.task_map import (
    models as _bundled_models,
)
from .types.task_map import (
    operation_task_types as _bundled_operation_task_types,
)
from .types.transport import RequestOptions, WireFrame
from .validate import validate_tasks


class Runware:
    """Async Runware client. Use as a context manager or call `close()` manually."""

    def __init__(self, *, api_key: str | None = None, **config_overrides: object) -> None:
        self._config: SDKConfig = create_config(api_key=api_key, **config_overrides)
        injected_session = (
            self._config.dependencies.session if self._config.dependencies else None
        )
        self._registry: Registry = create_registry(
            url=f"{SCHEMAS_BASE_URL}/registry.json",
            log=self._config.log,
            fallback=_build_registry_fallback(),
            session=injected_session,
        )
        # Reused for both validate `/resolve` calls and SSE streaming. Pull from
        # injected dependencies if available; otherwise create lazily.
        self._validation_session: aiohttp.ClientSession | None = injected_session
        self._owns_validation_session: bool = injected_session is None

        self._rest_transport: RestTransport | None = None
        self._ws_transport: WebSocketTransport | None = None
        if self._config.transport_type == "websocket":
            self._ws_transport = WebSocketTransport(self._config)
        else:
            self._rest_transport = RestTransport(self._config)

        # Tracks in-flight TextStream pumps so close() can abort them cleanly
        # instead of having them surface opaque ClientConnectorError when the
        # session is yanked from underneath. Lazily created when needed so the
        # event is bound to the current event loop.
        self._active_streams: set[TextStream] = set()
        self._closed: bool = False

    async def __aenter__(self) -> Self:
        await self.connect()
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.close()

    async def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        # Abort any in-flight streams first so they raise a clean `aborted`
        # error instead of an opaque ClientConnectorError when the validation
        # session closes underneath them.
        for stream in list(self._active_streams):
            stream._signal_shutdown()  # pyright: ignore[reportPrivateUsage]
        if self._rest_transport is not None:
            await self._rest_transport.close()
        if self._ws_transport is not None:
            await self._ws_transport.disconnect()
        if (
            self._owns_validation_session
            and self._validation_session is not None
        ):
            await self._validation_session.close()
            self._validation_session = None
        await self._registry.close()

    async def connect(self) -> None:
        """Open the underlying transport. No-op on REST."""
        if self._rest_transport is not None:
            await self._rest_transport.__aenter__()
        if self._ws_transport is not None:
            await self._ws_transport.connect()

    async def disconnect(self) -> None:
        """Close the underlying transport."""
        await self.close()

    @property
    def is_connected(self) -> bool:
        if self._ws_transport is not None:
            return self._ws_transport.is_connected
        return True

    async def refresh_registry(self) -> None:
        await self._registry.refresh()

    # ----------------------------------------------------------- run / stream

    # ---- Overloads narrow the return type when params is annotated with one
    # of the canonical TypedDicts. Untyped dicts fall through to the last
    # overload and get the loose `list[LoosePayload]` return.

    # Modalities (5)
    @overload
    async def run(
        self, params: ImageInferenceParams, options: RunOptions | None = None,
    ) -> list[ImageInferenceResult]: ...
    @overload
    async def run(
        self, params: VideoInferenceParams, options: RunOptions | None = None,
    ) -> list[VideoInferenceResult]: ...
    @overload
    async def run(
        self, params: AudioInferenceParams, options: RunOptions | None = None,
    ) -> list[AudioInferenceResult]: ...
    @overload
    async def run(
        self, params: TextInferenceParams, options: RunOptions | None = None,
    ) -> list[TextInferenceResult]: ...
    @overload
    async def run(
        self, params: ThreeDInferenceParams, options: RunOptions | None = None,
    ) -> list[ThreeDInferenceResult]: ...

    # Operations — slug variants collapse to one canonical Result per taskType.
    @overload
    async def run(
        self,
        params: CaptionParams | CaptionImageParams | CaptionVideoParams,
        options: RunOptions | None = None,
    ) -> list[CaptionResult]: ...
    @overload
    async def run(
        self,
        params: UpscaleParams | UpscaleImageParams | UpscaleVideoParams,
        options: RunOptions | None = None,
    ) -> list[UpscaleResult]: ...
    @overload
    async def run(
        self,
        params: (
            RemoveBackgroundParams
            | RemoveBackgroundImageParams
            | RemoveBackgroundVideoParams
        ),
        options: RunOptions | None = None,
    ) -> list[RemoveBackgroundResult]: ...
    @overload
    async def run(
        self, params: MaskingParams, options: RunOptions | None = None,
    ) -> list[ImageMaskingResult]: ...
    @overload
    async def run(
        self, params: ControlnetPreprocessParams, options: RunOptions | None = None,
    ) -> list[ControlNetPreprocessResult]: ...
    @overload
    async def run(
        self, params: PromptEnhanceParams, options: RunOptions | None = None,
    ) -> list[PromptEnhanceResult]: ...
    @overload
    async def run(
        self, params: VectorizeParams, options: RunOptions | None = None,
    ) -> list[VectorizeResult]: ...
    @overload
    async def run(
        self, params: TrainingParams, options: RunOptions | None = None,
    ) -> list[TrainingResult]: ...

    # Fallback for untyped dicts.
    @overload
    async def run(
        self,
        params: dict[str, Any],  # pyright: ignore[reportExplicitAny]
        options: RunOptions | None = None,
    ) -> list[dict[str, Any]]: ...  # pyright: ignore[reportExplicitAny]

    async def run(  # pyright: ignore[reportInconsistentOverload]
        self,
        params: dict[str, Any],  # pyright: ignore[reportExplicitAny]
        options: RunOptions | None = None,
    ) -> list[dict[str, Any]]:  # pyright: ignore[reportExplicitAny]
        """Run an inference task."""
        params = await self._normalize_model_param(params)
        task_type = await self._resolve_task_type(params)
        task_uuid = str(params.get("taskUUID") or uuid.uuid4())
        expected_count = max(int(params.get("numberResults") or 1), 1)
        # Default to 'async' on both transports, matching the TS SDK. Users
        # can opt into 'sync' explicitly for wire-level single-roundtrip delivery
        # (server holds the response open instead of ACK + polling).
        delivery_method = params.get("deliveryMethod") or "async"

        # Pass-through of user-supplied params: values are inherently Any
        # because the request shape is per-taskType. Server-side schemas
        # and the optional `validate=True` path do the actual checking.
        wire_task: LoosePayload = {
            k: v
            for k, v in params.items()  # pyright: ignore[reportAny]
            if k not in ("taskType", "taskUUID")
        }
        wire_task["taskType"] = task_type
        wire_task["taskUUID"] = task_uuid
        wire_task["deliveryMethod"] = delivery_method

        await self._maybe_validate([wire_task], options)

        if self._ws_transport is not None:
            return await self._run_over_ws(
                wire_task=wire_task,
                expected_count=expected_count,
                delivery_method=delivery_method,
                options=options,
            )

        assert self._rest_transport is not None
        return await self._run_over_rest(
            wire_task=wire_task,
            task_type=task_type,
            task_uuid=task_uuid,
            expected_count=expected_count,
            delivery_method=delivery_method,
            options=options,
        )

    async def stream(
        self,
        params: LoosePayload,
        options: StreamOptions | None = None,
    ) -> TextStream:
        """Stream LLM text via SSE. Forces the REST/SSE path regardless of transport."""
        if isinstance(params.get("numberResults"), int) and params["numberResults"] > 1:
            raise create_runware_error(
                "notImplemented",
                (
                    "stream() with numberResults > 1 is not supported "
                    "(the backend doesn't emit resultIndex on stream chunks)."
                ),
            )
        params = await self._normalize_model_param(params)
        task_type = await self._resolve_task_type(params)
        # User-supplied passthrough: values are Any by the same per-taskType reasoning.
        wire_task: LoosePayload = {
            k: v
            for k, v in params.items()  # pyright: ignore[reportAny]
            if k not in ("taskType",)
        }
        wire_task["taskType"] = task_type
        wire_task["deliveryMethod"] = "stream"
        wire_task.setdefault("taskUUID", str(uuid.uuid4()))

        await self._maybe_validate([wire_task], options)

        timeout_seconds: float | None = None
        if options is not None and options.timeout is not None:
            timeout_seconds = options.timeout / 1000.0

        session = await self._ensure_validation_session()
        stream = await create_text_stream(
            config=self._config,
            session=session,
            params=wire_task,
            cancel_event=options.cancel_event if options else None,
            timeout_seconds=timeout_seconds,
        )
        # Track for shutdown. Stream removes itself when its pump completes.
        self._active_streams.add(stream)
        stream._set_on_finish(  # pyright: ignore[reportPrivateUsage]
            lambda: self._active_streams.discard(stream)
        )
        return stream

    # ----------------------------------------------------------- utility methods

    async def model_search(
        self, params: ModelSearchParams, options: RunOptions | None = None,
    ) -> list[ModelSearchResult]:
        return cast(
            list[ModelSearchResult],
            await self._utility("modelSearch", dict(params), options),
        )

    async def model_upload(
        self, params: ModelUploadParams, options: RunOptions | None = None,
    ) -> list[ModelUploadResult]:
        return cast(
            list[ModelUploadResult],
            await self._utility("modelUpload", dict(params), options),
        )

    async def image_upload(
        self, params: ImageUploadParams, options: RunOptions | None = None,
    ) -> list[ImageUploadResult]:
        return cast(
            list[ImageUploadResult],
            await self._utility("imageUpload", dict(params), options),
        )

    async def account_management(
        self,
        params: AccountManagementParams,
        options: RunOptions | None = None,
    ) -> list[AccountManagementResult]:
        return cast(
            list[AccountManagementResult],
            await self._utility("accountManagement", dict(params), options),
        )

    async def get_response(
        self, params: GetResponseParams, options: RunOptions | None = None,
    ) -> list[GetResponseResult]:
        return cast(
            list[GetResponseResult],
            await self._utility("getResponse", dict(params), options),
        )

    async def get_task_details(
        self, params: GetTaskDetailsParams, options: RunOptions | None = None,
    ) -> list[GetTaskDetailsResult]:
        return cast(
            list[GetTaskDetailsResult],
            await self._utility("getTaskDetails", dict(params), options),
        )

    # ----------------------------------------------------------- internal

    async def _utility(
        self,
        task_type: str,
        params: LoosePayload,
        options: RunOptions | None = None,
    ) -> list[LoosePayload]:
        # User-supplied passthrough: values are Any by the same per-taskType reasoning.
        wire_task: LoosePayload = {
            k: v
            for k, v in params.items()  # pyright: ignore[reportAny]
            if k not in ("taskType", "taskUUID")
        }
        wire_task["taskType"] = task_type
        wire_task["taskUUID"] = str(params.get("taskUUID") or uuid.uuid4())

        if self._ws_transport is not None:
            timeout_seconds = (
                (options.timeout if options else None) or self._config.timeout
            ) / 1000.0
            # Utility responses don't carry inference-result markers
            # (imageURL/videoURL/etc.), so the inference-style terminal check
            # never fires. Treat the first data frame as the full result.
            return await self._ws_send_and_collect(
                wire_task=wire_task,
                task_uuid=wire_task["taskUUID"],
                expected_count=1,
                timeout_seconds=timeout_seconds,
                options=options,
                any_item_is_terminal=True,
            )

        assert self._rest_transport is not None
        request_options = RequestOptions(
            timeout=options.timeout if options else None,
            cancel_event=options.cancel_event if options else None,
        )
        response = await self._rest_transport.send_request(wire_task, request_options)
        return _extract_items(response)

    async def _resolve_task_type(self, params: LoosePayload) -> str:
        explicit = params.get("taskType")
        if isinstance(explicit, str) and explicit:
            return explicit
        model = params.get("model")
        if isinstance(model, str):
            resolved = await self._registry.get_model_task_type(model)
            if resolved:
                return resolved
        raise create_runware_error(
            "unknownModel",
            (
                f"Unknown model {params.get('model')!r}. Pass `taskType=...` explicitly "
                "or call refresh_registry() if this is a recently launched model."
            ),
            parameter="taskType",
        )

    async def _normalize_model_param(self, params: LoosePayload) -> LoosePayload:
        """
        If the user passed a curated-model slug (e.g. ``flux-1-dev``) instead
        of an AIR (e.g. ``runware:101@1``), swap it for the canonical AIR
        before sending — the server only knows the AIR form. Non-curated
        models, fine-tune AIRs, and unknown identifiers pass through.
        """
        model = params.get("model")
        if not isinstance(model, str):
            return params
        # AIR-shaped? Skip the registry lookup. This is the hot path.
        if ":" in model and "@" in model:
            return params
        air = await self._registry.resolve_model_air(model)
        if not air or air == model:
            return params
        return {**params, "model": air}

    async def _maybe_validate(
        self,
        tasks: list[LoosePayload],
        options: RunOptions | StreamOptions | None,
    ) -> None:
        per_call = options.validate if options is not None else None
        enabled = per_call if per_call is not None else self._config.validate
        if not enabled:
            return
        session = await self._ensure_validation_session()
        await validate_tasks(tasks, log=self._config.log, session=session)

    async def _ensure_validation_session(self) -> aiohttp.ClientSession:
        if self._validation_session is None or self._validation_session.closed:
            self._validation_session = aiohttp.ClientSession()
            self._owns_validation_session = True
        return self._validation_session

    # ----------------------------------------------------------- REST path

    async def _run_over_rest(
        self,
        *,
        wire_task: LoosePayload,
        task_type: str,
        task_uuid: str,
        expected_count: int,
        delivery_method: str,
        options: RunOptions | None,
    ) -> list[LoosePayload]:
        assert self._rest_transport is not None
        request_options = RequestOptions(
            timeout=options.timeout if options else None,
            cancel_event=options.cancel_event if options else None,
        )
        response = await self._rest_transport.send_request(wire_task, request_options)

        if delivery_method == "sync":
            items = _extract_items(response)
            # Use the collector so per-item errors fire callbacks and raise,
            # matching the async-polling and WS paths.
            collector = _AsyncCollector(
                expected_count, options, any_item_is_terminal=False,
            )
            collector.ingest(items)
            _maybe_raise_item_errors(
                collector, task_type=task_type, task_uuid=task_uuid,
            )
            return items

        return await self._poll_rest(
            task_type=task_type,
            task_uuid=task_uuid,
            expected_count=expected_count,
            initial_response=response,
            options=options,
        )

    async def _poll_rest(
        self,
        *,
        task_type: str,
        task_uuid: str,
        expected_count: int,
        initial_response: WireFrame,
        options: RunOptions | None,
    ) -> list[LoosePayload]:
        assert self._rest_transport is not None
        cancel_event = options.cancel_event if options else None
        poll_timeout_seconds = (
            (options.timeout if options else None) or self._config.poll_timeout
        ) / 1000.0

        collector = _AsyncCollector(expected_count, options)
        collector.ingest(_extract_items(initial_response))
        _maybe_raise_item_errors(collector, task_type=task_type, task_uuid=task_uuid)
        if collector.done():
            return collector.sorted_results()

        start = time.monotonic()
        delay = 1.0
        poll_number = 0

        while not collector.done():
            if cancel_event is not None and cancel_event.is_set():
                raise create_runware_error("aborted", "Request aborted during polling")
            elapsed = time.monotonic() - start
            if elapsed >= poll_timeout_seconds:
                raise create_runware_error(
                    "timeout",
                    (
                        f"Polling for task {task_uuid} (taskType={task_type}) "
                        f"timed out after {elapsed:.0f}s"
                    ),
                )

            await _interruptible_sleep(delay, cancel_event)

            poll_payload: LoosePayload = {
                "taskType": "getResponse",
                "taskUUID": task_uuid,
            }
            # Cap each inner POST at whichever is smaller: the remaining poll
            # budget or the transport's per-call timeout. Without this, a hung
            # `getResponse` can sit on the 20-min transport default and outrun
            # the outer poll_timeout we're trying to enforce here.
            remaining_ms = int(
                max(poll_timeout_seconds - (time.monotonic() - start), 0) * 1000,
            )
            inner_timeout = min(remaining_ms, self._config.timeout) or None
            poll_response = await self._rest_transport.send_request(
                poll_payload,
                RequestOptions(timeout=inner_timeout, cancel_event=cancel_event),
            )
            collector.ingest(_extract_items(poll_response))
            _maybe_raise_item_errors(
                collector, task_type=task_type, task_uuid=task_uuid
            )
            poll_number += 1
            delay = _next_poll_delay(poll_number, delay)

        return collector.sorted_results()

    # ----------------------------------------------------------- WebSocket path

    async def _run_over_ws(
        self,
        *,
        wire_task: LoosePayload,
        expected_count: int,
        delivery_method: str,
        options: RunOptions | None,
    ) -> list[LoosePayload]:
        timeout_seconds = (
            (options.timeout if options else None) or self._config.timeout
        ) / 1000.0
        # wire_task is LoosePayload so wire_task["taskUUID"] is Any. Narrow
        # at the call boundary — callers above already populated taskUUID with
        # a str, so this is sound.
        task_uuid = cast(str, wire_task["taskUUID"])
        if delivery_method == "async":
            poll_timeout_seconds = (
                (options.timeout if options else None) or self._config.poll_timeout
            ) / 1000.0
            return await self._ws_run_async(
                wire_task=wire_task,
                task_uuid=task_uuid,
                expected_count=expected_count,
                poll_timeout_seconds=poll_timeout_seconds,
                options=options,
            )
        return await self._ws_send_and_collect(
            wire_task=wire_task,
            task_uuid=task_uuid,
            expected_count=expected_count,
            timeout_seconds=timeout_seconds,
            options=options,
        )

    async def _ws_run_async(
        self,
        *,
        wire_task: LoosePayload,
        task_uuid: str,
        expected_count: int,
        poll_timeout_seconds: float,
        options: RunOptions | None,
    ) -> list[LoosePayload]:
        """
        Two-phase WS async: subscribe, send original task, wait for ACK, then
        poll getResponse over the same socket until each expected item arrives.

        Both the original task's ACK frame and subsequent getResponse poll
        responses arrive on the same subscription (keyed by the original
        taskUUID, which getResponse echoes back).
        """
        assert self._ws_transport is not None
        if not self._ws_transport.is_connected:
            await self._ws_transport.connect()

        cancel_event = options.cancel_event if options else None
        loop = asyncio.get_running_loop()

        ack_future: asyncio.Future[None] = loop.create_future()
        terminal_error: LoosePayload = {"err": None}
        poll_wake = asyncio.Event()
        collector = _AsyncCollector(expected_count, options)

        def on_frame(response: WireFrame) -> None:
            errors_raw = response.get("error") or response.get("errors")
            if errors_raw:
                err_list: list[object] = (
                    cast(list[object], errors_raw)
                    if isinstance(errors_raw, list)
                    else [errors_raw]
                )
                err = parse_api_error(
                    {"errors": err_list},
                    task_type=cast(str | None, wire_task.get("taskType")),
                    model=cast(str | None, wire_task.get("model")),
                )
                if not err.task_uuid:
                    err.task_uuid = task_uuid
                if not ack_future.done():
                    ack_future.set_exception(err)
                else:
                    terminal_error["err"] = err
                    poll_wake.set()
                return

            data = response.get("data")
            items: list[LoosePayload] = (
                [
                    cast(LoosePayload, item)
                    for item in cast(list[object], data)
                    if isinstance(item, dict)
                ]
                if isinstance(data, list)
                else []
            )
            if not ack_future.done():
                # First frame doubles as ACK — also ingest any data the server
                # may have eagerly returned in the same frame.
                ack_future.set_result(None)
                if items:
                    collector.ingest(items)
                if collector.done():
                    poll_wake.set()
                return

            if items:
                collector.ingest(items)
            poll_wake.set()

        self._ws_transport.subscribe_to_task(task_uuid, on_frame)

        try:
            await self._ws_transport.send_request(wire_task)

            ack_timeout_seconds = 30.0
            try:
                await asyncio.wait_for(ack_future, timeout=ack_timeout_seconds)
            except TimeoutError as exc:
                raise create_runware_error(
                    "timeout",
                    (
                        f"ACK not received for task {task_uuid} after "
                        f"{ack_timeout_seconds:.0f}s"
                    ),
                ) from exc

            _maybe_raise_item_errors(
                collector,
                task_type=cast(str | None, wire_task.get("taskType")),
                task_uuid=task_uuid,
            )

            if collector.done():
                return collector.sorted_results()

            start = time.monotonic()
            delay = 1.0
            poll_number = 0

            while not collector.done():
                if cancel_event is not None and cancel_event.is_set():
                    raise create_runware_error(
                        "aborted", "Request aborted during polling"
                    )
                elapsed = time.monotonic() - start
                if elapsed >= poll_timeout_seconds:
                    raise create_runware_error(
                        "timeout",
                        (
                            f"Polling for task {task_uuid} timed out after "
                            f"{elapsed:.0f}s"
                        ),
                    )

                await _interruptible_sleep(delay, cancel_event)
                poll_wake.clear()

                poll_payload: LoosePayload = {
                    "taskType": "getResponse",
                    "taskUUID": task_uuid,
                }
                await self._ws_transport.send_request(poll_payload)

                # Wait briefly for poll response. If the server doesn't reply,
                # we still want to bound the loop iteration so we re-check
                # cancel / timeout regularly.
                with contextlib.suppress(TimeoutError):
                    await asyncio.wait_for(poll_wake.wait(), timeout=delay + 5.0)

                if terminal_error["err"] is not None:
                    raise terminal_error["err"]

                _maybe_raise_item_errors(
                    collector,
                    task_type=cast(str | None, wire_task.get("taskType")),
                    task_uuid=task_uuid,
                )

                poll_number += 1
                delay = _next_poll_delay(poll_number, delay)

            return collector.sorted_results()
        finally:
            self._ws_transport.unsubscribe_from_task(task_uuid)

    async def _ws_send_and_collect(
        self,
        *,
        wire_task: LoosePayload,
        task_uuid: str,
        expected_count: int,
        timeout_seconds: float,
        options: RunOptions | None,
        any_item_is_terminal: bool = False,
    ) -> list[LoosePayload]:
        assert self._ws_transport is not None
        if not self._ws_transport.is_connected:
            await self._ws_transport.connect()

        loop = asyncio.get_running_loop()
        future: asyncio.Future[list[LoosePayload]] = loop.create_future()
        collector = _AsyncCollector(
            expected_count, options, any_item_is_terminal=any_item_is_terminal
        )

        def on_frame(response: WireFrame) -> None:
            if future.done():
                return
            errors = response.get("error") or response.get("errors")
            if errors:
                err_list: list[object] = (
                    cast(list[object], errors) if isinstance(errors, list) else [errors]
                )
                first: LoosePayload = (
                    cast(LoosePayload, err_list[0])
                    if err_list and isinstance(err_list[0], dict)
                    else {}
                )
                err = parse_api_error(
                    {"errors": err_list},
                    task_type=cast(str | None, wire_task.get("taskType")),
                    model=cast(str | None, wire_task.get("model")),
                )
                if not err.task_uuid:
                    err.task_uuid = first.get("taskUUID") or task_uuid
                future.set_exception(err)
                return
            items_raw: object = response.get("data")
            if isinstance(items_raw, list):
                collector.ingest(cast(list[LoosePayload], items_raw))
                # Per-item errors (`status: error`) terminate the call. Fire
                # callbacks BEFORE rejecting so partial successes are visible.
                item_errors = collector.take_errors()
                if item_errors:
                    flattened_errors: list[LoosePayload] = [
                        {**(e.get("error") or {}), "taskUUID": e.get("taskUUID") or task_uuid}
                        for e in item_errors
                    ]
                    err = parse_api_error(
                        {"errors": flattened_errors},
                        task_type=cast(str | None, wire_task.get("taskType")),
                        model=cast(str | None, wire_task.get("model")),
                    )
                    if not err.task_uuid:
                        err.task_uuid = task_uuid
                    future.set_exception(err)
                    return
            if collector.done():
                future.set_result(collector.sorted_results())

        self._ws_transport.subscribe_to_task(task_uuid, on_frame)

        try:
            await self._ws_transport.send_request(wire_task)
        except Exception:
            self._ws_transport.unsubscribe_from_task(task_uuid)
            raise

        cancel_event = options.cancel_event if options else None
        try:
            return await asyncio.wait_for(
                _await_with_cancel(future, cancel_event),
                timeout=timeout_seconds,
            )
        except TimeoutError as exc:
            raise create_runware_error(
                "timeout",
                f"WebSocket task {task_uuid} timed out after {timeout_seconds:.0f}s",
            ) from exc
        finally:
            self._ws_transport.unsubscribe_from_task(task_uuid)


# ----------------------------------------------------------------- helpers

class _AsyncCollector:
    """Per-task result collector with deduplication by resultIndex."""

    # Per-item stable identifiers the server returns on terminal items, in
    # priority order. The first one present wins; if none are present we fall
    # back to a monotonic anonymous slot.
    _STABLE_ID_KEYS: tuple[str, ...] = (
        "imageUUID",
        "videoUUID",
        "audioUUID",
        "modelUUID",
        "taskUUID",
    )

    def __init__(
        self,
        expected_count: int,
        options: RunOptions | None,
        *,
        any_item_is_terminal: bool = False,
    ) -> None:
        self._expected = expected_count
        self._options = options
        self._any_item_is_terminal = any_item_is_terminal
        self._results: dict[str | int, LoosePayload] = {}
        self._seen_progress: dict[str | int, float] = {}
        self._seen_terminal: set[str | int] = set()
        # Per-item errors accumulated across `ingest()` calls. Drained by the
        # caller via `take_errors()`. Mirrors TS executeRest/executeWebSocketAsync
        # — error items fire on_result first, then the call rejects.
        self._errors: list[LoosePayload] = []
        # Fallback counter for terminal items that don't carry any stable id
        # field — preserves ordering so the result list isn't shuffled.
        self._next_anon_slot: int = 0

    def take_errors(self) -> list[LoosePayload]:
        """Return and clear any per-item errors seen since the last call."""
        errs, self._errors = self._errors, []
        return errs

    def _safe_on_result(self, item: LoosePayload) -> None:
        if self._options is None or self._options.on_result is None:
            return
        with contextlib.suppress(Exception):  # user callback throws don't kill polling
            self._options.on_result(item)

    def _safe_on_progress(self, item: LoosePayload) -> None:
        if self._options is None or self._options.on_progress is None:
            return
        with contextlib.suppress(Exception):
            self._options.on_progress(item)

    def ingest(self, items: list[LoosePayload]) -> None:
        for item in items:
            # An error item (status='error') is terminal — fire on_result for
            # it so the user sees the partial outcome, record the error for the
            # caller to raise, but do NOT add it to `_results` (which only
            # holds successes the caller eventually returns).
            if item.get("status") == "error":
                key = self._stable_id(item)
                if key is None:
                    key = self._next_anon_slot
                    self._next_anon_slot += 1
                if key in self._seen_terminal:
                    continue
                self._seen_terminal.add(key)
                self._errors.append(item)
                self._safe_on_result(item)
                continue

            is_terminal = self._any_item_is_terminal or _is_terminal(item)
            if is_terminal:
                key = self._stable_id(item)
                if key is None:
                    key = self._next_anon_slot
                    self._next_anon_slot += 1
                if key in self._seen_terminal:
                    # REST polling returns cumulative state on every poll;
                    # re-seeing the same UUID is expected and must not produce
                    # a duplicate entry.
                    continue
                self._seen_terminal.add(key)
                self._results[key] = item
                self._safe_on_result(item)
            else:
                progress_key: str | int | None = self._stable_id(item)
                if progress_key is None:
                    raw_idx = item.get("resultIndex")
                    progress_key = raw_idx if isinstance(raw_idx, int) else -1
                progress = _progress_value(item)
                if progress is None or self._seen_progress.get(progress_key) == progress:
                    continue
                self._seen_progress[progress_key] = progress
                self._safe_on_progress(item)

    @classmethod
    def _stable_id(cls, item: LoosePayload) -> str | int | None:
        raw_idx = item.get("resultIndex")
        if isinstance(raw_idx, int):
            return raw_idx
        for key in cls._STABLE_ID_KEYS:
            value = item.get(key)
            if isinstance(value, str) and value:
                return value
        return None

    def done(self) -> bool:
        return len(self._seen_terminal) >= self._expected

    def sorted_results(self) -> list[LoosePayload]:
        # When all keys are resultIndex ints, sort by them so the order
        # matches the server's intended ordering. Otherwise (UUID-keyed),
        # preserve insertion order — Python dicts have ordered insertion
        # semantics since 3.7.
        keys = list(self._results)
        if keys and all(isinstance(k, int) for k in keys):
            keys.sort()
        return [self._results[k] for k in keys]


def _maybe_raise_item_errors(
    collector: _AsyncCollector,
    *,
    task_type: str | None,
    task_uuid: str,
) -> None:
    """
    Drain per-item errors from the collector. If any are present, raise a
    `RunwareError` for the first one. Callbacks fire during ingest() so the
    user sees partial outcomes before this raise.
    """
    errors = collector.take_errors()
    if not errors:
        return
    # Each error item has the shape {status: 'error', error: {code, message, ...}, taskUUID?}.
    # parse_api_error accepts the standard {errors: [...]} envelope.
    err_payloads: list[LoosePayload] = [
        {
            **cast(LoosePayload, item.get("error") or {}),
            "taskUUID": item.get("taskUUID") or task_uuid,
        }
        for item in errors
    ]
    raise parse_api_error(
        {"errors": err_payloads},
        task_type=task_type,
    )


def _build_registry_fallback() -> RegistryData:
    """Build a RegistryData snapshot from the bundled generated types.

    Operation task types (caption-image, upscale-video, etc.) are merged into
    the architecture map — they're keyed the same way (slug → taskType) and
    looked up through the same code path, matching the TS SDK's fallback shape.
    """
    from .registry import RegistryModelEntry  # avoid circular import at module load

    models_data: dict[str, RegistryModelEntry] = {
        air: RegistryModelEntry(task_type=entry.task_type, id=entry.id)
        for air, entry in _bundled_models.items()
    }
    architecture_fallback: dict[str, str] = {
        **_bundled_arch_task_types,
        **_bundled_operation_task_types,
    }
    return RegistryData(
        models=models_data,
        architecture_task_types=architecture_fallback,
        modality_task_types=dict(_bundled_modality_task_types),
    )


def _progress_value(item: LoosePayload) -> float | None:
    raw = item.get("progress")
    if isinstance(raw, (int, float)):
        return float(raw)
    return None


def _is_terminal(item: LoosePayload) -> bool:
    for key in ("imageURL", "videoURL", "audioURL", "modelURL", "text", "result"):
        if item.get(key) is not None:
            return True
    status: object = item.get("status")
    return status == "completed"


def _next_poll_delay(poll_number: int, current: float) -> float:
    if poll_number == 1:
        return 0.5
    return min(current * 1.5, 10.0)


async def _interruptible_sleep(seconds: float, cancel_event: asyncio.Event | None) -> None:
    if cancel_event is None:
        await asyncio.sleep(seconds)
        return
    sleep_task = asyncio.create_task(asyncio.sleep(seconds))
    cancel_task = asyncio.create_task(cancel_event.wait())
    try:
        done, _pending = await asyncio.wait(
            {sleep_task, cancel_task}, return_when=asyncio.FIRST_COMPLETED
        )
        if cancel_task in done:
            sleep_task.cancel()
            raise create_runware_error("aborted", "Request aborted during polling")
        cancel_task.cancel()
    except asyncio.CancelledError:
        sleep_task.cancel()
        cancel_task.cancel()
        raise


async def _await_with_cancel(
    future: asyncio.Future[list[LoosePayload]],
    cancel_event: asyncio.Event | None,
) -> list[LoosePayload]:
    if cancel_event is None:
        return await future
    cancel_task = asyncio.create_task(cancel_event.wait())
    try:
        done, _pending = await asyncio.wait(
            {future, cancel_task}, return_when=asyncio.FIRST_COMPLETED
        )
        if cancel_task in done and not future.done():
            future.cancel()
            raise create_runware_error("aborted", "Request aborted")
        cancel_task.cancel()
        return await future
    finally:
        if not cancel_task.done():
            cancel_task.cancel()


def _extract_items(response: WireFrame | object) -> list[LoosePayload]:
    if isinstance(response, dict):
        obj = cast(dict[str, object], response)
        if "errors" in obj or "error" in obj:
            raise parse_api_error(obj)
        data = obj.get("data")
        if isinstance(data, list):
            data_list = cast(list[object], data)
            return [cast(LoosePayload, item) for item in data_list if isinstance(item, dict)]
        return []
    if isinstance(response, list):
        resp_list = cast(list[object], response)
        return [cast(LoosePayload, item) for item in resp_list if isinstance(item, dict)]
    return []
