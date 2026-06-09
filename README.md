# Runware Python SDK

Async Python SDK for the Runware platform. A unified API for image, video, audio, text, and 3D generation — powered by the [Runware inference platform](https://runware.ai).

[Documentation](https://runware.ai/docs) · [Report a bug](https://github.com/Runware/python-sdk/issues)

- **One method for everything** — `.run()` handles every model type
- **Schema-driven types** — generated from Runware's canonical JSON schemas
- **WebSocket and REST transports** — persistent connections or stateless HTTP
- **LLM streaming via SSE** — token-by-token text generation with `.stream()`
- **Automatic model resolution** — the SDK resolves task types from AIR identifiers
- **Python 3.11+, asyncio-native** — single source of truth for all I/O


## Installation

```bash
pip install runware
```

## Quick start

Generate an image in five lines:

```python
import asyncio
import os
from runware import Runware

async def main() -> None:
    async with Runware(api_key=os.environ["RUNWARE_API_KEY"]) as client:
        results = await client.run({
            "model": "runware:400@1",
            "positivePrompt": "A serene mountain landscape at sunset",
            "width": 1024,
            "height": 1024,
        })
        print(results[0]["imageURL"])

asyncio.run(main())
```

The SDK resolves `runware:400@1` to the right task type automatically. `RUNWARE_API_KEY` is read from the environment if you don't pass `api_key=...` explicitly.

More runnable patterns in [`examples/`](./examples/) — curated models, community fine-tunes, streaming, the WebSocket transport.

## Core Concepts

### One method for everything

Every inference task goes through `.run()`. The SDK determines the task type from the model's AIR identifier:

```python
# Image generation
images = await client.run({
    "model": "runware:400@1",
    "positivePrompt": "Abstract digital art",
    "width": 1024, "height": 1024,
})

# Video generation
videos = await client.run({
    "model": "google:3@3",
    "positivePrompt": "Ocean waves at sunset",
    "duration": 8,
})

# Text inference (LLM)
responses = await client.run({
    "model": "google:gemma@4-31b",
    "messages": [{"role": "user", "content": "Explain quantum computing"}],
})

# Audio generation (designs a voice from the prompt, then speaks the text)
audio = await client.run({
    "model": "alibaba:qwen@3-tts-1.7b-voicedesign",
    "positivePrompt": "A calm, friendly young woman with a soft tone",
    "speech": {"text": "Hello world", "voice": "design"},
})
```

### Typed params per architecture

When you know the architecture, import its `Params` TypedDict from `runware.types.task_map` and annotate your call:

```python
from runware.types.task_map import SdxlParams

params: SdxlParams = {
    "model": "civitai:133005@782002",
    "taskType": "imageInference",
    "positivePrompt": "A professional headshot portrait",
    "negativePrompt": "blurry, distorted",
    "width": 1024,
    "height": 1024,
    "steps": 30,
    "scheduler": "DPMSolverMultistep",
}
images = await client.run(params)
```

The generated module ships params and result TypedDicts for every architecture and operation, plus three lookup dicts:

- `architecture_task_types` — `sdxl`, `flux-1-dev`, `pony`, `illustrious`, and more
- `modality_task_types` — `image`, `video`, `audio`, `text`, `3d`
- `operation_task_types` — `caption-image`, `upscale-image`, `remove-background-image`, `prompt-enhance`, `vectorize`, and more

### Community and trained models

For models not built into the SDK (community uploads, fine-tunes), the registry won't have them yet — pass `taskType` explicitly:

```python
images = await client.run({
    "model": "runware:exactly-illustrative@my-trained-style",
    "taskType": "imageInference",
    "positivePrompt": "A lighthouse on a rocky cliff at twilight",
    "width": 1024,
    "height": 1024,
})
```

Validation (when enabled) automatically picks the right schema for the AIR — no extra option needed.

### Curated-model slugs

The registry indexes every curated model under both its AIR (`runware:400@1`) and its slug (`bfl-flux-2-dev`). You can pass either:

```python
# Both call the same model.
await client.run({"model": "runware:400@1", "positivePrompt": "..."})
await client.run({"model": "bfl-flux-2-dev", "positivePrompt": "..."})
```

The SDK rewrites slugs to canonical AIRs before sending. Non-curated identifiers (custom fine-tunes, unknown strings) pass through unchanged.

## LLM Streaming

For text models, `.stream()` delivers tokens as they're generated:

```python
stream = await client.stream({
    "model": "google:gemma@4-31b",
    "messages": [{"role": "user", "content": "Tell me a story about a robot"}],
})

async for word in stream.text_stream:
    print(word, end="", flush=True)
```

`stream()` returns a `TextStream` with multiple ways to consume the response:

```python
stream = await client.stream({
    "model": "google:gemma@4-31b",
    "messages": [{"role": "user", "content": "Explain gravity"}],
})

# Iterate text deltas
async for word in stream.text_stream:
    print(word, end="", flush=True)

# Iterate reasoning content (reasoning models)
async for thought in stream.reasoning_stream:
    print(f"[thinking] {thought}")

# Get the full text at once (awaits the entire stream)
full_text = await stream.text()

# Get the final result with metadata
result = await stream.result()
print(result.text)
print(result.finish_reason)  # "stop", "length", etc.
print(result.usage)          # {"promptTokens": ..., "completionTokens": ...}
print(result.cost)           # USD cost
```

> **Note:** `stream()` only supports `numberResults: 1`. For multiple completions use `run()` — `stream()` raises if you pass `numberResults > 1`.

## Transport Options

### WebSocket (default)

Best when you make multiple requests or want real-time feedback:

```python
async with Runware(transport_type="websocket") as client:
    images = await client.run({"model": "runware:400@1", "positivePrompt": "..."})
    videos = await client.run({"model": "google:3@3", "positivePrompt": "..."})
```

WebSocket connections are automatically recovered on network interruptions. The SDK re-authenticates with the same session UUID and the server replays pending results.

### REST

Best for serverless functions or one-off requests:

```python
async with Runware(transport_type="rest") as client:
    images = await client.run({
        "model": "runware:400@1",
        "positivePrompt": "A landscape painting",
        "width": 1024, "height": 1024,
    })
```

## Concurrent Operations

Run multiple tasks in parallel with `asyncio.gather`:

```python
import asyncio

async with Runware() as client:
    images, upscaled, caption = await asyncio.gather(
        client.run({
            "model": "runware:400@1",
            "positivePrompt": "Abstract art",
            "numberResults": 3,
        }),
        client.run({
            "model": "runware:504@1",
            "taskType": "upscale",
            "inputs": {"image": "https://example.com/photo.jpg"},
        }),
        client.run({
            "model": "runware:150@2",
            "taskType": "caption",
            "inputs": {"image": "https://example.com/photo.jpg"},
        }),
    )
```

## Cancellation

Pass an `asyncio.Event` and `.set()` it to cancel mid-flight. Works for `run()` and `stream()`, on both transports.

> **Heads-up:** cancel is client-side only. The server keeps processing the task and **you will be billed for it**. Cancelling just stops the SDK from waiting for the result.

```python
import asyncio
from runware import RunOptions, RunwareError

async def main() -> None:
    async with Runware() as client:
        cancel = asyncio.Event()

        async def deadline() -> None:
            await asyncio.sleep(5)
            cancel.set()

        asyncio.create_task(deadline())

        try:
            await client.run(
                {"model": "runware:400@1", "positivePrompt": "A detailed scene"},
                RunOptions(cancel_event=cancel),
            )
        except RunwareError as exc:
            if exc.code == "aborted":
                print("Cancelled")
```

For streams, set the cancel event to end iteration:

```python
from runware import StreamOptions

stream = await client.stream(
    {"model": "google:gemma@4-31b", "messages": [{"role": "user", "content": "..."}]},
    StreamOptions(cancel_event=cancel),
)
async for word in stream.text_stream:
    print(word, end="")
    if some_condition:
        cancel.set()
```

## Result and progress callbacks

Two callbacks let you observe a task as it unfolds:

- **`on_result(item)`** — fires once per item the moment it reaches a terminal state (`success` or `error`). For `numberResults > 1`, fires up to N times. Useful for streaming results into a UI as they appear.
- **`on_progress(item)`** — fires when an item's `progress` field changes (0-100). Currently only a handful of long-running models emit progress (mostly training).

```python
from runware import RunOptions

def watch(item: dict) -> None:
    if item.get("status") == "success":
        print("ready:", item.get("imageURL"))
    else:
        print("failed:", item.get("error"))

def progress(item: dict) -> None:
    print(f"{item.get('progress')}%")

results = await client.run(
    {"model": "google:3@3", "positivePrompt": "Ocean waves", "numberResults": 3},
    RunOptions(on_result=watch, on_progress=progress),
)
```

Error items fire `on_result` **before** the call raises — so when a per-result failure happens (provider hiccup, one of N results moderated, etc.), you still see the successful items via callback before the call raises. Same behavior on both WebSocket and REST. Request-level failures (`validation`, `auth`, `quota`, `rateLimit`) are the exception: they raise at submit time, before any results exist.

## Error Handling

All SDK errors are `RunwareError` instances:

```python
from runware import Runware, RunwareError

async with Runware() as client:
    try:
        results = await client.run({
            "model": "runware:400@1",
            "positivePrompt": "A detailed rendering",
        })
    except RunwareError as exc:
        print(exc.code)              # 'validation' | 'auth' | 'quota' | ...
        print(exc.retryable)         # True for provider/timeout/connection/rateLimit/serverError
        print(exc.message)           # Human-readable description
        print(exc.parameter)         # Which param caused the error, if any
        print(exc.documentation)     # Link to model / utility / errors docs
        print(exc.task_uuid)         # Request UUID
        print(exc.status_code)       # HTTP status, when applicable
        print(exc.validation_errors) # Per-field errors when validate=True
```

For cross-realm setups (different asyncio loops, subprocess boundaries) use `is_runware_error(exc)` instead of `isinstance`:

```python
from runware import is_runware_error

if is_runware_error(exc):
    ...
```

`code` is a small, stable enum — `validation`, `auth`, `quota`, `rateLimit`, `safety`, `provider`, `timeout`, `notFound`, `serverError`, `connection`, `aborted`, `unknown`. Switch on it for high-level handling. The server's raw error identifier (hundreds of unstable values) is intentionally not exposed.

```python
if exc.code == "validation":
    # Show form error, use exc.parameter to highlight the field
    ...
elif exc.code == "quota":
    # Redirect to billing
    ...
elif exc.retryable:
    # Backoff and retry
    ...
```

### Raising your own RunwareError

If you're wrapping the SDK behind another layer and want to surface errors with the same shape, build one with `create_runware_error`:

```python
from runware import create_runware_error

raise create_runware_error(
    "invalidParameter",
    "Width must be a multiple of 64",
    parameter="width",
    task_type="imageInference",
)
```

The constructor derives `code` and `documentation` URL from the raw code + model/parameter context — same logic the SDK uses internally.

## Configuration

`Runware(...)` accepts keyword arguments matching the `SDKConfig` dataclass:

| Field | Default | Notes |
|---|---|---|
| `api_key` | from `RUNWARE_API_KEY` | required |
| `transport_type` | `"websocket"` | or `"rest"` |
| `http_base_url` | `https://api.runware.ai/v1` | include the version path |
| `ws_base_url` | `wss://ws-api.runware.ai/v1` | include the version path |
| `timeout` | `1_200_000` (ms) | per-HTTP-call (one POST, one `getResponse` poll) |
| `poll_timeout` | `1_200_000` (ms) | end-to-end polling budget on either transport |
| `auth_timeout` | `15_000` (ms) | WebSocket auth handshake |
| `max_retries` | `3` | REST retries |
| `retry_delay` | `1_000` (ms) | base backoff |
| `retry_strategy` | `"exponential"` | or `"linear"` |
| `max_reconnect_attempts` | `inf` | WebSocket reconnect cap |
| `debug` | `False` | enable structured debug logs |
| `validate` | `False` | enable client-side schema validation |
| `dependencies` | `None` | inject a custom `aiohttp.ClientSession` and/or `ws_connect` |
| `log_sink` | `None` | pluggable destination for log entries |

### Custom log sink

By default, logs go through Python's stdlib `logging` under the `runware` logger. To send them elsewhere (Datadog, Sentry, a file, an aggregator), pass a `log_sink`:

```python
from runware import LogEntry, Runware

def sink(entry: LogEntry) -> None:
    # entry: { category, message, data, timestamp }
    print(entry.category, entry.message, entry.data)

async with Runware(debug=True, log_sink=sink) as client:
    ...
```

Categories: `connection`, `auth`, `heartbeat`, `send`, `receive`, `request`, `retry`, `error`, `warn`, `info`. With `debug=False`, the logger is a noop — every call drops, no I/O.

### Picking up newly-launched models

New Runware models become usable automatically — no SDK update needed. To force a refresh immediately (instead of waiting for the next 5-minute background cycle):

```python
await client.refresh_registry()
results = await client.run({"model": "newprovider:1@1", "positivePrompt": "..."})
```

The registry caches the model map for 5 minutes. A bundled snapshot ships with the package and is used as a fallback when the network is unreachable.

### Async delivery

The SDK sends `deliveryMethod: "async"` by default for all inference tasks. On both transports, the server stores the result and the SDK polls `getResponse` until the task completes — that's why the same `poll_timeout` controls behavior on REST and WebSocket alike (default: 20 minutes).

For long tasks (video, training, large upscale), raise `poll_timeout`:

```python
client = Runware(poll_timeout=1_800_000)  # 30 minutes
```

Or per-call via `RunOptions`:

```python
videos = await client.run(
    {"model": "google:3@3", "positivePrompt": "Ocean waves"},
    RunOptions(timeout=600_000),
)
```

#### Opting into sync delivery

For fast tasks (text inference, fast image gen, captioning) you can skip the polling round-trips by setting `deliveryMethod: "sync"`. The server holds the response open and pushes back the result in one round trip:

```python
responses = await client.run({
    "model": "google:gemma@4-31b",
    "messages": [{"role": "user", "content": "Hello"}],
    "deliveryMethod": "sync",
})
```

On **WebSocket** this is where the persistent connection pays off — one frame in, one frame back, no polling.
On **REST** it's a single HTTP request with the full result in the response body.

Pick sync when the task finishes inside the server's connection budget (~120s for WebSocket sync, the HTTP read timeout for REST). For anything longer — video, 3D, large upscale, multi-result batches — stick with the async default.

### Per-call options

The second argument to `client.run()` and `client.stream()` is a `RunOptions` / `StreamOptions` instance — per-call overrides that don't belong on the client:

```python
from runware import RunOptions

await client.run(
    {"model": "runware:400@1", "positivePrompt": "A landscape"},
    RunOptions(
        timeout=600_000,         # ms — override config.poll_timeout for this call
        cancel_event=cancel,     # asyncio.Event — cancel this call
        on_result=watch,         # fires per item as it completes
        on_progress=progress,    # fires when an item's progress % changes
        validate=True,           # override config.validate for this call
    ),
)
```

`stream()` accepts `StreamOptions` with `timeout`, `cancel_event`, and `validate` (no polling means no per-item callbacks).

## Validation

Enable client-side validation to catch invalid parameters before they reach the API:

```python
async with Runware(validate=True) as client:
    await client.run({"model": "...", ...})  # raises RunwareError(code='validation') on bad params
```

The schema for each model is fetched on first use and cached per-process. Works the same for curated models and community fine-tunes — pass nothing beyond `validate=True`.

If the schema can't be fetched (network failure, model unknown to the registry), validation is silently skipped and the server still validates as the source of truth.

Validation errors come back as a `RunwareError` with `code="validation"` and structured details on `validation_errors`:

```python
from runware import RunwareError

try:
    await client.run({...})
except RunwareError as exc:
    if exc.code == "validation":
        print(exc.task_type)          # "imageInference"
        print(exc.validation_errors)  # [{message, path, rule, rule_definition}]
```

Validation can also be toggled **per call** via `RunOptions.validate`, which overrides `config.validate`:

```python
# Force on for one call even if config.validate is False
await client.run({...}, RunOptions(validate=True))

# Skip for one call even if config.validate is True
await client.run({...}, RunOptions(validate=False))
```

To clear the in-process validator cache (e.g., after a server-side schema change without restarting):

```python
from runware import clear_validator_cache
clear_validator_cache()
```

## Utility Methods

```python
# Search for available models
models = await client.model_search({
    "search": "portrait",
    "category": "checkpoint",
    "architecture": "sdxl",
    "limit": 10,
})

# Upload an image for use as input
uploaded = await client.image_upload({
    "image": "https://example.com/photo.jpg",  # URL, Data URI, or Base64
})

# Get account details
account = await client.account_management({"operation": "getDetails"})

# Retrieve a previously executed task
archived = await client.get_task_details({"taskUUID": "abc-123"})

# Poll for an async task result (used internally by run() — rarely needed directly)
result = await client.get_response({"taskUUID": "abc-123"})

# Upload a custom model
await client.model_upload({
    "category": "checkpoint",
    "architecture": "sdxl",
    "format": "safetensors",
    # ... plus model file details
})
```

`get_task_details` vs `get_response`: use `get_task_details` for "look up something I ran before" — it queries the task archive. `get_response` is the polling mechanism the SDK uses internally during async `.run()`; you generally don't need to call it directly.

## Content metadata

`client.content.*` exposes Runware's curated model catalog as read-only metadata — names, AIRs, headlines, capabilities, pricing, examples. Public information, no extra cost.

```python
# List curated models, optionally filtered
models = await client.content.list_models({
    "capability": "io:text-to-image",
    "category": "image",
    "creator": "black-forest-labs",
    "search": "flux",
})

# Single curated model by id
model = await client.content.get_model("alibaba-z-image-turbo")

# Sample input/output pairs the model can produce
examples = await client.content.get_model_examples("flux-1-dev")

# Pricing summary and per-configuration examples
pricing = await client.content.get_model_pricing("flux-1-dev")

# Discover the capability taxonomy (io:*, op:*, form:*)
capabilities = await client.content.list_capabilities()

# Collections (Runware-defined model groupings) with full model objects inlined
collections = await client.content.list_collections({"category": "image"})

# Creators with their curated models inlined
creators = await client.content.list_creators()
google = await client.content.get_creator("google")

# Pagination — pass paginate=True to get {"total", "limit", "offset", "items"}
page = await client.content.list_models({"paginate": True, "limit": 25, "offset": 0})
```

`creator`, `capabilities`, and `architecture` on each model are returned as id strings — resolve them against `list_creators`, `list_capabilities`, and the architecture id respectively when you need the human-readable label. Collections and creators are the only endpoints that resolve their inner `models` array to full objects.

## File helpers

`file_to_data_uri` encodes a local file as a `data:` URI for passing as input:

```python
from pathlib import Path
from runware import file_to_data_uri

data_uri = file_to_data_uri(Path("photo.jpg"))
await client.image_upload({"image": data_uri})
```

Accepts both `Path` and `bytes` — `bytes` is useful when the file lives in memory (e.g. a freshly downloaded blob).

## Custom dependencies

For testing, proxies, or custom auth flows, pass a `RuntimeDependencies`:

```python
import aiohttp
from runware import Runware, RuntimeDependencies

session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60))

async with Runware(
    api_key="...",
    dependencies=RuntimeDependencies(session=session),
) as client:
    ...
```

Pass `ws_connect=...` similarly to override the WebSocket connect path (defaults to `websockets.connect`). Injected sessions are not closed on `client.close()` — you own the lifecycle.

## License

MIT
