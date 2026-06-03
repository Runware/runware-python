"""
Generate `runware/types/task_map.py` from the schemas bundle.

The schemas service publishes immutable per-release bundles at
`https://schemas.runware.ai/releases/<version>/schema-map.json` (served from
R2). This script reads that bundle and emits Python types: a TypedDict per
curated model / architecture / utility, plus dictionaries of curated AIRs,
architecture task types, and modality task types — equivalent of TS's
generated `task-map.ts`.

Pin the version in `runware/_schemas_version.py`. Bump it whenever you want
fresh types: edit the constant, re-run this script, commit the regenerated
`task_map.py`.

While the R2 endpoint hasn't been deployed yet, this script falls back to
reading `repos/schemas/dist-worker/schema-map.json` locally. Set
`RUNWARE_SCHEMA_MAP_PATH` to override.
"""

from __future__ import annotations

import json
import os
import re
import sys
import textwrap
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Read the pinned schemas version without triggering `runware/__init__.py` —
# the package's chain of imports would fail mid-regeneration whenever the
# generated file is being rewritten with a new shape.
_VERSION_FILE = PROJECT_ROOT / "runware" / "_schemas_version.py"
_match = re.search(
    r'SCHEMAS_VERSION\s*=\s*"([^"]*)"', _VERSION_FILE.read_text()
)
SCHEMAS_VERSION = _match.group(1) if _match else "latest"

OUTPUT_PATH = PROJECT_ROOT / "runware" / "types" / "task_map.py"
REMOTE_URL = f"https://schemas.runware.ai/releases/{SCHEMAS_VERSION}/schema-map.json"
LOCAL_FALLBACK = (
    PROJECT_ROOT.parent / "schemas" / "dist-worker" / "schema-map.json"
)


# --------------------------------------------------------------------------- fetch


def load_schema_map() -> dict[str, Any]:
    override = os.environ.get("RUNWARE_SCHEMA_MAP_PATH")
    if override:
        path = Path(override).expanduser()
        print(f"Reading schema-map.json from {path} (override).", file=sys.stderr)
        return json.loads(path.read_text())

    try:
        print(f"Fetching {REMOTE_URL} ...", file=sys.stderr)
        with urllib.request.urlopen(REMOTE_URL) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as exc:
        print(
            f"Remote fetch failed ({exc.code} {exc.reason}). "
            "Falling back to local dist-worker.",
            file=sys.stderr,
        )
    except urllib.error.URLError as exc:
        print(
            f"Remote fetch failed ({exc.reason}). "
            "Falling back to local dist-worker.",
            file=sys.stderr,
        )

    if LOCAL_FALLBACK.exists():
        print(f"Reading {LOCAL_FALLBACK} (local fallback).", file=sys.stderr)
        return json.loads(LOCAL_FALLBACK.read_text())

    raise SystemExit(
        f"Could not load schema-map. Tried {REMOTE_URL} and {LOCAL_FALLBACK}. "
        "Set RUNWARE_SCHEMA_MAP_PATH to a local path or deploy the worker first."
    )


# ----------------------------------------------------------- python identifier helpers


_IDENTIFIER_RE = re.compile(r"[^0-9A-Za-z]+")

# Slug prefixes that would otherwise produce identifiers starting with a digit.
# Matches the TS generator's special case so cross-SDK class names stay aligned.
_LEADING_DIGIT_REWRITE: dict[str, str] = {
    "3d": "ThreeD",
}


def to_class_name(*parts: str) -> str:
    """Turn arbitrary slugs into a PascalCase Python identifier."""
    pieces: list[str] = []
    for raw_part in parts:
        # Apply the digit-prefix rewrite to the raw part before tokenizing so
        # `3dInference` becomes `ThreeDInference`, not `_3dInference`.
        part = raw_part
        for prefix, replacement in _LEADING_DIGIT_REWRITE.items():
            if part.lower().startswith(prefix):
                part = replacement + part[len(prefix):]
                break
        for chunk in _IDENTIFIER_RE.split(part):
            if not chunk:
                continue
            pieces.append(chunk[:1].upper() + chunk[1:])
    name = "".join(pieces)
    if name and name[0].isdigit():
        name = "_" + name
    return name or "Unnamed"


# --------------------------------------------------------------------------- JSON Schema → Python


