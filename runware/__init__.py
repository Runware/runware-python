"""
Runware Python SDK.

Public surface mirrors the TypeScript SDK's exports.

Client:
    Runware                    — async client class

Errors:
    RunwareError               — exception class for all SDK errors
    ErrorCode                  — Literal type of stable error codes
    is_runware_error           — type guard
    create_runware_error       — programmatic constructor
    parse_api_error            — parse a server error response into RunwareError

Options & config:
    SDKConfig                  — config dataclass
    RunOptions                 — per-call options for client.run()
    StreamOptions              — per-call options for client.stream()
    RuntimeDependencies        — inject custom aiohttp session / WS connect
    WebSocketConnectFactory    — type alias for the WS connect callable

Streaming:
    TextStream                 — LLM stream result with async iterators
    TextStreamChunk            — one parsed SSE chunk
    TextStreamResult           — final accumulated stream state
    parse_sse_line             — low-level SSE parser

Registry:
    Registry                   — model registry with TTL + ETag + offline fallback
    RegistryData               — parsed registry payload
    RegistryModelEntry         — single model entry
    create_registry            — factory
    models                     — bundled curated-model map (from generated types)
    architecture_task_types    — bundled architecture → taskType map
    modality_task_types        — bundled modality → taskType map
    operation_task_types       — bundled operation (caption-image, upscale-video, …) → taskType map

Logging:
    Logger                     — logger class
    LogEntry                   — one structured log line
    LogCategory                — Literal of log channel names (matches TS)
    LogSink                    — pluggable sink protocol
    create_logger              — factory

Validation:
    clear_validator_cache      — reset the in-process compiled-validator cache

Helpers:
    file_to_data_uri           — encode files/bytes as data URIs for inputs

Schemas pin:
    SCHEMAS_VERSION            — the pinned schemas-bundle version
    ModelEntry                 — generated curated-model entry shape
    TaskType                   — Literal union of all known task types
"""

from .client import Runware
from .content import ContentClient
from .errors import (
    ErrorCode,
    RunwareError,
    create_runware_error,
    is_runware_error,
    parse_api_error,
)
from .logger import LogCategory, LogEntry, Logger, LogSink, create_logger
from .registry import Registry, RegistryData, RegistryModelEntry, create_registry
from .stream import TextStream, parse_sse_line
from .types.content import (
    ArchitectureMetadata,
    Capability,
    CollectionMetadata,
    CollectionWithModels,
    Creator,
    CreatorWithModels,
    ExampleMetadata,
    GetModelExamplesOptions,
    GuideMetadata,
    ListCollectionsOptions,
    ListModelsOptions,
    ModelMetadata,
    PaginatedResponse,
    PricingExample,
    PricingModelListItem,
)
from .types.sdk import (
    RunOptions,
    RuntimeDependencies,
    SDKConfig,
    StreamOptions,
    WebSocketConnectFactory,
)
from .types.stream import TextStreamChunk, TextStreamResult
from .types.task_map import (
    SCHEMAS_VERSION,
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
    ModelEntry,
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
    TaskType,
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
    architecture_task_types,
    modality_task_types,
    models,
    operation_task_types,
)
from .utils.file import file_to_data_uri
from .validate import clear_validator_cache

__all__ = [
    "SCHEMAS_VERSION",
    "AccountManagementParams",
    "AccountManagementResult",
    "ArchitectureMetadata",
    "AudioInferenceParams",
    "AudioInferenceResult",
    "Capability",
    "CaptionImageParams",
    "CaptionParams",
    "CaptionResult",
    "CaptionVideoParams",
    "CollectionMetadata",
    "CollectionWithModels",
    "ContentClient",
    "ControlNetPreprocessResult",
    "ControlnetPreprocessParams",
    "Creator",
    "CreatorWithModels",
    "ErrorCode",
    "ExampleMetadata",
    "GetModelExamplesOptions",
    "GetResponseParams",
    "GetResponseResult",
    "GetTaskDetailsParams",
    "GetTaskDetailsResult",
    "GuideMetadata",
    "ImageInferenceParams",
    "ImageInferenceResult",
    "ImageMaskingResult",
    "ImageUploadParams",
    "ImageUploadResult",
    "ListCollectionsOptions",
    "ListModelsOptions",
    "LogCategory",
    "LogEntry",
    "LogSink",
    "Logger",
    "MaskingParams",
    "ModelEntry",
    "ModelMetadata",
    "ModelSearchParams",
    "ModelSearchResult",
    "ModelUploadParams",
    "ModelUploadResult",
    "PaginatedResponse",
    "PricingExample",
    "PricingModelListItem",
    "PromptEnhanceParams",
    "PromptEnhanceResult",
    "Registry",
    "RegistryData",
    "RegistryModelEntry",
    "RemoveBackgroundImageParams",
    "RemoveBackgroundParams",
    "RemoveBackgroundResult",
    "RemoveBackgroundVideoParams",
    "RunOptions",
    "RuntimeDependencies",
    "Runware",
    "RunwareError",
    "SDKConfig",
    "StreamOptions",
    "TaskType",
    "TextInferenceParams",
    "TextInferenceResult",
    "TextStream",
    "TextStreamChunk",
    "TextStreamResult",
    "ThreeDInferenceParams",
    "ThreeDInferenceResult",
    "TrainingParams",
    "TrainingResult",
    "UpscaleImageParams",
    "UpscaleParams",
    "UpscaleResult",
    "UpscaleVideoParams",
    "VectorizeParams",
    "VectorizeResult",
    "VideoInferenceParams",
    "VideoInferenceResult",
    "WebSocketConnectFactory",
    "architecture_task_types",
    "clear_validator_cache",
    "create_logger",
    "create_registry",
    "create_runware_error",
    "file_to_data_uri",
    "is_runware_error",
    "modality_task_types",
    "models",
    "operation_task_types",
    "parse_api_error",
    "parse_sse_line",
]
