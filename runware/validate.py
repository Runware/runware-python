"""
Client-side request validation against fetched schemas.

Opt-in via `validate=True` on the SDK config or `RunOptions.validate=True` per
call. Schemas are fetched from `https://schemas.runware.ai/resolve/:id`,
compiled by fastjsonschema, and cached per-model. Concurrent first-hits for
the same model share an asyncio.Future to avoid double-compile (which would
break fastjsonschema state in some edge cases).

Inner `$id`s are stripped before compile — they're vestigial on a fully
dereferenced schema and break compile with "reference resolves to more than
one schema" when the same inner sub-schema appears at multiple paths.
"""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from typing import cast

import aiohttp
import fastjsonschema  # pyright: ignore[reportMissingTypeStubs]

from ._docs_cache import clear_docs_url_cache, set_docs_url_for_model
from .constants import SCHEMAS_BASE_URL
from .errors import create_runware_error
from .logger import Logger

Validator = Callable[[dict[str, object]], object]
_JsonSchemaException: type[Exception] = fastjsonschema.JsonSchemaException

_validator_cache: dict[str, asyncio.Future[Validator | None]] = {}


def clear_validator_cache() -> None:
    """Reset the in-process compiled-validator cache."""
    _validator_cache.clear()
    clear_docs_url_cache()


def strip_inner_ids(schema: object) -> object:
    """
    Drop `$id` from every non-root subschema.

    After full dereferencing, inner `$id`s are vestigial — and a sub-schema
    inlined at two paths carrying the same `$id` breaks fastjsonschema at
    compile time. Mirrors the SDK-side defense in the TS validate.ts.
    """

    def walk(node: object, is_root: bool) -> object:
        if isinstance(node, list):
            node_list = cast(list[object], node)
            return [walk(item, False) for item in node_list]
        if isinstance(node, dict):
            node_dict = cast(dict[str, object], node)
            out: dict[str, object] = {}
            for key, value in node_dict.items():
                if key == "$id" and not is_root:
                    continue
                out[key] = walk(value, False)
            return out
        return node

    return walk(schema, True)


async def validate_tasks(
    tasks: list[dict[str, object]],
    *,
    log: Logger,
    session: aiohttp.ClientSession,
) -> None:
    """
    Validate each task in the batch. Raises RunwareError(code='validation')
    on the first failure. Tasks without a `model` field are skipped (utility
    tasks like getResponse, accountManagement).
    """
    for task in tasks:
        model = task.get("model")
        if not isinstance(model, str):
            continue

        validator = await _get_validator(model, log=log, session=session)
        if validator is None:
            continue

        try:
            validator(task)
        except _JsonSchemaException as exc:
            raise _build_validation_error(task, exc) from exc


async def _get_validator(
    model: str,
    *,
    log: Logger,
    session: aiohttp.ClientSession,
) -> Validator | None:
    cached = _validator_cache.get(model)
    if cached is not None:
        return await cached

    loop = asyncio.get_running_loop()
    future: asyncio.Future[Validator | None] = loop.create_future()
    _validator_cache[model] = future

    try:
        schema = await _fetch_model_schema(model, log=log, session=session)
        if schema is None:
            future.set_result(None)
            return None
        sanitized = strip_inner_ids(schema)
        # fastjsonschema is untyped; compile() returns the validator function.
        validator = cast(
            Validator,
            fastjsonschema.compile(sanitized),  # pyright: ignore[reportUnknownMemberType]
        )
        future.set_result(validator)
        return validator
    except Exception as exc:
        future.set_exception(exc)
        _validator_cache.pop(model, None)
        raise


async def _fetch_model_schema(
    model: str,
    *,
    log: Logger,
    session: aiohttp.ClientSession,
) -> dict[str, object] | None:
    url = f"{SCHEMAS_BASE_URL}/resolve/{model}"
    try:
        async with session.get(url) as response:
            if response.status == 404:
                return None
            if not response.ok:
                log.warn(
                    f"Schema resolve failed for {model}: HTTP {response.status}",
                    {"url": url},
                )
                return None
            payload = cast(dict[str, object], await response.json())
    except aiohttp.ClientError as exc:
        log.warn(f"Schema resolve error for {model}: {exc}", {"url": url})
        return None

    documentation = payload.get("documentation")
    if isinstance(documentation, str):
        set_docs_url_for_model(model, documentation)

    request_schema = payload.get("requestSchema")
    if isinstance(request_schema, dict):
        return cast(dict[str, object], request_schema)
    return None


def _build_validation_error(task: dict[str, object], exc: Exception) -> Exception:
    # fastjsonschema's JsonSchemaException carries `message`, `path`, `rule`,
    # and `rule_definition` attributes but the library is untyped, so we
    # access them defensively via getattr.
    message = cast(str, getattr(exc, "message", str(exc)))
    raw_path_any = cast(object, getattr(exc, "path", None))
    raw_path: list[object] = (
        cast(list[object], raw_path_any) if isinstance(raw_path_any, list) else []
    )
    parameter: str | None = None
    if len(raw_path) > 1:
        # path[0] is usually "data" (the root). Skip it for the user-facing param name.
        parts = [str(p) for p in raw_path[1:]]
        parameter = ".".join(parts) or None

    task_type = task.get("taskType")
    task_uuid = task.get("taskUUID")
    model = task.get("model")
    return create_runware_error(
        "validationFailed",
        f"Validation failed for {task_type}: {message}",
        parameter=parameter,
        task_type=task_type if isinstance(task_type, str) else None,
        task_uuid=task_uuid if isinstance(task_uuid, str) else None,
        model=model if isinstance(model, str) else None,
        validation_errors=[
            {
                "message": message,
                "path": list(raw_path),
                "rule": cast(object, getattr(exc, "rule", None)),
                "rule_definition": cast(object, getattr(exc, "rule_definition", None)),
            }
        ],
    )