def _py_literal(value: Any) -> str:
    """Render a JSON-Schema literal as a valid Python expression."""
    # `bool` must be checked before `int` because `True`/`False` are `int` subclasses.
    if isinstance(value, bool):
        return "True" if value else "False"
    if value is None:
        return "None"
    if isinstance(value, str):
        return repr(value)
    if isinstance(value, (int, float)):
        return repr(value)
    return repr(value)


def schema_to_py(schema: Any, *, owner_name: str, field_name: str | None = None) -> str:
    """
    Translate a single JSON Schema fragment to a Python type expression.

    Complex / unknown shapes fall back to `Any` — the TypedDict still provides
    autocomplete on the field name; the value type stops at the boundary.
    """
    if not isinstance(schema, dict):
        return "Any"

    # const wins everything else (most specific).
    if "const" in schema:
        return f"Literal[{_py_literal(schema['const'])}]"

    # enum becomes a Literal union.
    if "enum" in schema and isinstance(schema["enum"], list):
        members = [
            _py_literal(v) for v in schema["enum"]
            if isinstance(v, (str, int, bool, float)) or v is None
        ]
        if members:
            return "Literal[" + ", ".join(members) + "]"

    # Explicit nullability flag (some Runware schemas use this).
    nullable = schema.get("nullable") is True

    json_type = schema.get("type")

    py: str
    if json_type == "string":
        py = "str"
    elif json_type == "integer":
        py = "int"
    elif json_type == "number":
        py = "float"
    elif json_type == "boolean":
        py = "bool"
    elif json_type == "array":
        items = schema.get("items")
        item_py = schema_to_py(items, owner_name=owner_name, field_name=field_name)
        py = f"list[{item_py}]"
    elif json_type == "object":
        # Inline object — fall back to a permissive dict. Generating a nested
        # TypedDict here would require coordinating names across the whole
        # tree; the boundary at `dict[str, Any]` is the pragmatic call.
        py = "dict[str, Any]"
    elif isinstance(json_type, list):
        # Union of primitive types, e.g. ["string", "null"].
        union_parts: list[str] = []
        for t in json_type:
            sub = schema_to_py({"type": t}, owner_name=owner_name, field_name=field_name)
            union_parts.append(sub)
        py = " | ".join(dict.fromkeys(union_parts))
    elif "oneOf" in schema or "anyOf" in schema:
        variants = schema.get("oneOf") or schema.get("anyOf") or []
        if isinstance(variants, list):
            parts = [
                schema_to_py(v, owner_name=owner_name, field_name=field_name)
                for v in variants
            ]
            unique = list(dict.fromkeys(parts))
            py = " | ".join(unique) if unique else "Any"
        else:
            py = "Any"
    else:
        py = "Any"

    if nullable and "None" not in py:
        py = f"{py} | None"
    return py


# --------------------------------------------------------------------------- emit


def emit_typed_dict(
    class_name: str,
    schema: dict[str, Any],
    *,
    description: str | None = None,
) -> str:
    """Emit a TypedDict declaration from an object schema."""
    properties = schema.get("properties") if isinstance(schema, dict) else None
    required = set(schema.get("required", []) or []) if isinstance(schema, dict) else set()

    lines: list[str] = []
    if description:
        lines.append(f'    """{description}"""')
        lines.append("")

    if not isinstance(properties, dict) or not properties:
        lines.append("    pass")
        return f"class {class_name}(TypedDict, total=False):\n" + "\n".join(lines)

    for prop_name, prop_schema in properties.items():
        py_type = schema_to_py(prop_schema, owner_name=class_name, field_name=prop_name)
        type_expr = py_type if prop_name in required else f"NotRequired[{py_type}]"

        if _is_python_keyword_or_reserved(prop_name):
            # Skip keys that aren't valid Python identifiers in a TypedDict
            # class body — they're still valid wire keys, but pyright can't
            # express them this way. Most runware schemas avoid this.
            lines.append(
                f"    # NOTE: field {prop_name!r} skipped (not a valid Python identifier)"
            )
            continue
        lines.append(f"    {prop_name}: {type_expr}")

    return f"class {class_name}(TypedDict, total=False):\n" + "\n".join(lines)


_PY_KEYWORDS = {
    "False", "None", "True", "and", "as", "assert", "async", "await", "break",
    "class", "continue", "def", "del", "elif", "else", "except", "finally",
    "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
    "not", "or", "pass", "raise", "return", "try", "while", "with", "yield",
}


def _is_python_keyword_or_reserved(name: str) -> bool:
    return name in _PY_KEYWORDS or not name.isidentifier()


def _extract_task_type(schema: dict[str, Any]) -> str | None:
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        return None
    task_type_field = properties.get("taskType")
    if not isinstance(task_type_field, dict):
        return None
    const = task_type_field.get("const")
    return const if isinstance(const, str) else None


# --------------------------------------------------------------------------- driver


def build(schema_map: dict[str, Any]) -> str:
    inference: list[dict[str, Any]] = schema_map.get("inference") or []
    architectures: dict[str, Any] = schema_map.get("architectures") or {}
    modalities: dict[str, Any] = schema_map.get("modalities") or {}
    operations: dict[str, Any] = schema_map.get("operations") or {}
    utilities: list[dict[str, Any]] = schema_map.get("utilities") or []

    inference_entries: list[tuple[str, str, str]] = []
    seen_airs: set[str] = set()
    typed_dicts: list[str] = []
    seen_class_names: set[str] = set()

    def add_typed_dict(class_name: str, schema: dict[str, Any], description: str) -> str:
        candidate = class_name
        suffix = 2
        while candidate in seen_class_names:
            candidate = f"{class_name}{suffix}"
            suffix += 1
        seen_class_names.add(candidate)
        typed_dicts.append(emit_typed_dict(candidate, schema, description=description))
        return candidate

    # Inference: one Params + one Result TypedDict per curated model. Dedupe
    # by AIR — if two models share an AIR (data bug in the schemas, but it
    # does happen), keep the first occurrence to avoid emitting a
    # duplicate-key dict literal.
    for entry in inference:
        slug = entry.get("slug")
        air = entry.get("air")
        request_schema = entry.get("requestSchema")
        response_schema = entry.get("responseSchema")
        if not isinstance(slug, str) or not isinstance(request_schema, dict):
            continue
        task_type = (
            request_schema.get("properties", {}).get("taskType", {}).get("const")
            if isinstance(request_schema.get("properties"), dict)
            else None
        )
        if not isinstance(task_type, str) or not isinstance(air, str):
            continue
        add_typed_dict(
            to_class_name(slug, "Params"),
            request_schema,
            f"Inference params for curated model `{air}` (slug: {slug}).",
        )
        if isinstance(response_schema, dict):
            add_typed_dict(
                to_class_name(slug, "Result"),
                response_schema,
                f"Inference result for curated model `{air}` (slug: {slug}).",
            )
        if air in seen_airs:
            print(f"warning: duplicate AIR {air!r} (skipping in models dict)", file=sys.stderr)
            continue
        seen_airs.add(air)
        inference_entries.append((air, task_type, slug))

    # Architectures: one Params TypedDict per architecture.
    for arch_key, arch_schema in architectures.items():
        if not isinstance(arch_schema, dict):
            continue
        add_typed_dict(
            to_class_name(arch_key, "ArchParams"),
            arch_schema,
            f"Inference params for architecture `{arch_key}`.",
        )

    # Modalities: one loose Params TypedDict per modality (image, video, …).
    # The class name uses the modality's taskType so users get the familiar
    # `ImageInferenceParams`, `VideoInferenceParams`, etc.
    for modality_key, modality_schema in modalities.items():
        if not isinstance(modality_schema, dict):
            continue
        task_type = _extract_task_type(modality_schema) or f"{modality_key}Inference"
        add_typed_dict(
            to_class_name(task_type, "Params"),
            modality_schema,
            f"Loose params for the `{task_type}` modality (slug: {modality_key}).",
        )

    # Operations: one Params TypedDict per slug (caption-image, upscale-video,
    # remove-background, etc.). We emit per-slug rather than deduping by
    # taskType, since slugs like `caption-image` vs `caption-video` carry
    # distinct media-specific parameter shapes.
    for op_key, op_schema in operations.items():
        if not isinstance(op_schema, dict):
            continue
        add_typed_dict(
            to_class_name(op_key, "Params"),
            op_schema,
            f"Params for the `{op_key}` operation.",
        )

    # Utilities: Params + Result TypedDict per utility task.
    utility_slugs: list[str] = []
    for entry in utilities:
        slug = entry.get("slug")
        request_schema = entry.get("requestSchema")
        response_schema = entry.get("responseSchema")
        if not isinstance(slug, str) or not isinstance(request_schema, dict):
            continue
        utility_slugs.append(slug)
        add_typed_dict(
            to_class_name(slug, "Params"),
            request_schema,
            f"Params for the `{slug}` utility task.",
        )
        if isinstance(response_schema, dict):
            add_typed_dict(
                to_class_name(slug, "Result"),
                response_schema,
                f"Result for the `{slug}` utility task.",
            )

    # ----- registry dictionaries -----

    models_lines: list[str] = []
    task_type_literals: set[str] = set()
    for air, task_type, slug in inference_entries:
        models_lines.append(
            f'    "{air}": ModelEntry(task_type="{task_type}", id="{slug}"),'
        )
        task_type_literals.add(task_type)

    arch_lines: list[str] = []
    for arch_key, arch_schema in architectures.items():
        if not isinstance(arch_schema, dict):
            continue
        task_type = _extract_task_type(arch_schema)
        if isinstance(task_type, str):
            arch_lines.append(f'    "{arch_key}": "{task_type}",')
            task_type_literals.add(task_type)

    # Modality task types: derive from the bundle. Fall back to the hardcoded
    # canonical mapping for older bundles that don't carry the `modalities` key.
    modality_task_types: dict[str, str] = {}
    for modality_key, modality_schema in modalities.items():
        if not isinstance(modality_schema, dict):
            continue
        task_type = _extract_task_type(modality_schema)
        if isinstance(task_type, str):
            modality_task_types[modality_key] = task_type
    if not modality_task_types:
        modality_task_types = {
            "image": "imageInference",
            "video": "videoInference",
            "audio": "audioInference",
            "text": "textInference",
            "3d": "3dInference",
        }
    for v in modality_task_types.values():
        task_type_literals.add(v)

    # Operation task types: one entry per slug in the bundle's `operations` map.
    # Fall back to the canonical alphabetical subset for older bundles.
    operation_task_types: dict[str, str] = {}
    for op_key, op_schema in operations.items():
        if not isinstance(op_schema, dict):
            continue
        task_type = _extract_task_type(op_schema)
        if isinstance(task_type, str):
            operation_task_types[op_key] = task_type
    if not operation_task_types:
        operation_task_types = {
            "caption-image": "caption",
            "controlnet-preprocess": "controlNetPreprocess",
            "masking": "imageMasking",
            "prompt-enhance": "promptEnhance",
            "remove-background-image": "removeBackground",
            "training": "training",
            "upscale-image": "upscale",
            "vectorize": "vectorize",
        }
    for v in operation_task_types.values():
        task_type_literals.add(v)

    task_type_literal_members = ", ".join(
        json.dumps(s) for s in sorted(task_type_literals)
    )

    # ----- file assembly -----

    header = textwrap.dedent(f'''\
        """
        AUTO-GENERATED from runware schemas v{SCHEMAS_VERSION} — do not edit manually.

        Re-run `uv run python scripts/generate_types.py` after bumping
        `runware/_schemas_version.py` to refresh.
        """

        from __future__ import annotations

        from dataclasses import dataclass
        from typing import Any, Literal, NotRequired, TypedDict

        SCHEMAS_VERSION = "{SCHEMAS_VERSION}"

        TaskType = Literal[{task_type_literal_members}]


        @dataclass(frozen=True)
        class ModelEntry:
            task_type: str
            id: str
        ''')

    body = "\n\n".join(typed_dicts) + "\n\n"

    constants = (
        "\n# ----------------------------------------------------------- registry data\n\n"
        "models: dict[str, ModelEntry] = {\n"
        + "\n".join(sorted(models_lines))
        + "\n}\n\n"
        "architecture_task_types: dict[str, str] = {\n"
        + "\n".join(sorted(arch_lines))
        + "\n}\n\n"
        f"modality_task_types: dict[str, str] = {json.dumps(modality_task_types, indent=4, sort_keys=True)}\n\n"
        f"operation_task_types: dict[str, str] = {json.dumps(operation_task_types, indent=4, sort_keys=True)}\n"
    )

    utility_slug_literal = (
        "UtilitySlug = Literal[" + ", ".join(json.dumps(s) for s in sorted(utility_slugs)) + "]\n"
        if utility_slugs
        else "UtilitySlug = str  # no utilities in this bundle\n"
    )

    return header + "\n" + utility_slug_literal + "\n" + body + constants


def main() -> None:
    schema_map = load_schema_map()
    output = build(schema_map)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(output)
    print(f"Wrote {OUTPUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
