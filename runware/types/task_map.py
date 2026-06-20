"""
AUTO-GENERATED from runware schemas v20260619230808 — do not edit manually.

Re-run `uv run python scripts/generate_types.py` after bumping
`runware/_schemas_version.py` to refresh.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, NotRequired, TypedDict

SCHEMAS_VERSION = "20260619230808"

TaskType = Literal["3dInference", "audioInference", "caption", "controlNetPreprocess", "imageInference", "imageMasking", "modelUpload", "promptEnhance", "removeBackground", "textInference", "training", "upscale", "vectorize", "videoInference"]


@dataclass(frozen=True)
class ModelEntry:
    task_type: str
    id: str

UtilitySlug = Literal["account-management", "authentication", "get-response", "get-task-details", "image-upload", "model-search", "model-upload", "ping"]

class Llama318bPromptEnhancerParams(TypedDict, total=False):
    """Inference params for curated model `runware:llama-3-1-8b@prompt-enhancer` (slug: llama-3-1-8b-prompt-enhancer)."""

    model: Literal['runware:llama-3-1-8b@prompt-enhancer']
    taskType: Literal['promptEnhance']
    taskUUID: str
    webhookURL: NotRequired[str]
    deliveryMethod: NotRequired[str]
    includeCost: NotRequired[bool]
    prompt: str
    promptMaxLength: NotRequired[int]
    promptVersions: NotRequired[int]

class Llama318bPromptEnhancerResult(TypedDict, total=False):
    """Inference result for curated model `runware:llama-3-1-8b@prompt-enhancer` (slug: llama-3-1-8b-prompt-enhancer)."""

    taskType: Literal['promptEnhance']
    taskUUID: str
    cost: NotRequired[float]
    text: str

class PromptEnhanceResult(TypedDict, total=False):
    """Canonical result shape for `promptEnhance` tasks."""

    taskType: Literal['promptEnhance']
    taskUUID: str
    cost: NotRequired[float]
    text: str

class Dia22bParams(TypedDict, total=False):
    """Inference params for curated model `runware:dia2@2b` (slug: dia2-2b)."""

    model: Literal['runware:dia2@2b']
    inputs: NotRequired[dict[str, object]]
    negativePrompt: NotRequired[str]
    seed: NotRequired[int]
    CFGScale: NotRequired[float]
    speech: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class Dia22bResult(TypedDict, total=False):
    """Inference result for curated model `runware:dia2@2b` (slug: dia2-2b)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class AudioInferenceResult(TypedDict, total=False):
    """Canonical result shape for `audioInference` tasks."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class BirefnetV1BaseCodParams(TypedDict, total=False):
    """Inference params for curated model `runware:112@2` (slug: birefnet-v1-base-cod)."""

    model: Literal['runware:112@2']
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BirefnetV1BaseCodResult(TypedDict, total=False):
    """Inference result for curated model `runware:112@2` (slug: birefnet-v1-base-cod)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class RemoveBackgroundResult(TypedDict, total=False):
    """Canonical result shape for `removeBackground` tasks."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class ControlnetPreprocessLineartParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@lineart` (slug: controlnet-preprocess-lineart)."""

    model: Literal['runware:controlnet-preprocess@lineart']
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessLineartResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@lineart` (slug: controlnet-preprocess-lineart)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class ControlNetPreprocessResult(TypedDict, total=False):
    """Canonical result shape for `controlNetPreprocess` tasks."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class BirefnetPortraitParams(TypedDict, total=False):
    """Inference params for curated model `runware:112@10` (slug: birefnet-portrait)."""

    model: Literal['runware:112@10']
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BirefnetPortraitResult(TypedDict, total=False):
    """Inference result for curated model `runware:112@10` (slug: birefnet-portrait)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class Kandinsky50LiteParams(TypedDict, total=False):
    """Inference params for curated model `runware:210@1` (slug: kandinsky-5-0-lite)."""

    model: Literal['runware:210@1']
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    duration: Literal[5, 10]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Kandinsky50LiteResult(TypedDict, total=False):
    """Inference result for curated model `runware:210@1` (slug: kandinsky-5-0-lite)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class VideoInferenceResult(TypedDict, total=False):
    """Canonical result shape for `videoInference` tasks."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class OviParams(TypedDict, total=False):
    """Inference params for curated model `runware:190@1` (slug: ovi)."""

    model: Literal['runware:190@1']
    inputs: dict[str, object]
    positivePrompt: str
    fps: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    acceleratorOptions: NotRequired[dict[str, object]]
    advancedFeatures: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class OviResult(TypedDict, total=False):
    """Inference result for curated model `runware:190@1` (slug: ovi)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Dia16bParams(TypedDict, total=False):
    """Inference params for curated model `runware:dia@1.6b` (slug: dia-1-6b)."""

    model: Literal['runware:dia@1.6b']
    negativePrompt: NotRequired[str]
    seed: NotRequired[int]
    CFGScale: NotRequired[float]
    speech: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class Dia16bResult(TypedDict, total=False):
    """Inference result for curated model `runware:dia@1.6b` (slug: dia-1-6b)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class Flux1DevSrpoParams(TypedDict, total=False):
    """Inference params for curated model `runware:111@1` (slug: flux-1-dev-srpo)."""

    model: Literal['runware:111@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    layerDiffuse: NotRequired[bool]
    pulid: NotRequired[dict[str, object]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Flux1DevSrpoResult(TypedDict, total=False):
    """Inference result for curated model `runware:111@1` (slug: flux-1-dev-srpo)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ImageInferenceResult(TypedDict, total=False):
    """Canonical result shape for `imageInference` tasks."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class MediapipeFaceShortParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@7` (slug: mediapipe-face-short)."""

    model: Literal['runware:35@7']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class MediapipeFaceShortResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@7` (slug: mediapipe-face-short)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class ImageMaskingResult(TypedDict, total=False):
    """Canonical result shape for `imageMasking` tasks."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class Yolov8nHandParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@3` (slug: yolov8n-hand)."""

    model: Literal['runware:35@3']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class Yolov8nHandResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@3` (slug: yolov8n-hand)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class VitAgeClassifierParams(TypedDict, total=False):
    """Inference params for curated model `runware:153@1` (slug: vit-age-classifier)."""

    model: Literal['runware:153@1']
    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class VitAgeClassifierResult(TypedDict, total=False):
    """Inference result for curated model `runware:153@1` (slug: vit-age-classifier)."""

    taskType: Literal['caption']
    taskUUID: str
    cost: NotRequired[float]
    structuredData: dict[str, object]

class CaptionResult(TypedDict, total=False):
    """Canonical result shape for `caption` tasks."""

    taskType: Literal['caption']
    taskUUID: str
    cost: NotRequired[float]
    structuredData: dict[str, object]

class AceStepV15BaseParams(TypedDict, total=False):
    """Inference params for curated model `runware:ace-step@v1.5-base` (slug: ace-step-v1-5-base)."""

    model: Literal['runware:ace-step@v1.5-base']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    duration: NotRequired[float]
    seed: NotRequired[int]
    steps: NotRequired[int]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class AceStepV15BaseResult(TypedDict, total=False):
    """Inference result for curated model `runware:ace-step@v1.5-base` (slug: ace-step-v1-5-base)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class ControlnetPreprocessNormalbaeParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@normalbae` (slug: controlnet-preprocess-normalbae)."""

    model: Literal['runware:controlnet-preprocess@normalbae']
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessNormalbaeResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@normalbae` (slug: controlnet-preprocess-normalbae)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class ControlnetPreprocessMlsdParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@mlsd` (slug: controlnet-preprocess-mlsd)."""

    model: Literal['runware:controlnet-preprocess@mlsd']
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessMlsdResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@mlsd` (slug: controlnet-preprocess-mlsd)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class MediapipeNoseMeshParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@13` (slug: mediapipe-nose-mesh)."""

    model: Literal['runware:35@13']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class MediapipeNoseMeshResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@13` (slug: mediapipe-nose-mesh)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class HidreamI1FastParams(TypedDict, total=False):
    """Inference params for curated model `runware:97@3` (slug: hidream-i1-fast)."""

    model: Literal['runware:97@3']
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class HidreamI1FastResult(TypedDict, total=False):
    """Inference result for curated model `runware:97@3` (slug: hidream-i1-fast)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BriaRmbgV20OpenParams(TypedDict, total=False):
    """Inference params for curated model `runware:110@1` (slug: bria-rmbg-v2-0-open)."""

    model: Literal['runware:110@1']
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BriaRmbgV20OpenResult(TypedDict, total=False):
    """Inference result for curated model `runware:110@1` (slug: bria-rmbg-v2-0-open)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class ControlnetPreprocessTileParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@tile` (slug: controlnet-preprocess-tile)."""

    model: Literal['runware:controlnet-preprocess@tile']
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessTileResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@tile` (slug: controlnet-preprocess-tile)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class Yolov8sFaceParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@2` (slug: yolov8s-face)."""

    model: Literal['runware:35@2']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class Yolov8sFaceResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@2` (slug: yolov8s-face)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class RealEsrganParams(TypedDict, total=False):
    """Inference params for curated model `runware:504@1` (slug: real-esrgan)."""

    model: Literal['runware:504@1']
    upscaleFactor: NotRequired[Literal[2, 4]]
    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class RealEsrganResult(TypedDict, total=False):
    """Inference result for curated model `runware:504@1` (slug: real-esrgan)."""

    taskType: Literal['upscale']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class UpscaleResult(TypedDict, total=False):
    """Canonical result shape for `upscale` tasks."""

    taskType: Literal['upscale']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class ControlnetPreprocessLineartAnimeParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@lineart-anime` (slug: controlnet-preprocess-lineart-anime)."""

    model: Literal['runware:controlnet-preprocess@lineart-anime']
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessLineartAnimeResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@lineart-anime` (slug: controlnet-preprocess-lineart-anime)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class MediapipeNoseLipsMeshParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@12` (slug: mediapipe-nose-lips-mesh)."""

    model: Literal['runware:35@12']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class MediapipeNoseLipsMeshResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@12` (slug: mediapipe-nose-lips-mesh)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class BirefnetGeneralResolution512x512Fp16Params(TypedDict, total=False):
    """Inference params for curated model `runware:112@6` (slug: birefnet-general-resolution-512x512-fp16)."""

    model: Literal['runware:112@6']
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BirefnetGeneralResolution512x512Fp16Result(TypedDict, total=False):
    """Inference result for curated model `runware:112@6` (slug: birefnet-general-resolution-512x512-fp16)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class ClarityParams(TypedDict, total=False):
    """Inference params for curated model `runware:500@1` (slug: clarity)."""

    model: Literal['runware:500@1']
    upscaleFactor: NotRequired[Literal[2]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class ClarityResult(TypedDict, total=False):
    """Inference result for curated model `runware:500@1` (slug: clarity)."""

    taskType: Literal['upscale']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class AceStepV15TurboParams(TypedDict, total=False):
    """Inference params for curated model `runware:ace-step@v1.5-turbo` (slug: ace-step-v1-5-turbo)."""

    model: Literal['runware:ace-step@v1.5-turbo']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    duration: NotRequired[float]
    seed: NotRequired[int]
    steps: NotRequired[int]
    strength: NotRequired[float]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class AceStepV15TurboResult(TypedDict, total=False):
    """Inference result for curated model `runware:ace-step@v1.5-turbo` (slug: ace-step-v1-5-turbo)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class ControlnetPreprocessSegParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@seg` (slug: controlnet-preprocess-seg)."""

    model: Literal['runware:controlnet-preprocess@seg']
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessSegResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@seg` (slug: controlnet-preprocess-seg)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class Yolov8nPersonSegParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@4` (slug: yolov8n-person-seg)."""

    model: Literal['runware:35@4']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class Yolov8nPersonSegResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@4` (slug: yolov8n-person-seg)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class Yolov8sPersonSegParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@5` (slug: yolov8s-person-seg)."""

    model: Literal['runware:35@5']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class Yolov8sPersonSegResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@5` (slug: yolov8s-person-seg)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class AceStepV15XlBaseParams(TypedDict, total=False):
    """Inference params for curated model `runware:ace-step@v1.5-xl-base` (slug: ace-step-v1-5-xl-base)."""

    model: Literal['runware:ace-step@v1.5-xl-base']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    duration: NotRequired[float]
    seed: NotRequired[int]
    steps: NotRequired[int]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    settings: NotRequired[dict[str, object]]
    advancedFeatures: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class AceStepV15XlBaseResult(TypedDict, total=False):
    """Inference result for curated model `runware:ace-step@v1.5-xl-base` (slug: ace-step-v1-5-xl-base)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class AceStepV15XlSftParams(TypedDict, total=False):
    """Inference params for curated model `runware:ace-step@v1.5-xl-sft` (slug: ace-step-v1-5-xl-sft)."""

    model: Literal['runware:ace-step@v1.5-xl-sft']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    duration: NotRequired[float]
    seed: NotRequired[int]
    steps: NotRequired[int]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    settings: NotRequired[dict[str, object]]
    advancedFeatures: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class AceStepV15XlSftResult(TypedDict, total=False):
    """Inference result for curated model `runware:ace-step@v1.5-xl-sft` (slug: ace-step-v1-5-xl-sft)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class ControlnetPreprocessCannyParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@canny` (slug: controlnet-preprocess-canny)."""

    model: Literal['runware:controlnet-preprocess@canny']
    settings: NotRequired[dict[str, object]]
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessCannyResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@canny` (slug: controlnet-preprocess-canny)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class HidreamI1DevParams(TypedDict, total=False):
    """Inference params for curated model `runware:97@2` (slug: hidream-i1-dev)."""

    model: Literal['runware:97@2']
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class HidreamI1DevResult(TypedDict, total=False):
    """Inference result for curated model `runware:97@2` (slug: hidream-i1-dev)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class OpenAgeDetectionParams(TypedDict, total=False):
    """Inference params for curated model `runware:154@1` (slug: open-age-detection)."""

    model: Literal['runware:154@1']
    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class OpenAgeDetectionResult(TypedDict, total=False):
    """Inference result for curated model `runware:154@1` (slug: open-age-detection)."""

    taskType: Literal['caption']
    taskUUID: str
    cost: NotRequired[float]
    structuredData: dict[str, object]

class Qwen25Vl7bAgeDetectorParams(TypedDict, total=False):
    """Inference params for curated model `runware:152@50` (slug: qwen2-5-vl-7b-age-detector)."""

    model: Literal['runware:152@50']
    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class Qwen25Vl7bAgeDetectorResult(TypedDict, total=False):
    """Inference result for curated model `runware:152@50` (slug: qwen2-5-vl-7b-age-detector)."""

    taskType: Literal['caption']
    taskUUID: str
    cost: NotRequired[float]
    structuredData: dict[str, object]

class HidreamI1FullParams(TypedDict, total=False):
    """Inference params for curated model `runware:97@1` (slug: hidream-i1-full)."""

    model: Literal['runware:97@1']
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class HidreamI1FullResult(TypedDict, total=False):
    """Inference result for curated model `runware:97@1` (slug: hidream-i1-full)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ControlnetPreprocessScribbleParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@scribble` (slug: controlnet-preprocess-scribble)."""

    model: Literal['runware:controlnet-preprocess@scribble']
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessScribbleResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@scribble` (slug: controlnet-preprocess-scribble)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class BirefnetV1BaseParams(TypedDict, total=False):
    """Inference params for curated model `runware:112@1` (slug: birefnet-v1-base)."""

    model: Literal['runware:112@1']
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BirefnetV1BaseResult(TypedDict, total=False):
    """Inference result for curated model `runware:112@1` (slug: birefnet-v1-base)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class MediapipeEyesLipsMeshParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@10` (slug: mediapipe-eyes-lips-mesh)."""

    model: Literal['runware:35@10']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class MediapipeEyesLipsMeshResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@10` (slug: mediapipe-eyes-lips-mesh)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class RembgV14Params(TypedDict, total=False):
    """Inference params for curated model `runware:109@1` (slug: rembg-v1-4)."""

    model: Literal['runware:109@1']
    settings: NotRequired[dict[str, object]]
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class RembgV14Result(TypedDict, total=False):
    """Inference result for curated model `runware:109@1` (slug: rembg-v1-4)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class SwinirParams(TypedDict, total=False):
    """Inference params for curated model `runware:503@1` (slug: swinir)."""

    model: Literal['runware:503@1']
    upscaleFactor: NotRequired[Literal[2, 4]]
    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class SwinirResult(TypedDict, total=False):
    """Inference result for curated model `runware:503@1` (slug: swinir)."""

    taskType: Literal['upscale']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class BirefnetDisParams(TypedDict, total=False):
    """Inference params for curated model `runware:112@3` (slug: birefnet-dis)."""

    model: Literal['runware:112@3']
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BirefnetDisResult(TypedDict, total=False):
    """Inference result for curated model `runware:112@3` (slug: birefnet-dis)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class AceStepV15XlTurboParams(TypedDict, total=False):
    """Inference params for curated model `runware:ace-step@v1.5-xl-turbo` (slug: ace-step-v1-5-xl-turbo)."""

    model: Literal['runware:ace-step@v1.5-xl-turbo']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    duration: NotRequired[float]
    seed: NotRequired[int]
    steps: NotRequired[int]
    strength: NotRequired[float]
    settings: NotRequired[dict[str, object]]
    advancedFeatures: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class AceStepV15XlTurboResult(TypedDict, total=False):
    """Inference result for curated model `runware:ace-step@v1.5-xl-turbo` (slug: ace-step-v1-5-xl-turbo)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class ControlnetPreprocessOpenposeParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@openpose` (slug: controlnet-preprocess-openpose)."""

    model: Literal['runware:controlnet-preprocess@openpose']
    settings: NotRequired[dict[str, object]]
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessOpenposeResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@openpose` (slug: controlnet-preprocess-openpose)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class ControlnetPreprocessDepthParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@depth` (slug: controlnet-preprocess-depth)."""

    model: Literal['runware:controlnet-preprocess@depth']
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessDepthResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@depth` (slug: controlnet-preprocess-depth)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class CcsrParams(TypedDict, total=False):
    """Inference params for curated model `runware:501@1` (slug: ccsr)."""

    model: Literal['runware:501@1']
    upscaleFactor: NotRequired[Literal[2]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class CcsrResult(TypedDict, total=False):
    """Inference result for curated model `runware:501@1` (slug: ccsr)."""

    taskType: Literal['upscale']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class ObjectEraserParams(TypedDict, total=False):
    """Inference params for curated model `runware:300@1` (slug: object-eraser)."""

    model: Literal['runware:300@1']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    seed: NotRequired[int]
    steps: NotRequired[int]
    CFGScale: NotRequired[float]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ObjectEraserResult(TypedDict, total=False):
    """Inference result for curated model `runware:300@1` (slug: object-eraser)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Kandinsky50ImageLiteParams(TypedDict, total=False):
    """Inference params for curated model `runware:kandinsky-5.0-image-lite@1` (slug: kandinsky-5-0-image-lite)."""

    model: Literal['runware:kandinsky-5.0-image-lite@1']
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DPM++ 2M Karras', 'DPM++ SDE Karras', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'Euler', 'Euler a', 'Euler Trailing', 'LCM', 'DDIM', 'DDPM', 'PNDM', 'UniPC']]
    CFGScale: NotRequired[float]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Kandinsky50ImageLiteResult(TypedDict, total=False):
    """Inference result for curated model `runware:kandinsky-5.0-image-lite@1` (slug: kandinsky-5-0-image-lite)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class MediapipeFaceMeshEyesOnlyParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@9` (slug: mediapipe-face-mesh-eyes-only)."""

    model: Literal['runware:35@9']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class MediapipeFaceMeshEyesOnlyResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@9` (slug: mediapipe-face-mesh-eyes-only)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class MediapipeNoseEyesMeshParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@11` (slug: mediapipe-nose-eyes-mesh)."""

    model: Literal['runware:35@11']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class MediapipeNoseEyesMeshResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@11` (slug: mediapipe-nose-eyes-mesh)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class MediapipeEyesMeshParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@15` (slug: mediapipe-eyes-mesh)."""

    model: Literal['runware:35@15']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class MediapipeEyesMeshResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@15` (slug: mediapipe-eyes-mesh)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class Yolov8nFaceParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@1` (slug: yolov8n-face)."""

    model: Literal['runware:35@1']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class Yolov8nFaceResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@1` (slug: yolov8n-face)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class ControlnetPreprocessSoftedgeParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@softedge` (slug: controlnet-preprocess-softedge)."""

    model: Literal['runware:controlnet-preprocess@softedge']
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessSoftedgeResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@softedge` (slug: controlnet-preprocess-softedge)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class StableDiffusionLatentUpscalerParams(TypedDict, total=False):
    """Inference params for curated model `runware:502@1` (slug: stable-diffusion-latent-upscaler)."""

    model: Literal['runware:502@1']
    upscaleFactor: NotRequired[Literal[2]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class StableDiffusionLatentUpscalerResult(TypedDict, total=False):
    """Inference result for curated model `runware:502@1` (slug: stable-diffusion-latent-upscaler)."""

    taskType: Literal['upscale']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class BirefnetMassiveTrDis5kTrTesParams(TypedDict, total=False):
    """Inference params for curated model `runware:112@8` (slug: birefnet-massive-tr-dis5k-tr-tes)."""

    model: Literal['runware:112@8']
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BirefnetMassiveTrDis5kTrTesResult(TypedDict, total=False):
    """Inference result for curated model `runware:112@8` (slug: birefnet-massive-tr-dis5k-tr-tes)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class BirefnetHrsodDhuParams(TypedDict, total=False):
    """Inference params for curated model `runware:112@7` (slug: birefnet-hrsod-dhu)."""

    model: Literal['runware:112@7']
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BirefnetHrsodDhuResult(TypedDict, total=False):
    """Inference result for curated model `runware:112@7` (slug: birefnet-hrsod-dhu)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class MediapipeFaceMeshParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@8` (slug: mediapipe-face-mesh)."""

    model: Literal['runware:35@8']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class MediapipeFaceMeshResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@8` (slug: mediapipe-face-mesh)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class ControlnetPreprocessShuffleParams(TypedDict, total=False):
    """Inference params for curated model `runware:controlnet-preprocess@shuffle` (slug: controlnet-preprocess-shuffle)."""

    model: Literal['runware:controlnet-preprocess@shuffle']
    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class ControlnetPreprocessShuffleResult(TypedDict, total=False):
    """Inference result for curated model `runware:controlnet-preprocess@shuffle` (slug: controlnet-preprocess-shuffle)."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    cost: NotRequired[float]
    guideImageUUID: str
    guideImageURL: NotRequired[str]
    guideImageBase64Data: NotRequired[str]
    guideImageDataURI: NotRequired[str]
    inputImageUUID: str

class MediapipeLipsMeshParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@14` (slug: mediapipe-lips-mesh)."""

    model: Literal['runware:35@14']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class MediapipeLipsMeshResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@14` (slug: mediapipe-lips-mesh)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class MediapipeFaceFullParams(TypedDict, total=False):
    """Inference params for curated model `runware:35@6` (slug: mediapipe-face-full)."""

    model: Literal['runware:35@6']
    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class MediapipeFaceFullResult(TypedDict, total=False):
    """Inference result for curated model `runware:35@6` (slug: mediapipe-face-full)."""

    taskType: Literal['imageMasking']
    taskUUID: str
    cost: NotRequired[float]
    maskImageUUID: str
    maskImageURL: NotRequired[str]
    maskImageBase64Data: NotRequired[str]
    maskImageDataURI: NotRequired[str]
    detections: list[dict[str, object]]
    inputImageUUID: str

class BirefnetGeneralParams(TypedDict, total=False):
    """Inference params for curated model `runware:112@5` (slug: birefnet-general)."""

    model: Literal['runware:112@5']
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BirefnetGeneralResult(TypedDict, total=False):
    """Inference result for curated model `runware:112@5` (slug: birefnet-general)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class BirefnetMattingParams(TypedDict, total=False):
    """Inference params for curated model `runware:112@9` (slug: birefnet-matting)."""

    model: Literal['runware:112@9']
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BirefnetMattingResult(TypedDict, total=False):
    """Inference result for curated model `runware:112@9` (slug: birefnet-matting)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class TwinflowZImageTurboParams(TypedDict, total=False):
    """Inference params for curated model `runware:twinflow-z-image-turbo@0` (slug: twinflow-z-image-turbo)."""

    model: Literal['runware:twinflow-z-image-turbo@0']
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleration: NotRequired[Literal['none', 'low', 'medium', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class TwinflowZImageTurboResult(TypedDict, total=False):
    """Inference result for curated model `runware:twinflow-z-image-turbo@0` (slug: twinflow-z-image-turbo)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class MinimaxM27HighspeedParams(TypedDict, total=False):
    """Inference params for curated model `minimax:m2.7@highspeed` (slug: minimax-m2-7-highspeed)."""

    model: Literal['minimax:m2.7@highspeed']
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class MinimaxM27HighspeedResult(TypedDict, total=False):
    """Inference result for curated model `minimax:m2.7@highspeed` (slug: minimax-m2-7-highspeed)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class TextInferenceResult(TypedDict, total=False):
    """Canonical result shape for `textInference` tasks."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class MinimaxM27Params(TypedDict, total=False):
    """Inference params for curated model `minimax:m2.7@0` (slug: minimax-m2-7)."""

    model: Literal['minimax:m2.7@0']
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class MinimaxM27Result(TypedDict, total=False):
    """Inference result for curated model `minimax:m2.7@0` (slug: minimax-m2-7)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class MinimaxM3Params(TypedDict, total=False):
    """Inference params for curated model `minimax:m3@0` (slug: minimax-m3)."""

    model: Literal['minimax:m3@0']
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class MinimaxM3Result(TypedDict, total=False):
    """Inference result for curated model `minimax:m3@0` (slug: minimax-m3)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]
    reasoningContent: NotRequired[str]

class MinimaxMusic26Params(TypedDict, total=False):
    """Inference params for curated model `minimax:music@2.6` (slug: minimax-music-2-6)."""

    model: Literal['minimax:music@2.6']
    positivePrompt: NotRequired[str]
    negativePrompt: NotRequired[str]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class MinimaxMusic26Result(TypedDict, total=False):
    """Inference result for curated model `minimax:music@2.6` (slug: minimax-music-2-6)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class MinimaxHailuo23Params(TypedDict, total=False):
    """Inference params for curated model `minimax:4@1` (slug: minimax-hailuo-2-3)."""

    model: Literal['minimax:4@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[float]
    fps: NotRequired[Literal[25]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class MinimaxHailuo23Result(TypedDict, total=False):
    """Inference result for curated model `minimax:4@1` (slug: minimax-hailuo-2-3)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class MinimaxSpeech28Params(TypedDict, total=False):
    """Inference params for curated model `minimax:speech@2.8` (slug: minimax-speech-2-8)."""

    model: Literal['minimax:speech@2.8']
    audioSettings: NotRequired[dict[str, object]]
    speech: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]

class MinimaxSpeech28Result(TypedDict, total=False):
    """Inference result for curated model `minimax:speech@2.8` (slug: minimax-speech-2-8)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class Minimax01LiveParams(TypedDict, total=False):
    """Inference params for curated model `minimax:2@3` (slug: minimax-01-live)."""

    model: Literal['minimax:2@3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[6]]
    fps: NotRequired[Literal[25]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Minimax01LiveResult(TypedDict, total=False):
    """Inference result for curated model `minimax:2@3` (slug: minimax-01-live)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Minimax01DirectorParams(TypedDict, total=False):
    """Inference params for curated model `minimax:2@1` (slug: minimax-01-director)."""

    model: Literal['minimax:2@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[6]]
    fps: NotRequired[Literal[25]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Minimax01DirectorResult(TypedDict, total=False):
    """Inference result for curated model `minimax:2@1` (slug: minimax-01-director)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class MinimaxHailuo23FastParams(TypedDict, total=False):
    """Inference params for curated model `minimax:4@2` (slug: minimax-hailuo-2-3-fast)."""

    model: Literal['minimax:4@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[float]
    fps: NotRequired[Literal[25]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class MinimaxHailuo23FastResult(TypedDict, total=False):
    """Inference result for curated model `minimax:4@2` (slug: minimax-hailuo-2-3-fast)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class MinimaxHailuo02Params(TypedDict, total=False):
    """Inference params for curated model `minimax:3@1` (slug: minimax-hailuo-02)."""

    model: Literal['minimax:3@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[float]
    fps: NotRequired[Literal[25]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class MinimaxHailuo02Result(TypedDict, total=False):
    """Inference result for curated model `minimax:3@1` (slug: minimax-hailuo-02)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class MinimaxM25Params(TypedDict, total=False):
    """Inference params for curated model `minimax:m2.5@0` (slug: minimax-m2-5)."""

    model: Literal['minimax:m2.5@0']
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class MinimaxM25Result(TypedDict, total=False):
    """Inference result for curated model `minimax:m2.5@0` (slug: minimax-m2-5)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]
    reasoningContent: NotRequired[str]

class Minimax01Params(TypedDict, total=False):
    """Inference params for curated model `minimax:1@1` (slug: minimax-01)."""

    model: Literal['minimax:1@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[6]]
    fps: NotRequired[Literal[25]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Minimax01Result(TypedDict, total=False):
    """Inference result for curated model `minimax:1@1` (slug: minimax-01)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class MinimaxMusicCoverParams(TypedDict, total=False):
    """Inference params for curated model `minimax:music@cover` (slug: minimax-music-cover)."""

    model: Literal['minimax:music@cover']
    inputs: dict[str, object]
    positivePrompt: str
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class MinimaxMusicCoverResult(TypedDict, total=False):
    """Inference result for curated model `minimax:music@cover` (slug: minimax-music-cover)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class DeepseekV4FlashParams(TypedDict, total=False):
    """Inference params for curated model `deepseek:v4@flash` (slug: deepseek-v4-flash)."""

    model: Literal['deepseek:v4@flash']
    outputFormat: NotRequired[Literal['TEXT', 'JSON']]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    jsonSchema: NotRequired[dict[str, object] | str]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class DeepseekV4FlashResult(TypedDict, total=False):
    """Inference result for curated model `deepseek:v4@flash` (slug: deepseek-v4-flash)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class DeepseekV4ProParams(TypedDict, total=False):
    """Inference params for curated model `deepseek:v4@pro` (slug: deepseek-v4-pro)."""

    model: Literal['deepseek:v4@pro']
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class DeepseekV4ProResult(TypedDict, total=False):
    """Inference result for curated model `deepseek:v4@pro` (slug: deepseek-v4-pro)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class PrunaaiPVideoParams(TypedDict, total=False):
    """Inference params for curated model `prunaai:p-video@0` (slug: prunaai-p-video)."""

    model: Literal['prunaai:p-video@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p']]
    duration: NotRequired[int]
    fps: NotRequired[Literal[24, 48]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PrunaaiPVideoResult(TypedDict, total=False):
    """Inference result for curated model `prunaai:p-video@0` (slug: prunaai-p-video)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PrunaaiPImageParams(TypedDict, total=False):
    """Inference params for curated model `prunaai:1@1` (slug: prunaai-p-image)."""

    model: Literal['prunaai:1@1']
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PrunaaiPImageResult(TypedDict, total=False):
    """Inference result for curated model `prunaai:1@1` (slug: prunaai-p-image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PrunaaiPVideoAnimateParams(TypedDict, total=False):
    """Inference params for curated model `prunaai:p-video@animate` (slug: prunaai-p-video-animate)."""

    model: Literal['prunaai:p-video@animate']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    resolution: NotRequired[Literal['720p', '1080p']]
    fps: NotRequired[Literal[24, 48]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PrunaaiPVideoAnimateResult(TypedDict, total=False):
    """Inference result for curated model `prunaai:p-video@animate` (slug: prunaai-p-video-animate)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PrunaaiPImageUpscaleParams(TypedDict, total=False):
    """Inference params for curated model `prunaai:p-image@upscale` (slug: prunaai-p-image-upscale)."""

    model: Literal['prunaai:p-image@upscale']
    settings: NotRequired[dict[str, object]]
    targetMegapixels: NotRequired[int]
    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class PrunaaiPImageUpscaleResult(TypedDict, total=False):
    """Inference result for curated model `prunaai:p-image@upscale` (slug: prunaai-p-image-upscale)."""

    taskType: Literal['upscale']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class PrunaaiPImageTryOnParams(TypedDict, total=False):
    """Inference params for curated model `prunaai:p-image@try-on` (slug: prunaai-p-image-try-on)."""

    model: Literal['prunaai:p-image@try-on']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PrunaaiPImageTryOnResult(TypedDict, total=False):
    """Inference result for curated model `prunaai:p-image@try-on` (slug: prunaai-p-image-try-on)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PrunaaiPImageEditParams(TypedDict, total=False):
    """Inference params for curated model `prunaai:2@1` (slug: prunaai-p-image-edit)."""

    model: Literal['prunaai:2@1']
    inputs: dict[str, object]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PrunaaiPImageEditResult(TypedDict, total=False):
    """Inference result for curated model `prunaai:2@1` (slug: prunaai-p-image-edit)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PrunaaiPVideoAvatarParams(TypedDict, total=False):
    """Inference params for curated model `prunaai:p-video@avatar` (slug: prunaai-p-video-avatar)."""

    model: Literal['prunaai:p-video@avatar']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    resolution: NotRequired[Literal['720p', '1080p']]
    seed: NotRequired[int]
    speech: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PrunaaiPVideoAvatarResult(TypedDict, total=False):
    """Inference result for curated model `prunaai:p-video@avatar` (slug: prunaai-p-video-avatar)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PrunaaiPVideoReplaceParams(TypedDict, total=False):
    """Inference params for curated model `prunaai:p-video@replace` (slug: prunaai-p-video-replace)."""

    model: Literal['prunaai:p-video@replace']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    resolution: NotRequired[Literal['720p', '1080p']]
    fps: NotRequired[Literal[24, 48]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PrunaaiPVideoReplaceResult(TypedDict, total=False):
    """Inference result for curated model `prunaai:p-video@replace` (slug: prunaai-p-video-replace)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RundiffusionJuggernautLightningFluxParams(TypedDict, total=False):
    """Inference params for curated model `rundiffusion:110@101` (slug: rundiffusion-juggernaut-lightning-flux)."""

    model: Literal['rundiffusion:110@101']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RundiffusionJuggernautLightningFluxResult(TypedDict, total=False):
    """Inference result for curated model `rundiffusion:110@101` (slug: rundiffusion-juggernaut-lightning-flux)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RundiffusionJuggernautZParams(TypedDict, total=False):
    """Inference params for curated model `rundiffusion:200@100` (slug: rundiffusion-juggernaut-z)."""

    model: Literal['rundiffusion:200@100']
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RundiffusionJuggernautZResult(TypedDict, total=False):
    """Inference result for curated model `rundiffusion:200@100` (slug: rundiffusion-juggernaut-z)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RundiffusionJuggernautBaseFluxParams(TypedDict, total=False):
    """Inference params for curated model `rundiffusion:120@100` (slug: rundiffusion-juggernaut-base-flux)."""

    model: Literal['rundiffusion:120@100']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    layerDiffuse: NotRequired[bool]
    pulid: NotRequired[dict[str, object]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RundiffusionJuggernautBaseFluxResult(TypedDict, total=False):
    """Inference result for curated model `rundiffusion:120@100` (slug: rundiffusion-juggernaut-base-flux)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RundiffusionJuggernautProFluxParams(TypedDict, total=False):
    """Inference params for curated model `rundiffusion:130@100` (slug: rundiffusion-juggernaut-pro-flux)."""

    model: Literal['rundiffusion:130@100']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    layerDiffuse: NotRequired[bool]
    pulid: NotRequired[dict[str, object]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RundiffusionJuggernautProFluxResult(TypedDict, total=False):
    """Inference result for curated model `rundiffusion:130@100` (slug: rundiffusion-juggernaut-pro-flux)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SyncReact1Params(TypedDict, total=False):
    """Inference params for curated model `sync:react-1@1` (slug: sync-react-1)."""

    model: Literal['sync:react-1@1']
    inputs: dict[str, object]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SyncReact1Result(TypedDict, total=False):
    """Inference result for curated model `sync:react-1@1` (slug: sync-react-1)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SyncLipsync2Params(TypedDict, total=False):
    """Inference params for curated model `sync:lipsync-2@1` (slug: sync-lipsync-2)."""

    model: Literal['sync:lipsync-2@1']
    inputs: dict[str, object]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SyncLipsync2Result(TypedDict, total=False):
    """Inference result for curated model `sync:lipsync-2@1` (slug: sync-lipsync-2)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Sync3Params(TypedDict, total=False):
    """Inference params for curated model `sync:lipsync@3` (slug: sync-3)."""

    model: Literal['sync:lipsync@3']
    inputs: dict[str, object]
    speech: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Sync3Result(TypedDict, total=False):
    """Inference result for curated model `sync:lipsync@3` (slug: sync-3)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SyncLipsync2ProParams(TypedDict, total=False):
    """Inference params for curated model `sync:lipsync-2-pro@1` (slug: sync-lipsync-2-pro)."""

    model: Literal['sync:lipsync-2-pro@1']
    inputs: dict[str, object]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SyncLipsync2ProResult(TypedDict, total=False):
    """Inference result for curated model `sync:lipsync-2-pro@1` (slug: sync-lipsync-2-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PicsartImageVectorizerParams(TypedDict, total=False):
    """Inference params for curated model `picsart:1@1` (slug: picsart-image-vectorizer)."""

    model: Literal['picsart:1@1']
    inputs: dict[str, object]
    taskType: Literal['vectorize']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['SVG']]
    deliveryMethod: NotRequired[str]

class PicsartImageVectorizerResult(TypedDict, total=False):
    """Inference result for curated model `picsart:1@1` (slug: picsart-image-vectorizer)."""

    taskType: Literal['vectorize']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class VectorizeResult(TypedDict, total=False):
    """Canonical result shape for `vectorize` tasks."""

    taskType: Literal['vectorize']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class MetaLlava16Mistral7bParams(TypedDict, total=False):
    """Inference params for curated model `runware:150@2` (slug: meta-llava-1-6-mistral-7b)."""

    model: Literal['runware:150@2']
    prompt: NotRequired[str]
    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class MetaLlava16Mistral7bResult(TypedDict, total=False):
    """Inference result for curated model `runware:150@2` (slug: meta-llava-1-6-mistral-7b)."""

    taskType: Literal['caption']
    taskUUID: str
    cost: NotRequired[float]
    text: str

class MetaSam3dObjectsParams(TypedDict, total=False):
    """Inference params for curated model `meta:sam@3d` (slug: meta-sam-3d-objects)."""

    model: Literal['meta:sam@3d']
    inputs: dict[str, object]
    positivePrompt: str
    seed: NotRequired[int]
    taskType: Literal['3dInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['GLB']]
    deliveryMethod: NotRequired[str]

class MetaSam3dObjectsResult(TypedDict, total=False):
    """Inference result for curated model `meta:sam@3d` (slug: meta-sam-3d-objects)."""

    taskType: Literal['3dInference']
    taskUUID: str
    cost: NotRequired[float]
    outputs: dict[str, object]
    seed: NotRequired[int]

class ThreeDInferenceResult(TypedDict, total=False):
    """Canonical result shape for `3dInference` tasks."""

    taskType: Literal['3dInference']
    taskUUID: str
    cost: NotRequired[float]
    outputs: dict[str, object]
    seed: NotRequired[int]

class ViduQ1Params(TypedDict, total=False):
    """Inference params for curated model `vidu:1@1` (slug: vidu-q1)."""

    model: Literal['vidu:1@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[4, 5]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ViduQ1Result(TypedDict, total=False):
    """Inference result for curated model `vidu:1@1` (slug: vidu-q1)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ViduQ2TurboParams(TypedDict, total=False):
    """Inference params for curated model `vidu:3@2` (slug: vidu-q2-turbo)."""

    model: Literal['vidu:3@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[float]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ViduQ2TurboResult(TypedDict, total=False):
    """Inference result for curated model `vidu:3@2` (slug: vidu-q2-turbo)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Vidu15Params(TypedDict, total=False):
    """Inference params for curated model `vidu:1@5` (slug: vidu-1-5)."""

    model: Literal['vidu:1@5']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[4, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Vidu15Result(TypedDict, total=False):
    """Inference result for curated model `vidu:1@5` (slug: vidu-1-5)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ViduQ1ImageParams(TypedDict, total=False):
    """Inference params for curated model `vidu:q1@image` (slug: vidu-q1-image)."""

    model: Literal['vidu:q1@image']
    inputs: dict[str, object]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ViduQ1ImageResult(TypedDict, total=False):
    """Inference result for curated model `vidu:q1@image` (slug: vidu-q1-image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Vidu20Params(TypedDict, total=False):
    """Inference params for curated model `vidu:2@0` (slug: vidu-2-0)."""

    model: Literal['vidu:2@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[4, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Vidu20Result(TypedDict, total=False):
    """Inference result for curated model `vidu:2@0` (slug: vidu-2-0)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ViduQ3TurboParams(TypedDict, total=False):
    """Inference params for curated model `vidu:4@2` (slug: vidu-q3-turbo)."""

    model: Literal['vidu:4@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: int
    height: int
    duration: NotRequired[int]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ViduQ3TurboResult(TypedDict, total=False):
    """Inference result for curated model `vidu:4@2` (slug: vidu-q3-turbo)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ViduQ1ClassicParams(TypedDict, total=False):
    """Inference params for curated model `vidu:1@0` (slug: vidu-q1-classic)."""

    model: Literal['vidu:1@0']
    inputs: NotRequired[dict[str, object]]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ViduQ1ClassicResult(TypedDict, total=False):
    """Inference result for curated model `vidu:1@0` (slug: vidu-q1-classic)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ViduQ3Params(TypedDict, total=False):
    """Inference params for curated model `vidu:4@1` (slug: vidu-q3)."""

    model: Literal['vidu:4@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['360p', '540p', '720p', '1080p']]
    duration: NotRequired[int]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ViduQ3Result(TypedDict, total=False):
    """Inference result for curated model `vidu:4@1` (slug: vidu-q3)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ViduQ2ProParams(TypedDict, total=False):
    """Inference params for curated model `vidu:3@1` (slug: vidu-q2-pro)."""

    model: Literal['vidu:3@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[float]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ViduQ2ProResult(TypedDict, total=False):
    """Inference result for curated model `vidu:3@1` (slug: vidu-q2-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class StabilityaiStableDiffusion3Params(TypedDict, total=False):
    """Inference params for curated model `runware:5@1` (slug: stabilityai-stable-diffusion-3)."""

    model: Literal['runware:5@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class StabilityaiStableDiffusion3Result(TypedDict, total=False):
    """Inference result for curated model `runware:5@1` (slug: stabilityai-stable-diffusion-3)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class StabilityaiStableDiffusionXlV10VaeFixParams(TypedDict, total=False):
    """Inference params for curated model `civitai:101055@128078` (slug: stabilityai-stable-diffusion-xl-v1-0-vae-fix)."""

    model: Literal['civitai:101055@128078']
    width: int
    height: int
    steps: NotRequired[int]
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    seed: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    refiner: NotRequired[dict[str, object]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    photoMaker: NotRequired[dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class StabilityaiStableDiffusionXlV10VaeFixResult(TypedDict, total=False):
    """Inference result for curated model `civitai:101055@128078` (slug: stabilityai-stable-diffusion-xl-v1-0-vae-fix)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwenImageLayeredParams(TypedDict, total=False):
    """Inference params for curated model `alibaba:qwen-image@layered` (slug: alibaba-qwen-image-layered)."""

    model: Literal['alibaba:qwen-image@layered']
    outputFormat: NotRequired[Literal['TIFF']]
    inputs: dict[str, object]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaQwenImageLayeredResult(TypedDict, total=False):
    """Inference result for curated model `alibaba:qwen-image@layered` (slug: alibaba-qwen-image-layered)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwen25Vl3bInstructParams(TypedDict, total=False):
    """Inference params for curated model `runware:152@1` (slug: alibaba-qwen2-5-vl-3b-instruct)."""

    model: Literal['runware:152@1']
    prompt: NotRequired[str]
    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class AlibabaQwen25Vl3bInstructResult(TypedDict, total=False):
    """Inference result for curated model `runware:152@1` (slug: alibaba-qwen2-5-vl-3b-instruct)."""

    taskType: Literal['caption']
    taskUUID: str
    cost: NotRequired[float]
    text: str

class AlibabaWan26Params(TypedDict, total=False):
    """Inference params for curated model `alibaba:wan@2.6` (slug: alibaba-wan2-6)."""

    model: Literal['alibaba:wan@2.6']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p']]
    duration: NotRequired[Literal[5, 10, 15]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaWan26Result(TypedDict, total=False):
    """Inference result for curated model `alibaba:wan@2.6` (slug: alibaba-wan2-6)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwen3Tts17bCustomvoiceParams(TypedDict, total=False):
    """Inference params for curated model `alibaba:qwen@3-tts-1.7b-customvoice` (slug: alibaba-qwen3-tts-1-7b-customvoice)."""

    model: Literal['alibaba:qwen@3-tts-1.7b-customvoice']
    positivePrompt: NotRequired[str]
    speech: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class AlibabaQwen3Tts17bCustomvoiceResult(TypedDict, total=False):
    """Inference result for curated model `alibaba:qwen@3-tts-1.7b-customvoice` (slug: alibaba-qwen3-tts-1-7b-customvoice)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class AlibabaWan27ImageParams(TypedDict, total=False):
    """Inference params for curated model `alibaba:wan@2.7-image` (slug: alibaba-wan2-7-image)."""

    model: Literal['alibaba:wan@2.7-image']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaWan27ImageResult(TypedDict, total=False):
    """Inference result for curated model `alibaba:wan@2.7-image` (slug: alibaba-wan2-7-image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwen3527bParams(TypedDict, total=False):
    """Inference params for curated model `alibaba:qwen@3.5-27b` (slug: alibaba-qwen3-5-27b)."""

    model: Literal['alibaba:qwen@3.5-27b']
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class AlibabaQwen3527bResult(TypedDict, total=False):
    """Inference result for curated model `alibaba:qwen@3.5-27b` (slug: alibaba-qwen3-5-27b)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class AlibabaZImageParams(TypedDict, total=False):
    """Inference params for curated model `runware:z-image@0` (slug: alibaba-z-image)."""

    model: Literal['runware:z-image@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaZImageResult(TypedDict, total=False):
    """Inference result for curated model `runware:z-image@0` (slug: alibaba-z-image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwenImageParams(TypedDict, total=False):
    """Inference params for curated model `runware:108@1` (slug: alibaba-qwen-image)."""

    model: Literal['runware:108@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    settings: NotRequired[dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaQwenImageResult(TypedDict, total=False):
    """Inference result for curated model `runware:108@1` (slug: alibaba-qwen-image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaWan27Params(TypedDict, total=False):
    """Inference params for curated model `alibaba:wan@2.7` (slug: alibaba-wan2-7)."""

    model: Literal['alibaba:wan@2.7']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p']]
    duration: NotRequired[int]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaWan27Result(TypedDict, total=False):
    """Inference result for curated model `alibaba:wan@2.7` (slug: alibaba-wan2-7)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwen25Vl7bInstructParams(TypedDict, total=False):
    """Inference params for curated model `runware:152@2` (slug: alibaba-qwen2-5-vl-7b-instruct)."""

    model: Literal['runware:152@2']
    prompt: NotRequired[str]
    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class AlibabaQwen25Vl7bInstructResult(TypedDict, total=False):
    """Inference result for curated model `runware:152@2` (slug: alibaba-qwen2-5-vl-7b-instruct)."""

    taskType: Literal['caption']
    taskUUID: str
    cost: NotRequired[float]
    text: str

class AlibabaQwen3Tts17bVoicedesignParams(TypedDict, total=False):
    """Inference params for curated model `alibaba:qwen@3-tts-1.7b-voicedesign` (slug: alibaba-qwen3-tts-1-7b-voicedesign)."""

    model: Literal['alibaba:qwen@3-tts-1.7b-voicedesign']
    positivePrompt: str
    speech: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class AlibabaQwen3Tts17bVoicedesignResult(TypedDict, total=False):
    """Inference result for curated model `alibaba:qwen@3-tts-1.7b-voicedesign` (slug: alibaba-qwen3-tts-1-7b-voicedesign)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class AlibabaWan25PreviewParams(TypedDict, total=False):
    """Inference params for curated model `runware:201@1` (slug: alibaba-wan2-5-preview)."""

    model: Literal['runware:201@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '720p', '1080p']]
    duration: NotRequired[Literal[5, 10]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaWan25PreviewResult(TypedDict, total=False):
    """Inference result for curated model `runware:201@1` (slug: alibaba-wan2-5-preview)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaWan26ImageParams(TypedDict, total=False):
    """Inference params for curated model `alibaba:wan@2.6-image` (slug: alibaba-wan2-6-image)."""

    model: Literal['alibaba:wan@2.6-image']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaWan26ImageResult(TypedDict, total=False):
    """Inference result for curated model `alibaba:wan@2.6-image` (slug: alibaba-wan2-6-image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaZImageTurboParams(TypedDict, total=False):
    """Inference params for curated model `runware:z-image@turbo` (slug: alibaba-z-image-turbo)."""

    model: Literal['runware:z-image@turbo']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaZImageTurboResult(TypedDict, total=False):
    """Inference result for curated model `runware:z-image@turbo` (slug: alibaba-z-image-turbo)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwenImage20Params(TypedDict, total=False):
    """Inference params for curated model `alibaba:qwen-image@2.0` (slug: alibaba-qwen-image-2-0)."""

    model: Literal['alibaba:qwen-image@2.0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaQwenImage20Result(TypedDict, total=False):
    """Inference result for curated model `alibaba:qwen-image@2.0` (slug: alibaba-qwen-image-2-0)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaWan27ImageProParams(TypedDict, total=False):
    """Inference params for curated model `alibaba:wan@2.7-image-pro` (slug: alibaba-wan2-7-image-pro)."""

    model: Literal['alibaba:wan@2.7-image-pro']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaWan27ImageProResult(TypedDict, total=False):
    """Inference result for curated model `alibaba:wan@2.7-image-pro` (slug: alibaba-wan2-7-image-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwenImageEditPlusParams(TypedDict, total=False):
    """Inference params for curated model `runware:108@22` (slug: alibaba-qwen-image-edit-plus)."""

    model: Literal['runware:108@22']
    inputs: dict[str, object]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    settings: NotRequired[dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaQwenImageEditPlusResult(TypedDict, total=False):
    """Inference result for curated model `runware:108@22` (slug: alibaba-qwen-image-edit-plus)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwen3Tts17bBaseParams(TypedDict, total=False):
    """Inference params for curated model `alibaba:qwen@3-tts-1.7b-base` (slug: alibaba-qwen3-tts-1-7b-base)."""

    model: Literal['alibaba:qwen@3-tts-1.7b-base']
    inputs: dict[str, object]
    speech: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class AlibabaQwen3Tts17bBaseResult(TypedDict, total=False):
    """Inference result for curated model `alibaba:qwen@3-tts-1.7b-base` (slug: alibaba-qwen3-tts-1-7b-base)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class AlibabaWan22AnimateParams(TypedDict, total=False):
    """Inference params for curated model `runware:200@8` (slug: alibaba-wan2-2-animate)."""

    model: Literal['runware:200@8']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '580p', '720p']]
    fps: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    advancedFeatures: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaWan22AnimateResult(TypedDict, total=False):
    """Inference result for curated model `runware:200@8` (slug: alibaba-wan2-2-animate)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaWan26FlashParams(TypedDict, total=False):
    """Inference params for curated model `alibaba:wan@2.6-flash` (slug: alibaba-wan2-6-flash)."""

    model: Literal['alibaba:wan@2.6-flash']
    inputs: dict[str, object]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p']]
    duration: NotRequired[int]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaWan26FlashResult(TypedDict, total=False):
    """Inference result for curated model `alibaba:wan@2.6-flash` (slug: alibaba-wan2-6-flash)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwenImage2512Params(TypedDict, total=False):
    """Inference params for curated model `alibaba:qwen-image@2512` (slug: alibaba-qwen-image-2512)."""

    model: Literal['alibaba:qwen-image@2512']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    settings: NotRequired[dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaQwenImage2512Result(TypedDict, total=False):
    """Inference result for curated model `alibaba:qwen-image@2512` (slug: alibaba-qwen-image-2512)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaWan25PreviewImageParams(TypedDict, total=False):
    """Inference params for curated model `runware:201@10` (slug: alibaba-wan2-5-preview-image)."""

    model: Literal['runware:201@10']
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaWan25PreviewImageResult(TypedDict, total=False):
    """Inference result for curated model `runware:201@10` (slug: alibaba-wan2-5-preview-image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwenImage20ProParams(TypedDict, total=False):
    """Inference params for curated model `alibaba:qwen-image@2.0-pro` (slug: alibaba-qwen-image-2-0-pro)."""

    model: Literal['alibaba:qwen-image@2.0-pro']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaQwenImage20ProResult(TypedDict, total=False):
    """Inference result for curated model `alibaba:qwen-image@2.0-pro` (slug: alibaba-qwen-image-2-0-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwen35397bParams(TypedDict, total=False):
    """Inference params for curated model `alibaba:qwen@3.5-397b` (slug: alibaba-qwen3-5-397b)."""

    model: Literal['alibaba:qwen@3.5-397b']
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class AlibabaQwen35397bResult(TypedDict, total=False):
    """Inference result for curated model `alibaba:qwen@3.5-397b` (slug: alibaba-qwen3-5-397b)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class AlibabaWan22A14bParams(TypedDict, total=False):
    """Inference params for curated model `runware:200@6` (slug: alibaba-wan2-2-a14b)."""

    model: Literal['runware:200@6']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '580p', '720p']]
    duration: NotRequired[int]
    fps: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleration: NotRequired[Literal['none', 'low', 'medium', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaWan22A14bResult(TypedDict, total=False):
    """Inference result for curated model `runware:200@6` (slug: alibaba-wan2-2-a14b)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaQwenImageEditParams(TypedDict, total=False):
    """Inference params for curated model `runware:108@20` (slug: alibaba-qwen-image-edit)."""

    model: Literal['runware:108@20']
    inputs: dict[str, object]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    settings: NotRequired[dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaQwenImageEditResult(TypedDict, total=False):
    """Inference result for curated model `runware:108@20` (slug: alibaba-qwen-image-edit)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaHappyhorse10Params(TypedDict, total=False):
    """Inference params for curated model `alibaba:happyhorse@1.0` (slug: alibaba-happyhorse-1-0)."""

    model: Literal['alibaba:happyhorse@1.0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p']]
    duration: NotRequired[int]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaHappyhorse10Result(TypedDict, total=False):
    """Inference result for curated model `alibaba:happyhorse@1.0` (slug: alibaba-happyhorse-1-0)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AlibabaWan22A14bTurboParams(TypedDict, total=False):
    """Inference params for curated model `runware:200@8` (slug: alibaba-wan2-2-a14b-turbo)."""

    model: Literal['runware:200@8']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '580p', '720p']]
    duration: NotRequired[int]
    fps: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleration: NotRequired[Literal['none', 'low', 'medium', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AlibabaWan22A14bTurboResult(TypedDict, total=False):
    """Inference result for curated model `runware:200@8` (slug: alibaba-wan2-2-a14b-turbo)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class FishAudioS21ProParams(TypedDict, total=False):
    """Inference params for curated model `fishaudio:s2.1@pro` (slug: fish-audio-s2-1-pro)."""

    model: Literal['fishaudio:s2.1@pro']
    inputs: NotRequired[dict[str, object]]
    speech: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class FishAudioS21ProResult(TypedDict, total=False):
    """Inference result for curated model `fishaudio:s2.1@pro` (slug: fish-audio-s2-1-pro)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class MireloSfx15Params(TypedDict, total=False):
    """Inference params for curated model `mirelo:1@1` (slug: mirelo-sfx-1-5)."""

    model: Literal['mirelo:1@1']
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG', 'MP4', 'MOV', 'WEBM']]
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    duration: NotRequired[float]
    seed: NotRequired[int]
    steps: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class MireloSfx15Result(TypedDict, total=False):
    """Inference result for curated model `mirelo:1@1` (slug: mirelo-sfx-1-5)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class PixverseV6Params(TypedDict, total=False):
    """Inference params for curated model `pixverse:1@8` (slug: pixverse-v6)."""

    model: Literal['pixverse:1@8']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['360p', '540p', '720p', '1080p']]
    duration: NotRequired[float]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PixverseV6Result(TypedDict, total=False):
    """Inference result for curated model `pixverse:1@8` (slug: pixverse-v6)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PixverseV5FastParams(TypedDict, total=False):
    """Inference params for curated model `pixverse:1@5-fast` (slug: pixverse-v5-fast)."""

    model: Literal['pixverse:1@5-fast']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['360p', '540p', '720p', '1080p']]
    duration: NotRequired[Literal[5, 8]]
    seed: NotRequired[int]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PixverseV5FastResult(TypedDict, total=False):
    """Inference result for curated model `pixverse:1@5-fast` (slug: pixverse-v5-fast)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PixverseV4Params(TypedDict, total=False):
    """Inference params for curated model `pixverse:1@2` (slug: pixverse-v4)."""

    model: Literal['pixverse:1@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['360p', '540p', '720p', '1080p']]
    duration: NotRequired[Literal[5, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PixverseV4Result(TypedDict, total=False):
    """Inference result for curated model `pixverse:1@2` (slug: pixverse-v4)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PixverseV56Params(TypedDict, total=False):
    """Inference params for curated model `pixverse:1@7` (slug: pixverse-v5-6)."""

    model: Literal['pixverse:1@7']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['360p', '540p', '720p', '1080p']]
    duration: NotRequired[float]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PixverseV56Result(TypedDict, total=False):
    """Inference result for curated model `pixverse:1@7` (slug: pixverse-v5-6)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PixverseV5Params(TypedDict, total=False):
    """Inference params for curated model `pixverse:1@5` (slug: pixverse-v5)."""

    model: Literal['pixverse:1@5']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['360p', '540p', '720p', '1080p']]
    duration: NotRequired[Literal[5, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PixverseV5Result(TypedDict, total=False):
    """Inference result for curated model `pixverse:1@5` (slug: pixverse-v5)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PixverseV35Params(TypedDict, total=False):
    """Inference params for curated model `pixverse:1@1` (slug: pixverse-v3-5)."""

    model: Literal['pixverse:1@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['360p', '540p', '720p', '1080p']]
    duration: NotRequired[Literal[5, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PixverseV35Result(TypedDict, total=False):
    """Inference result for curated model `pixverse:1@1` (slug: pixverse-v3-5)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PixverseV55Params(TypedDict, total=False):
    """Inference params for curated model `pixverse:1@6` (slug: pixverse-v5-5)."""

    model: Literal['pixverse:1@6']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['360p', '540p', '720p', '1080p']]
    duration: NotRequired[float]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PixverseV55Result(TypedDict, total=False):
    """Inference result for curated model `pixverse:1@6` (slug: pixverse-v5-5)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PixverseModifyParams(TypedDict, total=False):
    """Inference params for curated model `pixverse:modify@0` (slug: pixverse-modify)."""

    model: Literal['pixverse:modify@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    resolution: NotRequired[Literal['360p', '540p', '720p']]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PixverseModifyResult(TypedDict, total=False):
    """Inference result for curated model `pixverse:modify@0` (slug: pixverse-modify)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PixverseLipsyncParams(TypedDict, total=False):
    """Inference params for curated model `pixverse:lipsync@1` (slug: pixverse-lipsync)."""

    model: Literal['pixverse:lipsync@1']
    inputs: dict[str, object]
    speech: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PixverseLipsyncResult(TypedDict, total=False):
    """Inference result for curated model `pixverse:lipsync@1` (slug: pixverse-lipsync)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class PixverseV45Params(TypedDict, total=False):
    """Inference params for curated model `pixverse:1@3` (slug: pixverse-v4-5)."""

    model: Literal['pixverse:1@3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['360p', '540p', '720p', '1080p']]
    duration: NotRequired[Literal[5, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PixverseV45Result(TypedDict, total=False):
    """Inference result for curated model `pixverse:1@3` (slug: pixverse-v4-5)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class InworldTts15MiniParams(TypedDict, total=False):
    """Inference params for curated model `inworld:tts@1.5-mini` (slug: inworld-tts-1-5-mini)."""

    model: Literal['inworld:tts@1.5-mini']
    audioSettings: NotRequired[dict[str, object]]
    speech: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]

class InworldTts15MiniResult(TypedDict, total=False):
    """Inference result for curated model `inworld:tts@1.5-mini` (slug: inworld-tts-1-5-mini)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class InworldTts2Params(TypedDict, total=False):
    """Inference params for curated model `inworld:tts@2` (slug: inworld-tts-2)."""

    model: Literal['inworld:tts@2']
    speech: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class InworldTts2Result(TypedDict, total=False):
    """Inference result for curated model `inworld:tts@2` (slug: inworld-tts-2)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class InworldTts15MaxParams(TypedDict, total=False):
    """Inference params for curated model `inworld:tts@1.5-max` (slug: inworld-tts-1-5-max)."""

    model: Literal['inworld:tts@1.5-max']
    audioSettings: NotRequired[dict[str, object]]
    speech: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]

class InworldTts15MaxResult(TypedDict, total=False):
    """Inference result for curated model `inworld:tts@1.5-max` (slug: inworld-tts-1-5-max)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class LumaUni1Params(TypedDict, total=False):
    """Inference params for curated model `luma:uni@1` (slug: luma-uni-1)."""

    model: Literal['luma:uni@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class LumaUni1Result(TypedDict, total=False):
    """Inference result for curated model `luma:uni@1` (slug: luma-uni-1)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class LumaUni1MaxParams(TypedDict, total=False):
    """Inference params for curated model `luma:uni@1-max` (slug: luma-uni-1-max)."""

    model: Literal['luma:uni@1-max']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class LumaUni1MaxResult(TypedDict, total=False):
    """Inference result for curated model `luma:uni@1-max` (slug: luma-uni-1-max)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class LumaRay32Params(TypedDict, total=False):
    """Inference params for curated model `luma:ray@3.2` (slug: luma-ray3-2)."""

    model: Literal['luma:ray@3.2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['360p', '540p', '720p', '1080p']]
    duration: NotRequired[Literal[5, 10]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class LumaRay32Result(TypedDict, total=False):
    """Inference result for curated model `luma:ray@3.2` (slug: luma-ray3-2)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RecraftV41ProParams(TypedDict, total=False):
    """Inference params for curated model `recraft:v4.1-pro@0` (slug: recraft-v4-1-pro)."""

    model: Literal['recraft:v4.1-pro@0']
    positivePrompt: str
    width: int
    height: int
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RecraftV41ProResult(TypedDict, total=False):
    """Inference result for curated model `recraft:v4.1-pro@0` (slug: recraft-v4-1-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RecraftVectorizeParams(TypedDict, total=False):
    """Inference params for curated model `recraft:1@1` (slug: recraft-vectorize)."""

    model: Literal['recraft:1@1']
    inputs: dict[str, object]
    taskType: Literal['vectorize']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['SVG']]
    deliveryMethod: NotRequired[str]

class RecraftVectorizeResult(TypedDict, total=False):
    """Inference result for curated model `recraft:1@1` (slug: recraft-vectorize)."""

    taskType: Literal['vectorize']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class RecraftV41UtilityParams(TypedDict, total=False):
    """Inference params for curated model `recraft:v4.1-utility@0` (slug: recraft-v4-1-utility)."""

    model: Literal['recraft:v4.1-utility@0']
    positivePrompt: str
    width: int
    height: int
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RecraftV41UtilityResult(TypedDict, total=False):
    """Inference result for curated model `recraft:v4.1-utility@0` (slug: recraft-v4-1-utility)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RecraftV41Params(TypedDict, total=False):
    """Inference params for curated model `recraft:v4.1@0` (slug: recraft-v4-1)."""

    model: Literal['recraft:v4.1@0']
    positivePrompt: str
    width: int
    height: int
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RecraftV41Result(TypedDict, total=False):
    """Inference result for curated model `recraft:v4.1@0` (slug: recraft-v4-1)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RecraftV4VectorParams(TypedDict, total=False):
    """Inference params for curated model `recraft:v4@vector` (slug: recraft-v4-vector)."""

    model: Literal['recraft:v4@vector']
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['vectorize']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['SVG']]
    deliveryMethod: NotRequired[str]

class RecraftV4VectorResult(TypedDict, total=False):
    """Inference result for curated model `recraft:v4@vector` (slug: recraft-v4-vector)."""

    taskType: Literal['vectorize']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class RecraftV4ProParams(TypedDict, total=False):
    """Inference params for curated model `recraft:v4-pro@0` (slug: recraft-v4-pro)."""

    model: Literal['recraft:v4-pro@0']
    positivePrompt: str
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RecraftV4ProResult(TypedDict, total=False):
    """Inference result for curated model `recraft:v4-pro@0` (slug: recraft-v4-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RecraftV4Params(TypedDict, total=False):
    """Inference params for curated model `recraft:v4@0` (slug: recraft-v4)."""

    model: Literal['recraft:v4@0']
    positivePrompt: str
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RecraftV4Result(TypedDict, total=False):
    """Inference result for curated model `recraft:v4@0` (slug: recraft-v4)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RecraftV4ProVectorParams(TypedDict, total=False):
    """Inference params for curated model `recraft:v4-pro@vector` (slug: recraft-v4-pro-vector)."""

    model: Literal['recraft:v4-pro@vector']
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['vectorize']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['SVG']]
    deliveryMethod: NotRequired[str]

class RecraftV4ProVectorResult(TypedDict, total=False):
    """Inference result for curated model `recraft:v4-pro@vector` (slug: recraft-v4-pro-vector)."""

    taskType: Literal['vectorize']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class RecraftV41UtilityProParams(TypedDict, total=False):
    """Inference params for curated model `recraft:v4.1-utility-pro@0` (slug: recraft-v4-1-utility-pro)."""

    model: Literal['recraft:v4.1-utility-pro@0']
    positivePrompt: str
    width: int
    height: int
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RecraftV41UtilityProResult(TypedDict, total=False):
    """Inference result for curated model `recraft:v4.1-utility-pro@0` (slug: recraft-v4-1-utility-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class TripoV31Params(TypedDict, total=False):
    """Inference params for curated model `tripo:v3.1@0` (slug: tripo-v3-1)."""

    model: Literal['tripo:v3.1@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    negativePrompt: NotRequired[str]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['3dInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['GLB']]
    deliveryMethod: NotRequired[str]

class TripoV31Result(TypedDict, total=False):
    """Inference result for curated model `tripo:v3.1@0` (slug: tripo-v3-1)."""

    taskType: Literal['3dInference']
    taskUUID: str
    cost: NotRequired[float]
    outputs: dict[str, object]
    seed: NotRequired[int]

class BflFlux2Klein9bParams(TypedDict, total=False):
    """Inference params for curated model `runware:400@2` (slug: bfl-flux-2-klein-9b)."""

    model: Literal['runware:400@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleration: NotRequired[Literal['none', 'low', 'medium', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux2Klein9bResult(TypedDict, total=False):
    """Inference result for curated model `runware:400@2` (slug: bfl-flux-2-klein-9b)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFluxVirtualTryOnParams(TypedDict, total=False):
    """Inference params for curated model `bfl:flux@vto` (slug: bfl-flux-virtual-try-on)."""

    model: Literal['bfl:flux@vto']
    inputs: dict[str, object]
    positivePrompt: str
    seed: NotRequired[int]
    steps: NotRequired[int]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFluxVirtualTryOnResult(TypedDict, total=False):
    """Inference result for curated model `bfl:flux@vto` (slug: bfl-flux-virtual-try-on)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux2Klein4bParams(TypedDict, total=False):
    """Inference params for curated model `runware:400@4` (slug: bfl-flux-2-klein-4b)."""

    model: Literal['runware:400@4']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleration: NotRequired[Literal['none', 'low', 'medium', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux2Klein4bResult(TypedDict, total=False):
    """Inference result for curated model `runware:400@4` (slug: bfl-flux-2-klein-4b)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux2FlexParams(TypedDict, total=False):
    """Inference params for curated model `bfl:6@1` (slug: bfl-flux-2-flex)."""

    model: Literal['bfl:6@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    CFGScale: NotRequired[float]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux2FlexResult(TypedDict, total=False):
    """Inference result for curated model `bfl:6@1` (slug: bfl-flux-2-flex)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux2MaxParams(TypedDict, total=False):
    """Inference params for curated model `bfl:7@1` (slug: bfl-flux-2-max)."""

    model: Literal['bfl:7@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux2MaxResult(TypedDict, total=False):
    """Inference result for curated model `bfl:7@1` (slug: bfl-flux-2-max)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux1KontextProParams(TypedDict, total=False):
    """Inference params for curated model `bfl:3@1` (slug: bfl-flux-1-kontext-pro)."""

    model: Literal['bfl:3@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux1KontextProResult(TypedDict, total=False):
    """Inference result for curated model `bfl:3@1` (slug: bfl-flux-1-kontext-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFluxEraseParams(TypedDict, total=False):
    """Inference params for curated model `bfl:flux@erase` (slug: bfl-flux-erase)."""

    model: Literal['bfl:flux@erase']
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFluxEraseResult(TypedDict, total=False):
    """Inference result for curated model `bfl:flux@erase` (slug: bfl-flux-erase)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux1KontextMaxParams(TypedDict, total=False):
    """Inference params for curated model `bfl:4@1` (slug: bfl-flux-1-kontext-max)."""

    model: Literal['bfl:4@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux1KontextMaxResult(TypedDict, total=False):
    """Inference result for curated model `bfl:4@1` (slug: bfl-flux-1-kontext-max)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux1FillDevParams(TypedDict, total=False):
    """Inference params for curated model `runware:102@1` (slug: bfl-flux-1-fill-dev)."""

    model: Literal['runware:102@1']
    acePlusPlus: NotRequired[dict[str, object]]
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    layerDiffuse: NotRequired[bool]
    pulid: NotRequired[dict[str, object]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux1FillDevResult(TypedDict, total=False):
    """Inference result for curated model `runware:102@1` (slug: bfl-flux-1-fill-dev)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux2Klein4bBaseParams(TypedDict, total=False):
    """Inference params for curated model `runware:400@5` (slug: bfl-flux-2-klein-4b-base)."""

    model: Literal['runware:400@5']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleration: NotRequired[Literal['none', 'low', 'medium', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux2Klein4bBaseResult(TypedDict, total=False):
    """Inference result for curated model `runware:400@5` (slug: bfl-flux-2-klein-4b-base)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFluxOutpaintingParams(TypedDict, total=False):
    """Inference params for curated model `bfl:flux@outpainting` (slug: bfl-flux-outpainting)."""

    model: Literal['bfl:flux@outpainting']
    inputs: dict[str, object]
    outpaint: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFluxOutpaintingResult(TypedDict, total=False):
    """Inference result for curated model `bfl:flux@outpainting` (slug: bfl-flux-outpainting)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux11ProUltraParams(TypedDict, total=False):
    """Inference params for curated model `bfl:2@2` (slug: bfl-flux-1-1-pro-ultra)."""

    model: Literal['bfl:2@2']
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux11ProUltraResult(TypedDict, total=False):
    """Inference result for curated model `bfl:2@2` (slug: bfl-flux-1-1-pro-ultra)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux2Klein9bBaseParams(TypedDict, total=False):
    """Inference params for curated model `runware:400@3` (slug: bfl-flux-2-klein-9b-base)."""

    model: Literal['runware:400@3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleration: NotRequired[Literal['none', 'low', 'medium', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux2Klein9bBaseResult(TypedDict, total=False):
    """Inference result for curated model `runware:400@3` (slug: bfl-flux-2-klein-9b-base)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux1KontextDevParams(TypedDict, total=False):
    """Inference params for curated model `runware:106@1` (slug: bfl-flux-1-kontext-dev)."""

    model: Literal['runware:106@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux1KontextDevResult(TypedDict, total=False):
    """Inference result for curated model `runware:106@1` (slug: bfl-flux-1-kontext-dev)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux1SchnellParams(TypedDict, total=False):
    """Inference params for curated model `runware:100@1` (slug: bfl-flux-1-schnell)."""

    model: Literal['runware:100@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux1SchnellResult(TypedDict, total=False):
    """Inference result for curated model `runware:100@1` (slug: bfl-flux-1-schnell)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux1DevParams(TypedDict, total=False):
    """Inference params for curated model `runware:101@1` (slug: bfl-flux-1-dev)."""

    model: Literal['runware:101@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    layerDiffuse: NotRequired[bool]
    pulid: NotRequired[dict[str, object]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux1DevResult(TypedDict, total=False):
    """Inference result for curated model `runware:101@1` (slug: bfl-flux-1-dev)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux11ProParams(TypedDict, total=False):
    """Inference params for curated model `bfl:2@1` (slug: bfl-flux-1-1-pro)."""

    model: Literal['bfl:2@1']
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux11ProResult(TypedDict, total=False):
    """Inference result for curated model `bfl:2@1` (slug: bfl-flux-1-1-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux2ProParams(TypedDict, total=False):
    """Inference params for curated model `bfl:5@1` (slug: bfl-flux-2-pro)."""

    model: Literal['bfl:5@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux2ProResult(TypedDict, total=False):
    """Inference result for curated model `bfl:5@1` (slug: bfl-flux-2-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux2Klein9bKvParams(TypedDict, total=False):
    """Inference params for curated model `runware:400@6` (slug: bfl-flux-2-klein-9b-kv)."""

    model: Literal['runware:400@6']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleration: NotRequired[Literal['none', 'low', 'medium', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux2Klein9bKvResult(TypedDict, total=False):
    """Inference result for curated model `runware:400@6` (slug: bfl-flux-2-klein-9b-kv)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux1ExpandProParams(TypedDict, total=False):
    """Inference params for curated model `bfl:1@3` (slug: bfl-flux-1-expand-pro)."""

    model: Literal['bfl:1@3']
    inputs: dict[str, object]
    positivePrompt: str
    steps: NotRequired[int]
    CFGScale: NotRequired[float]
    outpaint: dict[str, object]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux1ExpandProResult(TypedDict, total=False):
    """Inference result for curated model `bfl:1@3` (slug: bfl-flux-1-expand-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux1FillProParams(TypedDict, total=False):
    """Inference params for curated model `bfl:1@2` (slug: bfl-flux-1-fill-pro)."""

    model: Literal['bfl:1@2']
    inputs: dict[str, object]
    positivePrompt: str
    seed: NotRequired[int]
    steps: NotRequired[int]
    CFGScale: NotRequired[float]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux1FillProResult(TypedDict, total=False):
    """Inference result for curated model `bfl:1@2` (slug: bfl-flux-1-fill-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BflFlux2DevParams(TypedDict, total=False):
    """Inference params for curated model `runware:400@1` (slug: bfl-flux-2-dev)."""

    model: Literal['runware:400@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleration: NotRequired[Literal['none', 'low', 'medium', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BflFlux2DevResult(TypedDict, total=False):
    """Inference result for curated model `runware:400@1` (slug: bfl-flux-2-dev)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class TencentHunyuan3d31RapidParams(TypedDict, total=False):
    """Inference params for curated model `tencent:hunyuan-3d@3.1-rapid` (slug: tencent-hunyuan-3d-3-1-rapid)."""

    model: Literal['tencent:hunyuan-3d@3.1-rapid']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['3dInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['GLB']]
    deliveryMethod: NotRequired[str]

class TencentHunyuan3d31RapidResult(TypedDict, total=False):
    """Inference result for curated model `tencent:hunyuan-3d@3.1-rapid` (slug: tencent-hunyuan-3d-3-1-rapid)."""

    taskType: Literal['3dInference']
    taskUUID: str
    cost: NotRequired[float]
    outputs: dict[str, object]
    seed: NotRequired[int]

class TencentHunyuan3d31ProParams(TypedDict, total=False):
    """Inference params for curated model `tencent:hunyuan-3d@3.1-pro` (slug: tencent-hunyuan-3d-3-1-pro)."""

    model: Literal['tencent:hunyuan-3d@3.1-pro']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['3dInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['GLB']]
    deliveryMethod: NotRequired[str]

class TencentHunyuan3d31ProResult(TypedDict, total=False):
    """Inference result for curated model `tencent:hunyuan-3d@3.1-pro` (slug: tencent-hunyuan-3d-3-1-pro)."""

    taskType: Literal['3dInference']
    taskUUID: str
    cost: NotRequired[float]
    outputs: dict[str, object]
    seed: NotRequired[int]

class TencentHunyuanimage30Params(TypedDict, total=False):
    """Inference params for curated model `runware:180@1` (slug: tencent-hunyuanimage-3-0)."""

    model: Literal['runware:180@1']
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleration: NotRequired[Literal['none', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class TencentHunyuanimage30Result(TypedDict, total=False):
    """Inference result for curated model `runware:180@1` (slug: tencent-hunyuanimage-3-0)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class AnthropicClaudeSonnet46Params(TypedDict, total=False):
    """Inference params for curated model `anthropic:claude@sonnet-4.6` (slug: anthropic-claude-sonnet-4-6)."""

    model: Literal['anthropic:claude@sonnet-4.6']
    inputs: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class AnthropicClaudeSonnet46Result(TypedDict, total=False):
    """Inference result for curated model `anthropic:claude@sonnet-4.6` (slug: anthropic-claude-sonnet-4-6)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class AnthropicClaudeOpus47Params(TypedDict, total=False):
    """Inference params for curated model `anthropic:claude@opus-4.7` (slug: anthropic-claude-opus-4-7)."""

    model: Literal['anthropic:claude@opus-4.7']
    inputs: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class AnthropicClaudeOpus47Result(TypedDict, total=False):
    """Inference result for curated model `anthropic:claude@opus-4.7` (slug: anthropic-claude-opus-4-7)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class AnthropicClaudeOpus48Params(TypedDict, total=False):
    """Inference params for curated model `anthropic:claude@opus-4.8` (slug: anthropic-claude-opus-4-8)."""

    model: Literal['anthropic:claude@opus-4.8']
    inputs: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class AnthropicClaudeOpus48Result(TypedDict, total=False):
    """Inference result for curated model `anthropic:claude@opus-4.8` (slug: anthropic-claude-opus-4-8)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class AnthropicClaudeHaiku45Params(TypedDict, total=False):
    """Inference params for curated model `anthropic:claude@haiku-4.5` (slug: anthropic-claude-haiku-4-5)."""

    model: Literal['anthropic:claude@haiku-4.5']
    inputs: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class AnthropicClaudeHaiku45Result(TypedDict, total=False):
    """Inference result for curated model `anthropic:claude@haiku-4.5` (slug: anthropic-claude-haiku-4-5)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class AnthropicClaudeFable5Params(TypedDict, total=False):
    """Inference params for curated model `anthropic:claude@fable-5` (slug: anthropic-claude-fable-5)."""

    model: Literal['anthropic:claude@fable-5']
    outputFormat: NotRequired[Literal['TEXT', 'JSON']]
    inputs: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    jsonSchema: NotRequired[dict[str, object] | str]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class AnthropicClaudeFable5Result(TypedDict, total=False):
    """Inference result for curated model `anthropic:claude@fable-5` (slug: anthropic-claude-fable-5)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]
    reasoningContent: NotRequired[str]

class BriaRmbgV20Params(TypedDict, total=False):
    """Inference params for curated model `bria:2@1` (slug: bria-rmbg-v2-0)."""

    model: Literal['bria:2@1']
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BriaRmbgV20Result(TypedDict, total=False):
    """Inference result for curated model `bria:2@1` (slug: bria-rmbg-v2-0)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class BriaVideoIncreaseResolutionParams(TypedDict, total=False):
    """Inference params for curated model `bria:50@1` (slug: bria-video-increase-resolution)."""

    model: Literal['bria:50@1']
    upscaleFactor: NotRequired[Literal[2, 4]]
    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BriaVideoIncreaseResolutionResult(TypedDict, total=False):
    """Inference result for curated model `bria:50@1` (slug: bria-video-increase-resolution)."""

    taskType: Literal['upscale']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]

class BriaImageReplaceBackgroundParams(TypedDict, total=False):
    """Inference params for curated model `bria:11@1` (slug: bria-image-replace-background)."""

    model: Literal['bria:11@1']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    negativePrompt: NotRequired[str]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BriaImageReplaceBackgroundResult(TypedDict, total=False):
    """Inference result for curated model `bria:11@1` (slug: bria-image-replace-background)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BriaFiboParams(TypedDict, total=False):
    """Inference params for curated model `bria:20@1` (slug: bria-fibo)."""

    model: Literal['bria:20@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    CFGScale: NotRequired[Literal[3, 4, 5]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BriaFiboResult(TypedDict, total=False):
    """Inference result for curated model `bria:20@1` (slug: bria-fibo)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BriaImageIncreaseResolutionParams(TypedDict, total=False):
    """Inference params for curated model `bria:52@1` (slug: bria-image-increase-resolution)."""

    model: Literal['bria:52@1']
    upscaleFactor: NotRequired[Literal[2, 4]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BriaImageIncreaseResolutionResult(TypedDict, total=False):
    """Inference result for curated model `bria:52@1` (slug: bria-image-increase-resolution)."""

    taskType: Literal['upscale']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]

class BriaVideoBackgroundRemovalParams(TypedDict, total=False):
    """Inference params for curated model `bria:51@1` (slug: bria-video-background-removal)."""

    model: Literal['bria:51@1']
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class BriaVideoBackgroundRemovalResult(TypedDict, total=False):
    """Inference result for curated model `bria:51@1` (slug: bria-video-background-removal)."""

    taskType: Literal['removeBackground']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]

class BriaVideoEraserParams(TypedDict, total=False):
    """Inference params for curated model `bria:60@1` (slug: bria-video-eraser)."""

    model: Literal['bria:60@1']
    inputs: dict[str, object]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BriaVideoEraserResult(TypedDict, total=False):
    """Inference result for curated model `bria:60@1` (slug: bria-video-eraser)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BriaFiboEditParams(TypedDict, total=False):
    """Inference params for curated model `bria:21@1` (slug: bria-fibo-edit)."""

    model: Literal['bria:21@1']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    negativePrompt: NotRequired[str]
    seed: NotRequired[int]
    steps: NotRequired[int]
    CFGScale: NotRequired[Literal[3, 4, 5]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BriaFiboEditResult(TypedDict, total=False):
    """Inference result for curated model `bria:21@1` (slug: bria-fibo-edit)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BriaFiboLiteParams(TypedDict, total=False):
    """Inference params for curated model `bria:20@3` (slug: bria-fibo-lite)."""

    model: Literal['bria:20@3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    CFGScale: NotRequired[Literal[3, 4, 5]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BriaFiboLiteResult(TypedDict, total=False):
    """Inference result for curated model `bria:20@3` (slug: bria-fibo-lite)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Bria32Params(TypedDict, total=False):
    """Inference params for curated model `bria:10@1` (slug: bria-3-2)."""

    model: Literal['bria:10@1']
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Bria32Result(TypedDict, total=False):
    """Inference result for curated model `bria:10@1` (slug: bria-3-2)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BriaFiboEditToolsParams(TypedDict, total=False):
    """Inference params for curated model `bria:21@2` (slug: bria-fibo-edit-tools)."""

    model: Literal['bria:21@2']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    negativePrompt: NotRequired[str]
    outpaint: NotRequired[dict[str, object]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BriaFiboEditToolsResult(TypedDict, total=False):
    """Inference result for curated model `bria:21@2` (slug: bria-fibo-edit-tools)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class LightricksLtx2FastParams(TypedDict, total=False):
    """Inference params for curated model `lightricks:2@1` (slug: lightricks-ltx-2-fast)."""

    model: Literal['lightricks:2@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[6, 8, 10]]
    fps: NotRequired[Literal[25, 50]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class LightricksLtx2FastResult(TypedDict, total=False):
    """Inference result for curated model `lightricks:2@1` (slug: lightricks-ltx-2-fast)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class LightricksLtx23Params(TypedDict, total=False):
    """Inference params for curated model `lightricks:ltx@2.3` (slug: lightricks-ltx-2-3)."""

    model: Literal['lightricks:ltx@2.3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[6, 8, 10]]
    fps: NotRequired[Literal[24, 25, 48, 50]]
    CFGScale: NotRequired[float]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class LightricksLtx23Result(TypedDict, total=False):
    """Inference result for curated model `lightricks:ltx@2.3` (slug: lightricks-ltx-2-3)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class LightricksLtx2ProParams(TypedDict, total=False):
    """Inference params for curated model `lightricks:2@0` (slug: lightricks-ltx-2-pro)."""

    model: Literal['lightricks:2@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[6, 8, 10]]
    fps: NotRequired[Literal[24, 25, 50]]
    CFGScale: NotRequired[float]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class LightricksLtx2ProResult(TypedDict, total=False):
    """Inference result for curated model `lightricks:2@0` (slug: lightricks-ltx-2-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class LightricksLtx2Params(TypedDict, total=False):
    """Inference params for curated model `lightricks:ltx@2` (slug: lightricks-ltx-2)."""

    model: Literal['lightricks:ltx@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[int]
    fps: NotRequired[int]
    steps: NotRequired[int]
    CFGScale: NotRequired[float]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class LightricksLtx2Result(TypedDict, total=False):
    """Inference result for curated model `lightricks:ltx@2` (slug: lightricks-ltx-2)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class LightricksLtx2RetakeParams(TypedDict, total=False):
    """Inference params for curated model `lightricks:3@1` (slug: lightricks-ltx-2-retake)."""

    model: Literal['lightricks:3@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class LightricksLtx2RetakeResult(TypedDict, total=False):
    """Inference result for curated model `lightricks:3@1` (slug: lightricks-ltx-2-retake)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class LightricksLtx23FastParams(TypedDict, total=False):
    """Inference params for curated model `lightricks:ltx@2.3-fast` (slug: lightricks-ltx-2-3-fast)."""

    model: Literal['lightricks:ltx@2.3-fast']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[float]
    fps: NotRequired[Literal[24, 25, 48, 50]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class LightricksLtx23FastResult(TypedDict, total=False):
    """Inference result for curated model `lightricks:ltx@2.3-fast` (slug: lightricks-ltx-2-3-fast)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Imagineart15ProParams(TypedDict, total=False):
    """Inference params for curated model `imagineart:1.5-pro@0` (slug: imagineart-1-5-pro)."""

    model: Literal['imagineart:1.5-pro@0']
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Imagineart15ProResult(TypedDict, total=False):
    """Inference result for curated model `imagineart:1.5-pro@0` (slug: imagineart-1-5-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Imagineart15Params(TypedDict, total=False):
    """Inference params for curated model `imagineart:1@5` (slug: imagineart-1-5)."""

    model: Literal['imagineart:1@5']
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Imagineart15Result(TypedDict, total=False):
    """Inference result for curated model `imagineart:1@5` (slug: imagineart-1-5)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Imagineart20Params(TypedDict, total=False):
    """Inference params for curated model `imagineart:2.0@0` (slug: imagineart-2-0)."""

    model: Literal['imagineart:2.0@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['1K', '1.5K', '2K']]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Imagineart20Result(TypedDict, total=False):
    """Inference result for curated model `imagineart:2.0@0` (slug: imagineart-2-0)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Meshy6Params(TypedDict, total=False):
    """Inference params for curated model `meshy:meshy@6` (slug: meshy-6)."""

    model: Literal['meshy:meshy@6']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['3dInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['GLB']]
    deliveryMethod: NotRequired[str]

class Meshy6Result(TypedDict, total=False):
    """Inference result for curated model `meshy:meshy@6` (slug: meshy-6)."""

    taskType: Literal['3dInference']
    taskUUID: str
    cost: NotRequired[float]
    outputs: dict[str, object]
    seed: NotRequired[int]

class ExactlyPhotoExtremeContrastParams(TypedDict, total=False):
    """Inference params for curated model `exactly:photo@extreme-contrast` (slug: exactly-photo-extreme-contrast)."""

    model: Literal['exactly:photo@extreme-contrast']
    inputs: dict[str, object]
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ExactlyPhotoExtremeContrastResult(TypedDict, total=False):
    """Inference result for curated model `exactly:photo@extreme-contrast` (slug: exactly-photo-extreme-contrast)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ExactlyPhotoGrainFilmLookParams(TypedDict, total=False):
    """Inference params for curated model `exactly:photo@grain-film-look` (slug: exactly-photo-grain-film-look)."""

    model: Literal['exactly:photo@grain-film-look']
    inputs: dict[str, object]
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ExactlyPhotoGrainFilmLookResult(TypedDict, total=False):
    """Inference result for curated model `exactly:photo@grain-film-look` (slug: exactly-photo-grain-film-look)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ExactlyPhotoWarmLightParams(TypedDict, total=False):
    """Inference params for curated model `exactly:photo@warm-light` (slug: exactly-photo-warm-light)."""

    model: Literal['exactly:photo@warm-light']
    inputs: dict[str, object]
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ExactlyPhotoWarmLightResult(TypedDict, total=False):
    """Inference result for curated model `exactly:photo@warm-light` (slug: exactly-photo-warm-light)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ExactlyIllustrativeTrainingParams(TypedDict, total=False):
    """Inference params for curated model `exactly:illustrative@training` (slug: exactly-illustrative-training)."""

    model: Literal['exactly:illustrative@training']
    inputs: dict[str, object]
    importModel: dict[str, object]
    taskType: Literal['modelUpload']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]

class ExactlyIllustrativeTrainingResult(TypedDict, total=False):
    """Inference result for curated model `exactly:illustrative@training` (slug: exactly-illustrative-training)."""

    taskType: Literal['training']
    taskUUID: str
    cost: NotRequired[float]
    air: str

class ModelUploadResult(TypedDict, total=False):
    """Canonical result shape for `modelUpload` tasks."""

    taskType: Literal['training']
    taskUUID: str
    cost: NotRequired[float]
    air: str

class ExactlyPhotoJourneyParams(TypedDict, total=False):
    """Inference params for curated model `exactly:photo@journey` (slug: exactly-photo-journey)."""

    model: Literal['exactly:photo@journey']
    inputs: dict[str, object]
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ExactlyPhotoJourneyResult(TypedDict, total=False):
    """Inference result for curated model `exactly:photo@journey` (slug: exactly-photo-journey)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ExactlyPhotoBrightPulseParams(TypedDict, total=False):
    """Inference params for curated model `exactly:photo@bright-pulse` (slug: exactly-photo-bright-pulse)."""

    model: Literal['exactly:photo@bright-pulse']
    inputs: dict[str, object]
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ExactlyPhotoBrightPulseResult(TypedDict, total=False):
    """Inference result for curated model `exactly:photo@bright-pulse` (slug: exactly-photo-bright-pulse)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ExactlyPhotoDistantRealityParams(TypedDict, total=False):
    """Inference params for curated model `exactly:photo@distant-reality` (slug: exactly-photo-distant-reality)."""

    model: Literal['exactly:photo@distant-reality']
    inputs: dict[str, object]
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ExactlyPhotoDistantRealityResult(TypedDict, total=False):
    """Inference result for curated model `exactly:photo@distant-reality` (slug: exactly-photo-distant-reality)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BytedanceSeedream40Params(TypedDict, total=False):
    """Inference params for curated model `bytedance:5@0` (slug: bytedance-seedream-4-0)."""

    model: Literal['bytedance:5@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BytedanceSeedream40Result(TypedDict, total=False):
    """Inference result for curated model `bytedance:5@0` (slug: bytedance-seedream-4-0)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BytedanceSeedance20FastParams(TypedDict, total=False):
    """Inference params for curated model `bytedance:seedance@2.0-fast` (slug: bytedance-seedance-2-0-fast)."""

    model: Literal['bytedance:seedance@2.0-fast']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '720p']]
    duration: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BytedanceSeedance20FastResult(TypedDict, total=False):
    """Inference result for curated model `bytedance:seedance@2.0-fast` (slug: bytedance-seedance-2-0-fast)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BytedanceSeedance15ProParams(TypedDict, total=False):
    """Inference params for curated model `bytedance:seedance@1.5-pro` (slug: bytedance-seedance-1-5-pro)."""

    model: Literal['bytedance:seedance@1.5-pro']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '720p', '1080p']]
    duration: NotRequired[float]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BytedanceSeedance15ProResult(TypedDict, total=False):
    """Inference result for curated model `bytedance:seedance@1.5-pro` (slug: bytedance-seedance-1-5-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BytedanceOmnihuman15Params(TypedDict, total=False):
    """Inference params for curated model `bytedance:5@2` (slug: bytedance-omnihuman-1-5)."""

    model: Literal['bytedance:5@2']
    inputs: dict[str, object]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BytedanceOmnihuman15Result(TypedDict, total=False):
    """Inference result for curated model `bytedance:5@2` (slug: bytedance-omnihuman-1-5)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BytedanceSeedream45Params(TypedDict, total=False):
    """Inference params for curated model `bytedance:seedream@4.5` (slug: bytedance-seedream-4-5)."""

    model: Literal['bytedance:seedream@4.5']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['2K', '4K']]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BytedanceSeedream45Result(TypedDict, total=False):
    """Inference result for curated model `bytedance:seedream@4.5` (slug: bytedance-seedream-4-5)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BytedanceOmnihuman1Params(TypedDict, total=False):
    """Inference params for curated model `bytedance:5@1` (slug: bytedance-omnihuman-1)."""

    model: Literal['bytedance:5@1']
    inputs: dict[str, object]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BytedanceOmnihuman1Result(TypedDict, total=False):
    """Inference result for curated model `bytedance:5@1` (slug: bytedance-omnihuman-1)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BytedanceSeedance10ProFastParams(TypedDict, total=False):
    """Inference params for curated model `bytedance:2@2` (slug: bytedance-seedance-1-0-pro-fast)."""

    model: Literal['bytedance:2@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '720p', '1080p']]
    duration: NotRequired[float]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BytedanceSeedance10ProFastResult(TypedDict, total=False):
    """Inference result for curated model `bytedance:2@2` (slug: bytedance-seedance-1-0-pro-fast)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BytedanceVideoUpscalerParams(TypedDict, total=False):
    """Inference params for curated model `bytedance:50@1` (slug: bytedance-video-upscaler)."""

    model: Literal['bytedance:50@1']
    inputs: dict[str, object]
    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    deliveryMethod: NotRequired[str]

class BytedanceVideoUpscalerResult(TypedDict, total=False):
    """Inference result for curated model `bytedance:50@1` (slug: bytedance-video-upscaler)."""

    taskType: Literal['upscale']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]

class BytedanceSeedance20Params(TypedDict, total=False):
    """Inference params for curated model `bytedance:seedance@2.0` (slug: bytedance-seedance-2-0)."""

    model: Literal['bytedance:seedance@2.0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '720p', '1080p']]
    duration: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BytedanceSeedance20Result(TypedDict, total=False):
    """Inference result for curated model `bytedance:seedance@2.0` (slug: bytedance-seedance-2-0)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BytedanceSeedream50LiteParams(TypedDict, total=False):
    """Inference params for curated model `bytedance:seedream@5.0-lite` (slug: bytedance-seedream-5-0-lite)."""

    model: Literal['bytedance:seedream@5.0-lite']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BytedanceSeedream50LiteResult(TypedDict, total=False):
    """Inference result for curated model `bytedance:seedream@5.0-lite` (slug: bytedance-seedream-5-0-lite)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BytedanceSeedance10ProParams(TypedDict, total=False):
    """Inference params for curated model `bytedance:2@1` (slug: bytedance-seedance-1-0-pro)."""

    model: Literal['bytedance:2@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '1080p']]
    duration: NotRequired[float]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BytedanceSeedance10ProResult(TypedDict, total=False):
    """Inference result for curated model `bytedance:2@1` (slug: bytedance-seedance-1-0-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class ZaiGlm47Params(TypedDict, total=False):
    """Inference params for curated model `zai:glm@4.7` (slug: zai-glm-4-7)."""

    model: Literal['zai:glm@4.7']
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class ZaiGlm47Result(TypedDict, total=False):
    """Inference result for curated model `zai:glm@4.7` (slug: zai-glm-4-7)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class ZaiGlm51Params(TypedDict, total=False):
    """Inference params for curated model `zai:glm@5.1` (slug: zai-glm-5-1)."""

    model: Literal['zai:glm@5.1']
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class ZaiGlm51Result(TypedDict, total=False):
    """Inference result for curated model `zai:glm@5.1` (slug: zai-glm-5-1)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class ZaiGlmImageParams(TypedDict, total=False):
    """Inference params for curated model `runware:glm-image@0` (slug: zai-glm-image)."""

    model: Literal['runware:glm-image@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    CFGScale: NotRequired[float]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ZaiGlmImageResult(TypedDict, total=False):
    """Inference result for curated model `runware:glm-image@0` (slug: zai-glm-image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram30ReplaceBackgroundParams(TypedDict, total=False):
    """Inference params for curated model `ideogram:4@5` (slug: ideogram-3-0-replace-background)."""

    model: Literal['ideogram:4@5']
    inputs: dict[str, object]
    positivePrompt: str
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram30ReplaceBackgroundResult(TypedDict, total=False):
    """Inference result for curated model `ideogram:4@5` (slug: ideogram-3-0-replace-background)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram20RemixParams(TypedDict, total=False):
    """Inference params for curated model `ideogram:3@2` (slug: ideogram-2-0-remix)."""

    model: Literal['ideogram:3@2']
    inputs: dict[str, object]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram20RemixResult(TypedDict, total=False):
    """Inference result for curated model `ideogram:3@2` (slug: ideogram-2-0-remix)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram10RemixParams(TypedDict, total=False):
    """Inference params for curated model `ideogram:1@2` (slug: ideogram-1-0-remix)."""

    model: Literal['ideogram:1@2']
    inputs: dict[str, object]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram10RemixResult(TypedDict, total=False):
    """Inference result for curated model `ideogram:1@2` (slug: ideogram-1-0-remix)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram30ReframeParams(TypedDict, total=False):
    """Inference params for curated model `ideogram:4@4` (slug: ideogram-3-0-reframe)."""

    model: Literal['ideogram:4@4']
    inputs: dict[str, object]
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram30ReframeResult(TypedDict, total=False):
    """Inference result for curated model `ideogram:4@4` (slug: ideogram-3-0-reframe)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram20Params(TypedDict, total=False):
    """Inference params for curated model `ideogram:3@1` (slug: ideogram-2-0)."""

    model: Literal['ideogram:3@1']
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram20Result(TypedDict, total=False):
    """Inference result for curated model `ideogram:3@1` (slug: ideogram-2-0)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram30RemixParams(TypedDict, total=False):
    """Inference params for curated model `ideogram:4@2` (slug: ideogram-3-0-remix)."""

    model: Literal['ideogram:4@2']
    inputs: dict[str, object]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram30RemixResult(TypedDict, total=False):
    """Inference result for curated model `ideogram:4@2` (slug: ideogram-3-0-remix)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram20ReframeParams(TypedDict, total=False):
    """Inference params for curated model `ideogram:3@4` (slug: ideogram-2-0-reframe)."""

    model: Literal['ideogram:3@4']
    inputs: dict[str, object]
    width: NotRequired[int]
    height: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram20ReframeResult(TypedDict, total=False):
    """Inference result for curated model `ideogram:3@4` (slug: ideogram-2-0-reframe)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram10Params(TypedDict, total=False):
    """Inference params for curated model `ideogram:1@1` (slug: ideogram-1-0)."""

    model: Literal['ideogram:1@1']
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram10Result(TypedDict, total=False):
    """Inference result for curated model `ideogram:1@1` (slug: ideogram-1-0)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram20EditParams(TypedDict, total=False):
    """Inference params for curated model `ideogram:3@3` (slug: ideogram-2-0-edit)."""

    model: Literal['ideogram:3@3']
    inputs: dict[str, object]
    positivePrompt: str
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram20EditResult(TypedDict, total=False):
    """Inference result for curated model `ideogram:3@3` (slug: ideogram-2-0-edit)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class IdeogramLayerizeTextParams(TypedDict, total=False):
    """Inference params for curated model `ideogram:layerize-text@0` (slug: ideogram-layerize-text)."""

    model: Literal['ideogram:layerize-text@0']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    seed: NotRequired[int]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class IdeogramLayerizeTextResult(TypedDict, total=False):
    """Inference result for curated model `ideogram:layerize-text@0` (slug: ideogram-layerize-text)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]
    outputs: NotRequired[dict[str, object]]

class Ideogram30EditParams(TypedDict, total=False):
    """Inference params for curated model `ideogram:4@3` (slug: ideogram-3-0-edit)."""

    model: Literal['ideogram:4@3']
    inputs: dict[str, object]
    positivePrompt: str
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram30EditResult(TypedDict, total=False):
    """Inference result for curated model `ideogram:4@3` (slug: ideogram-3-0-edit)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram30Params(TypedDict, total=False):
    """Inference params for curated model `ideogram:4@1` (slug: ideogram-3-0)."""

    model: Literal['ideogram:4@1']
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    upscaleFactor: NotRequired[Literal[1, 2, 4]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram30Result(TypedDict, total=False):
    """Inference result for curated model `ideogram:4@1` (slug: ideogram-3-0)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram2aRemixParams(TypedDict, total=False):
    """Inference params for curated model `ideogram:2@2` (slug: ideogram-2a-remix)."""

    model: Literal['ideogram:2@2']
    inputs: dict[str, object]
    positivePrompt: str
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram2aRemixResult(TypedDict, total=False):
    """Inference result for curated model `ideogram:2@2` (slug: ideogram-2a-remix)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram2aParams(TypedDict, total=False):
    """Inference params for curated model `ideogram:2@1` (slug: ideogram-2a)."""

    model: Literal['ideogram:2@1']
    positivePrompt: str
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram2aResult(TypedDict, total=False):
    """Inference result for curated model `ideogram:2@1` (slug: ideogram-2a)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Ideogram40Params(TypedDict, total=False):
    """Inference params for curated model `ideogram:4@0` (slug: ideogram-4-0)."""

    model: Literal['ideogram:4@0']
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Ideogram40Result(TypedDict, total=False):
    """Inference result for curated model `ideogram:4@0` (slug: ideogram-4-0)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]
    structuredPrompt: NotRequired[dict[str, object]]

class Krea2TurboParams(TypedDict, total=False):
    """Inference params for curated model `krea:krea@2-turbo` (slug: krea-2-turbo)."""

    model: Literal['krea:krea@2-turbo']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Krea2TurboResult(TypedDict, total=False):
    """Inference result for curated model `krea:krea@2-turbo` (slug: krea-2-turbo)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Krea2MediumParams(TypedDict, total=False):
    """Inference params for curated model `krea:krea@2-medium` (slug: krea-2-medium)."""

    model: Literal['krea:krea@2-medium']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Krea2MediumResult(TypedDict, total=False):
    """Inference result for curated model `krea:krea@2-medium` (slug: krea-2-medium)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KreaFlux1KreaDevParams(TypedDict, total=False):
    """Inference params for curated model `runware:107@1` (slug: krea-flux-1-krea-dev)."""

    model: Literal['runware:107@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    layerDiffuse: NotRequired[bool]
    pulid: NotRequired[dict[str, object]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KreaFlux1KreaDevResult(TypedDict, total=False):
    """Inference result for curated model `runware:107@1` (slug: krea-flux-1-krea-dev)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Krea2LargeParams(TypedDict, total=False):
    """Inference params for curated model `krea:krea@2-large` (slug: krea-2-large)."""

    model: Literal['krea:krea@2-large']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Krea2LargeResult(TypedDict, total=False):
    """Inference result for curated model `krea:krea@2-large` (slug: krea-2-large)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class HeygenAvatarVParams(TypedDict, total=False):
    """Inference params for curated model `heygen:avatar@5` (slug: heygen-avatar-v)."""

    model: Literal['heygen:avatar@5']
    inputs: dict[str, object]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p', '4K']]
    speech: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class HeygenAvatarVResult(TypedDict, total=False):
    """Inference result for curated model `heygen:avatar@5` (slug: heygen-avatar-v)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class HeygenVideoAgentParams(TypedDict, total=False):
    """Inference params for curated model `heygen:video-agent@0` (slug: heygen-video-agent)."""

    model: Literal['heygen:video-agent@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[int]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class HeygenVideoAgentResult(TypedDict, total=False):
    """Inference result for curated model `heygen:video-agent@0` (slug: heygen-video-agent)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class HeygenAvatarIvParams(TypedDict, total=False):
    """Inference params for curated model `heygen:avatar@4` (slug: heygen-avatar-iv)."""

    model: Literal['heygen:avatar@4']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p']]
    speech: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class HeygenAvatarIvResult(TypedDict, total=False):
    """Inference result for curated model `heygen:avatar@4` (slug: heygen-avatar-iv)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SkyworkSkyreelsV4Params(TypedDict, total=False):
    """Inference params for curated model `skywork:skyreels@v4` (slug: skywork-skyreels-v4)."""

    model: Literal['skywork:skyreels@v4']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '720p', '1080p']]
    duration: NotRequired[float]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SkyworkSkyreelsV4Result(TypedDict, total=False):
    """Inference result for curated model `skywork:skyreels@v4` (slug: skywork-skyreels-v4)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class OpenaiSora2Params(TypedDict, total=False):
    """Inference params for curated model `openai:3@1` (slug: openai-sora-2)."""

    model: Literal['openai:3@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[4, 8, 12, 16, 20]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class OpenaiSora2Result(TypedDict, total=False):
    """Inference result for curated model `openai:3@1` (slug: openai-sora-2)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]
    outputs: NotRequired[dict[str, object]]

class OpenaiClipVitL14Params(TypedDict, total=False):
    """Inference params for curated model `runware:151@1` (slug: openai-clip-vit-l-14)."""

    model: Literal['runware:151@1']
    prompt: NotRequired[str]
    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class OpenaiClipVitL14Result(TypedDict, total=False):
    """Inference result for curated model `runware:151@1` (slug: openai-clip-vit-l-14)."""

    taskType: Literal['caption']
    taskUUID: str
    cost: NotRequired[float]
    text: str

class OpenaiGptImage1Params(TypedDict, total=False):
    """Inference params for curated model `openai:1@1` (slug: openai-gpt-image-1)."""

    model: Literal['openai:1@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class OpenaiGptImage1Result(TypedDict, total=False):
    """Inference result for curated model `openai:1@1` (slug: openai-gpt-image-1)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class OpenaiGptImage1MiniParams(TypedDict, total=False):
    """Inference params for curated model `openai:1@2` (slug: openai-gpt-image-1-mini)."""

    model: Literal['openai:1@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class OpenaiGptImage1MiniResult(TypedDict, total=False):
    """Inference result for curated model `openai:1@2` (slug: openai-gpt-image-1-mini)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class OpenaiGpt54ProParams(TypedDict, total=False):
    """Inference params for curated model `openai:gpt@5.4-pro` (slug: openai-gpt-5-4-pro)."""

    model: Literal['openai:gpt@5.4-pro']
    deliveryMethod: NotRequired[Literal['async']]
    includeCost: NotRequired[bool]
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    outputFormat: NotRequired[Literal['TEXT']]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class OpenaiGpt54ProResult(TypedDict, total=False):
    """Inference result for curated model `openai:gpt@5.4-pro` (slug: openai-gpt-5-4-pro)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class OpenaiGpt54Params(TypedDict, total=False):
    """Inference params for curated model `openai:gpt@5.4` (slug: openai-gpt-5-4)."""

    model: Literal['openai:gpt@5.4']
    includeCost: NotRequired[bool]
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class OpenaiGpt54Result(TypedDict, total=False):
    """Inference result for curated model `openai:gpt@5.4` (slug: openai-gpt-5-4)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class OpenaiGptImage2Params(TypedDict, total=False):
    """Inference params for curated model `openai:gpt-image@2` (slug: openai-gpt-image-2)."""

    model: Literal['openai:gpt-image@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class OpenaiGptImage2Result(TypedDict, total=False):
    """Inference result for curated model `openai:gpt-image@2` (slug: openai-gpt-image-2)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class OpenaiGptImage15Params(TypedDict, total=False):
    """Inference params for curated model `openai:4@1` (slug: openai-gpt-image-1-5)."""

    model: Literal['openai:4@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class OpenaiGptImage15Result(TypedDict, total=False):
    """Inference result for curated model `openai:4@1` (slug: openai-gpt-image-1-5)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class OpenaiGpt55Params(TypedDict, total=False):
    """Inference params for curated model `openai:gpt@5.5` (slug: openai-gpt-5-5)."""

    model: Literal['openai:gpt@5.5']
    outputFormat: NotRequired[Literal['TEXT', 'JSON']]
    inputs: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    jsonSchema: NotRequired[dict[str, object] | str]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class OpenaiGpt55Result(TypedDict, total=False):
    """Inference result for curated model `openai:gpt@5.5` (slug: openai-gpt-5-5)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class OpenaiSora2ProParams(TypedDict, total=False):
    """Inference params for curated model `openai:3@2` (slug: openai-sora-2-pro)."""

    model: Literal['openai:3@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[4, 8, 12, 16, 20]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class OpenaiSora2ProResult(TypedDict, total=False):
    """Inference result for curated model `openai:3@2` (slug: openai-sora-2-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]
    outputs: NotRequired[dict[str, object]]

class OpenaiGpt54MiniParams(TypedDict, total=False):
    """Inference params for curated model `openai:gpt@5.4-mini` (slug: openai-gpt-5-4-mini)."""

    model: Literal['openai:gpt@5.4-mini']
    includeCost: NotRequired[bool]
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class OpenaiGpt54MiniResult(TypedDict, total=False):
    """Inference result for curated model `openai:gpt@5.4-mini` (slug: openai-gpt-5-4-mini)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class OpenaiGpt54NanoParams(TypedDict, total=False):
    """Inference params for curated model `openai:gpt@5.4-nano` (slug: openai-gpt-5-4-nano)."""

    model: Literal['openai:gpt@5.4-nano']
    includeCost: NotRequired[bool]
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class OpenaiGpt54NanoResult(TypedDict, total=False):
    """Inference result for curated model `openai:gpt@5.4-nano` (slug: openai-gpt-5-4-nano)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class SourcefulRiverflow2PreviewMaxParams(TypedDict, total=False):
    """Inference params for curated model `sourceful:2@3` (slug: sourceful-riverflow-2-preview-max)."""

    model: Literal['sourceful:2@3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SourcefulRiverflow2PreviewMaxResult(TypedDict, total=False):
    """Inference result for curated model `sourceful:2@3` (slug: sourceful-riverflow-2-preview-max)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SourcefulRiverflow11ProParams(TypedDict, total=False):
    """Inference params for curated model `sourceful:1@2` (slug: sourceful-riverflow-1-1-pro)."""

    model: Literal['sourceful:1@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SourcefulRiverflow11ProResult(TypedDict, total=False):
    """Inference result for curated model `sourceful:1@2` (slug: sourceful-riverflow-1-1-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SourcefulRiverflow20FastParams(TypedDict, total=False):
    """Inference params for curated model `sourceful:riverflow-2.0@fast` (slug: sourceful-riverflow-2-0-fast)."""

    model: Literal['sourceful:riverflow-2.0@fast']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['1K', '2K']]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SourcefulRiverflow20FastResult(TypedDict, total=False):
    """Inference result for curated model `sourceful:riverflow-2.0@fast` (slug: sourceful-riverflow-2-0-fast)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SourcefulRiverflow25FastParams(TypedDict, total=False):
    """Inference params for curated model `sourceful:riverflow-2.5@fast` (slug: sourceful-riverflow-2-5-fast)."""

    model: Literal['sourceful:riverflow-2.5@fast']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['1K', '2K']]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SourcefulRiverflow25FastResult(TypedDict, total=False):
    """Inference result for curated model `sourceful:riverflow-2.5@fast` (slug: sourceful-riverflow-2-5-fast)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SourcefulRiverflow11MiniParams(TypedDict, total=False):
    """Inference params for curated model `sourceful:1@0` (slug: sourceful-riverflow-1-1-mini)."""

    model: Literal['sourceful:1@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SourcefulRiverflow11MiniResult(TypedDict, total=False):
    """Inference result for curated model `sourceful:1@0` (slug: sourceful-riverflow-1-1-mini)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SourcefulRiverflow2PreviewStandardParams(TypedDict, total=False):
    """Inference params for curated model `sourceful:2@1` (slug: sourceful-riverflow-2-preview-standard)."""

    model: Literal['sourceful:2@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SourcefulRiverflow2PreviewStandardResult(TypedDict, total=False):
    """Inference result for curated model `sourceful:2@1` (slug: sourceful-riverflow-2-preview-standard)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SourcefulRiverflow25ProParams(TypedDict, total=False):
    """Inference params for curated model `sourceful:riverflow-2.5@pro` (slug: sourceful-riverflow-2-5-pro)."""

    model: Literal['sourceful:riverflow-2.5@pro']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['1K', '2K', '4K']]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SourcefulRiverflow25ProResult(TypedDict, total=False):
    """Inference result for curated model `sourceful:riverflow-2.5@pro` (slug: sourceful-riverflow-2-5-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SourcefulRiverflow20ProParams(TypedDict, total=False):
    """Inference params for curated model `sourceful:riverflow-2.0@pro` (slug: sourceful-riverflow-2-0-pro)."""

    model: Literal['sourceful:riverflow-2.0@pro']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['1K', '2K', '4K']]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SourcefulRiverflow20ProResult(TypedDict, total=False):
    """Inference result for curated model `sourceful:riverflow-2.0@pro` (slug: sourceful-riverflow-2-0-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SourcefulRiverflow11Params(TypedDict, total=False):
    """Inference params for curated model `sourceful:1@1` (slug: sourceful-riverflow-1-1)."""

    model: Literal['sourceful:1@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SourcefulRiverflow11Result(TypedDict, total=False):
    """Inference result for curated model `sourceful:1@1` (slug: sourceful-riverflow-1-1)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class SourcefulRiverflow2PreviewFastParams(TypedDict, total=False):
    """Inference params for curated model `sourceful:2@2` (slug: sourceful-riverflow-2-preview-fast)."""

    model: Literal['sourceful:2@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SourcefulRiverflow2PreviewFastResult(TypedDict, total=False):
    """Inference result for curated model `sourceful:2@2` (slug: sourceful-riverflow-2-preview-fast)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class TopazlabsStarlightPrecise25Params(TypedDict, total=False):
    """Inference params for curated model `topazlabs:starlight-precise@2.5` (slug: topazlabs-starlight-precise-2-5)."""

    model: Literal['topazlabs:starlight-precise@2.5']
    inputs: dict[str, object]
    width: int
    height: int
    fps: NotRequired[float]
    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    deliveryMethod: NotRequired[str]

class TopazlabsStarlightPrecise25Result(TypedDict, total=False):
    """Inference result for curated model `topazlabs:starlight-precise@2.5` (slug: topazlabs-starlight-precise-2-5)."""

    taskType: Literal['upscale']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]

class MicrosoftTrellis2Params(TypedDict, total=False):
    """Inference params for curated model `microsoft:trellis-2@4b` (slug: microsoft-trellis-2)."""

    model: Literal['microsoft:trellis-2@4b']
    inputs: dict[str, object]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['3dInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['GLB']]
    deliveryMethod: NotRequired[str]

class MicrosoftTrellis2Result(TypedDict, total=False):
    """Inference result for curated model `microsoft:trellis-2@4b` (slug: microsoft-trellis-2)."""

    taskType: Literal['3dInference']
    taskUUID: str
    cost: NotRequired[float]
    outputs: dict[str, object]
    seed: NotRequired[int]

class GoogleGemini31FlashTtsParams(TypedDict, total=False):
    """Inference params for curated model `google:gemini@3.1-flash-tts` (slug: google-gemini-3-1-flash-tts)."""

    model: Literal['google:gemini@3.1-flash-tts']
    seed: NotRequired[int]
    speech: dict[str, object]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class GoogleGemini31FlashTtsResult(TypedDict, total=False):
    """Inference result for curated model `google:gemini@3.1-flash-tts` (slug: google-gemini-3-1-flash-tts)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class GoogleVeo3Params(TypedDict, total=False):
    """Inference params for curated model `google:3@0` (slug: google-veo-3)."""

    model: Literal['google:3@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p']]
    duration: NotRequired[Literal[4, 6, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleVeo3Result(TypedDict, total=False):
    """Inference result for curated model `google:3@0` (slug: google-veo-3)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleImagen4PreviewParams(TypedDict, total=False):
    """Inference params for curated model `google:2@1` (slug: google-imagen-4-preview)."""

    model: Literal['google:2@1']
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleImagen4PreviewResult(TypedDict, total=False):
    """Inference result for curated model `google:2@1` (slug: google-imagen-4-preview)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleVeo31Params(TypedDict, total=False):
    """Inference params for curated model `google:3@2` (slug: google-veo-3-1)."""

    model: Literal['google:3@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p', '4K']]
    duration: NotRequired[Literal[4, 6, 7, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleVeo31Result(TypedDict, total=False):
    """Inference result for curated model `google:3@2` (slug: google-veo-3-1)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleImagen3Params(TypedDict, total=False):
    """Inference params for curated model `google:1@1` (slug: google-imagen-3)."""

    model: Literal['google:1@1']
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleImagen3Result(TypedDict, total=False):
    """Inference result for curated model `google:1@1` (slug: google-imagen-3)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleGemini35FlashParams(TypedDict, total=False):
    """Inference params for curated model `google:gemini@3.5-flash` (slug: google-gemini-3-5-flash)."""

    model: Literal['google:gemini@3.5-flash']
    outputFormat: NotRequired[Literal['TEXT', 'JSON']]
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    providerSettings: NotRequired[dict[str, object]]
    jsonSchema: NotRequired[dict[str, object] | str]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class GoogleGemini35FlashResult(TypedDict, total=False):
    """Inference result for curated model `google:gemini@3.5-flash` (slug: google-gemini-3-5-flash)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]
    thoughtSignature: NotRequired[str]

class GoogleVeo3FastParams(TypedDict, total=False):
    """Inference params for curated model `google:3@1` (slug: google-veo-3-fast)."""

    model: Literal['google:3@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[4, 6, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleVeo3FastResult(TypedDict, total=False):
    """Inference result for curated model `google:3@1` (slug: google-veo-3-fast)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleVeo2Params(TypedDict, total=False):
    """Inference params for curated model `google:2@0` (slug: google-veo-2)."""

    model: Literal['google:2@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 6, 7, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleVeo2Result(TypedDict, total=False):
    """Inference result for curated model `google:2@0` (slug: google-veo-2)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleNanoBanana2Params(TypedDict, total=False):
    """Inference params for curated model `google:4@3` (slug: google-nano-banana-2)."""

    model: Literal['google:4@3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['0.5K', '1K', '2K', '4K']]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleNanoBanana2Result(TypedDict, total=False):
    """Inference result for curated model `google:4@3` (slug: google-nano-banana-2)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleGemini31FlashLiteParams(TypedDict, total=False):
    """Inference params for curated model `google:gemini@3.1-flash-lite` (slug: google-gemini-3-1-flash-lite)."""

    model: Literal['google:gemini@3.1-flash-lite']
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class GoogleGemini31FlashLiteResult(TypedDict, total=False):
    """Inference result for curated model `google:gemini@3.1-flash-lite` (slug: google-gemini-3-1-flash-lite)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class GoogleVeo31FastParams(TypedDict, total=False):
    """Inference params for curated model `google:3@3` (slug: google-veo-3-1-fast)."""

    model: Literal['google:3@3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p', '4K']]
    duration: NotRequired[Literal[4, 6, 7, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleVeo31FastResult(TypedDict, total=False):
    """Inference result for curated model `google:3@3` (slug: google-veo-3-1-fast)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleGemini3FlashParams(TypedDict, total=False):
    """Inference params for curated model `google:gemini@3-flash` (slug: google-gemini-3-flash)."""

    model: Literal['google:gemini@3-flash']
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class GoogleGemini3FlashResult(TypedDict, total=False):
    """Inference result for curated model `google:gemini@3-flash` (slug: google-gemini-3-flash)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class GoogleNanoBananaProParams(TypedDict, total=False):
    """Inference params for curated model `google:4@2` (slug: google-nano-banana-pro)."""

    model: Literal['google:4@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['1K', '2K', '4K']]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleNanoBananaProResult(TypedDict, total=False):
    """Inference result for curated model `google:4@2` (slug: google-nano-banana-pro)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleNanoBananaParams(TypedDict, total=False):
    """Inference params for curated model `google:4@1` (slug: google-nano-banana)."""

    model: Literal['google:4@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleNanoBananaResult(TypedDict, total=False):
    """Inference result for curated model `google:4@1` (slug: google-nano-banana)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleVeo31LiteParams(TypedDict, total=False):
    """Inference params for curated model `google:veo@3.1-lite` (slug: google-veo-3-1-lite)."""

    model: Literal['google:veo@3.1-lite']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p']]
    duration: NotRequired[Literal[4, 6, 8]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleVeo31LiteResult(TypedDict, total=False):
    """Inference result for curated model `google:veo@3.1-lite` (slug: google-veo-3-1-lite)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleGemini31ProParams(TypedDict, total=False):
    """Inference params for curated model `google:gemini@3.1-pro` (slug: google-gemini-3-1-pro)."""

    model: Literal['google:gemini@3.1-pro']
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class GoogleGemini31ProResult(TypedDict, total=False):
    """Inference result for curated model `google:gemini@3.1-pro` (slug: google-gemini-3-1-pro)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class GoogleImagen4FastParams(TypedDict, total=False):
    """Inference params for curated model `google:2@3` (slug: google-imagen-4-fast)."""

    model: Literal['google:2@3']
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleImagen4FastResult(TypedDict, total=False):
    """Inference result for curated model `google:2@3` (slug: google-imagen-4-fast)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleGemma431bParams(TypedDict, total=False):
    """Inference params for curated model `google:gemma@4-31b` (slug: google-gemma-4-31b)."""

    model: Literal['google:gemma@4-31b']
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class GoogleGemma431bResult(TypedDict, total=False):
    """Inference result for curated model `google:gemma@4-31b` (slug: google-gemma-4-31b)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class GoogleImagen3FastParams(TypedDict, total=False):
    """Inference params for curated model `google:1@2` (slug: google-imagen-3-fast)."""

    model: Literal['google:1@2']
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleImagen3FastResult(TypedDict, total=False):
    """Inference result for curated model `google:1@2` (slug: google-imagen-3-fast)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class GoogleImagen4UltraParams(TypedDict, total=False):
    """Inference params for curated model `google:2@2` (slug: google-imagen-4-ultra)."""

    model: Literal['google:2@2']
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class GoogleImagen4UltraResult(TypedDict, total=False):
    """Inference result for curated model `google:2@2` (slug: google-imagen-4-ultra)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class VeedFabric10Params(TypedDict, total=False):
    """Inference params for curated model `veed:fabric@1.0` (slug: veed-fabric-1-0)."""

    model: Literal['veed:fabric@1.0']
    inputs: dict[str, object]
    resolution: NotRequired[Literal['720p', '480p']]
    speech: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class VeedFabric10Result(TypedDict, total=False):
    """Inference result for curated model `veed:fabric@1.0` (slug: veed-fabric-1-0)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiVideoO3ProParams(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-video@o3-pro` (slug: klingai-video-o3-pro)."""

    model: Literal['klingai:kling-video@o3-pro']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['1080p']]
    duration: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiVideoO3ProResult(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-video@o3-pro` (slug: klingai-video-o3-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai16ProParams(TypedDict, total=False):
    """Inference params for curated model `klingai:3@2` (slug: klingai-1-6-pro)."""

    model: Literal['klingai:3@2']
    inputs: NotRequired[dict[str, object]]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai16ProResult(TypedDict, total=False):
    """Inference result for curated model `klingai:3@2` (slug: klingai-1-6-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiVideoO34kParams(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-video@o3-4k` (slug: klingai-video-o3-4k)."""

    model: Literal['klingai:kling-video@o3-4k']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['4k']]
    duration: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiVideoO34kResult(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-video@o3-4k` (slug: klingai-video-o3-4k)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiVideo26StandardParams(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-video@2.6-standard` (slug: klingai-video-2-6-standard)."""

    model: Literal['klingai:kling-video@2.6-standard']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiVideo26StandardResult(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-video@2.6-standard` (slug: klingai-video-2-6-standard)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiAvatar20StandardParams(TypedDict, total=False):
    """Inference params for curated model `klingai:avatar@2.0-standard` (slug: klingai-avatar-2-0-standard)."""

    model: Literal['klingai:avatar@2.0-standard']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiAvatar20StandardResult(TypedDict, total=False):
    """Inference result for curated model `klingai:avatar@2.0-standard` (slug: klingai-avatar-2-0-standard)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiImageO3Params(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-image@o3` (slug: klingai-image-o3)."""

    model: Literal['klingai:kling-image@o3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiImageO3Result(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-image@o3` (slug: klingai-image-o3)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiVideo26ProParams(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-video@2.6-pro` (slug: klingai-video-2-6-pro)."""

    model: Literal['klingai:kling-video@2.6-pro']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiVideo26ProResult(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-video@2.6-pro` (slug: klingai-video-2-6-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiVideoO1ProParams(TypedDict, total=False):
    """Inference params for curated model `klingai:kling@o1` (slug: klingai-video-o1-pro)."""

    model: Literal['klingai:kling@o1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiVideoO1ProResult(TypedDict, total=False):
    """Inference result for curated model `klingai:kling@o1` (slug: klingai-video-o1-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai20MasterParams(TypedDict, total=False):
    """Inference params for curated model `klingai:4@3` (slug: klingai-2-0-master)."""

    model: Literal['klingai:4@3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai20MasterResult(TypedDict, total=False):
    """Inference result for curated model `klingai:4@3` (slug: klingai-2-0-master)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai15StandardParams(TypedDict, total=False):
    """Inference params for curated model `klingai:2@1` (slug: klingai-1-5-standard)."""

    model: Literal['klingai:2@1']
    inputs: NotRequired[dict[str, object]]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai15StandardResult(TypedDict, total=False):
    """Inference result for curated model `klingai:2@1` (slug: klingai-1-5-standard)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiVideo30ProParams(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-video@3-pro` (slug: klingai-video-3-0-pro)."""

    model: Literal['klingai:kling-video@3-pro']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiVideo30ProResult(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-video@3-pro` (slug: klingai-video-3-0-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiVideoO3StandardParams(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-video@o3-standard` (slug: klingai-video-o3-standard)."""

    model: Literal['klingai:kling-video@o3-standard']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p']]
    duration: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiVideoO3StandardResult(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-video@o3-standard` (slug: klingai-video-o3-standard)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiLipSyncParams(TypedDict, total=False):
    """Inference params for curated model `klingai:7@1` (slug: klingai-lip-sync)."""

    model: Literal['klingai:7@1']
    inputs: dict[str, object]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiLipSyncResult(TypedDict, total=False):
    """Inference result for curated model `klingai:7@1` (slug: klingai-lip-sync)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiVideoO1StandardParams(TypedDict, total=False):
    """Inference params for curated model `klingai:kling@o1-standard` (slug: klingai-video-o1-standard)."""

    model: Literal['klingai:kling@o1-standard']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiVideoO1StandardResult(TypedDict, total=False):
    """Inference result for curated model `klingai:kling@o1-standard` (slug: klingai-video-o1-standard)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiVideo304kParams(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-video@3-4k` (slug: klingai-video-3-0-4k)."""

    model: Literal['klingai:kling-video@3-4k']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiVideo304kResult(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-video@3-4k` (slug: klingai-video-3-0-4k)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai10StandardParams(TypedDict, total=False):
    """Inference params for curated model `klingai:1@1` (slug: klingai-1-0-standard)."""

    model: Literal['klingai:1@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai10StandardResult(TypedDict, total=False):
    """Inference result for curated model `klingai:1@1` (slug: klingai-1-0-standard)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai25TurboProParams(TypedDict, total=False):
    """Inference params for curated model `klingai:6@1` (slug: klingai-2-5-turbo-pro)."""

    model: Literal['klingai:6@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai25TurboProResult(TypedDict, total=False):
    """Inference result for curated model `klingai:6@1` (slug: klingai-2-5-turbo-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai10ProParams(TypedDict, total=False):
    """Inference params for curated model `klingai:1@2` (slug: klingai-1-0-pro)."""

    model: Literal['klingai:1@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai10ProResult(TypedDict, total=False):
    """Inference result for curated model `klingai:1@2` (slug: klingai-1-0-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai15ProParams(TypedDict, total=False):
    """Inference params for curated model `klingai:2@2` (slug: klingai-1-5-pro)."""

    model: Literal['klingai:2@2']
    inputs: dict[str, object]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai15ProResult(TypedDict, total=False):
    """Inference result for curated model `klingai:2@2` (slug: klingai-1-5-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai16StandardParams(TypedDict, total=False):
    """Inference params for curated model `klingai:3@1` (slug: klingai-1-6-standard)."""

    model: Literal['klingai:3@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai16StandardResult(TypedDict, total=False):
    """Inference result for curated model `klingai:3@1` (slug: klingai-1-6-standard)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai21StandardParams(TypedDict, total=False):
    """Inference params for curated model `klingai:5@1` (slug: klingai-2-1-standard)."""

    model: Literal['klingai:5@1']
    inputs: dict[str, object]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai21StandardResult(TypedDict, total=False):
    """Inference result for curated model `klingai:5@1` (slug: klingai-2-1-standard)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiVideo30StandardParams(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-video@3-standard` (slug: klingai-video-3-0-standard)."""

    model: Literal['klingai:kling-video@3-standard']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiVideo30StandardResult(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-video@3-standard` (slug: klingai-video-3-0-standard)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiVideo30TurboParams(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-video@3.0-turbo` (slug: klingai-video-3-0-turbo)."""

    model: Literal['klingai:kling-video@3.0-turbo']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['720p', '1080p']]
    duration: NotRequired[int]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiVideo30TurboResult(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-video@3.0-turbo` (slug: klingai-video-3-0-turbo)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiImage30Params(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-image@3` (slug: klingai-image-3-0)."""

    model: Literal['klingai:kling-image@3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['1k', '2k']]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiImage30Result(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-image@3` (slug: klingai-image-3-0)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiAvatar20ProParams(TypedDict, total=False):
    """Inference params for curated model `klingai:avatar@2.0-pro` (slug: klingai-avatar-2-0-pro)."""

    model: Literal['klingai:avatar@2.0-pro']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiAvatar20ProResult(TypedDict, total=False):
    """Inference result for curated model `klingai:avatar@2.0-pro` (slug: klingai-avatar-2-0-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai21MasterParams(TypedDict, total=False):
    """Inference params for curated model `klingai:5@3` (slug: klingai-2-1-master)."""

    model: Literal['klingai:5@3']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai21MasterResult(TypedDict, total=False):
    """Inference result for curated model `klingai:5@3` (slug: klingai-2-1-master)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai21ProParams(TypedDict, total=False):
    """Inference params for curated model `klingai:5@2` (slug: klingai-2-1-pro)."""

    model: Literal['klingai:5@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai21ProResult(TypedDict, total=False):
    """Inference result for curated model `klingai:5@2` (slug: klingai-2-1-pro)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Klingai25TurboStandardParams(TypedDict, total=False):
    """Inference params for curated model `klingai:6@0` (slug: klingai-2-5-turbo-standard)."""

    model: Literal['klingai:6@0']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    duration: NotRequired[Literal[5, 10]]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Klingai25TurboStandardResult(TypedDict, total=False):
    """Inference result for curated model `klingai:6@0` (slug: klingai-2-5-turbo-standard)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class KlingaiImageO1Params(TypedDict, total=False):
    """Inference params for curated model `klingai:kling-image@o1` (slug: klingai-image-o1)."""

    model: Literal['klingai:kling-image@o1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['1k', '2k']]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class KlingaiImageO1Result(TypedDict, total=False):
    """Inference result for curated model `klingai:kling-image@o1` (slug: klingai-image-o1)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BaiduErnieImageParams(TypedDict, total=False):
    """Inference params for curated model `baidu:ernie-image@0` (slug: baidu-ernie-image)."""

    model: Literal['baidu:ernie-image@0']
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    CFGScale: NotRequired[float]
    acceleration: NotRequired[Literal['none', 'low', 'medium', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BaiduErnieImageResult(TypedDict, total=False):
    """Inference result for curated model `baidu:ernie-image@0` (slug: baidu-ernie-image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class BaiduErnieImageTurboParams(TypedDict, total=False):
    """Inference params for curated model `baidu:ernie-image@turbo` (slug: baidu-ernie-image-turbo)."""

    model: Literal['baidu:ernie-image@turbo']
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    acceleration: NotRequired[Literal['none', 'low', 'medium', 'high']]
    acceleratorOptions: NotRequired[dict[str, object]]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class BaiduErnieImageTurboResult(TypedDict, total=False):
    """Inference result for curated model `baidu:ernie-image@turbo` (slug: baidu-ernie-image-turbo)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class MoonshotaiKimiK26Params(TypedDict, total=False):
    """Inference params for curated model `moonshotai:kimi@k2.6` (slug: moonshotai-kimi-k2-6)."""

    model: Literal['moonshotai:kimi@k2.6']
    outputFormat: NotRequired[Literal['TEXT', 'JSON']]
    inputs: NotRequired[dict[str, object]]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    jsonSchema: NotRequired[dict[str, object] | str]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class MoonshotaiKimiK26Result(TypedDict, total=False):
    """Inference result for curated model `moonshotai:kimi@k2.6` (slug: moonshotai-kimi-k2-6)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class MemoriesVideoAgeDetectionParams(TypedDict, total=False):
    """Inference params for curated model `memories:2@1` (slug: memories-video-age-detection)."""

    model: Literal['memories:2@1']
    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class MemoriesVideoAgeDetectionResult(TypedDict, total=False):
    """Inference result for curated model `memories:2@1` (slug: memories-video-age-detection)."""

    taskType: Literal['caption']
    taskUUID: str
    cost: NotRequired[float]
    structuredData: dict[str, object]

class MemoriesVideoCaptioningParams(TypedDict, total=False):
    """Inference params for curated model `memories:1@1` (slug: memories-video-captioning)."""

    model: Literal['memories:1@1']
    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class MemoriesVideoCaptioningResult(TypedDict, total=False):
    """Inference result for curated model `memories:1@1` (slug: memories-video-captioning)."""

    taskType: Literal['caption']
    taskUUID: str
    cost: NotRequired[float]
    text: str

class XaiGrokImagineVideo15PreviewParams(TypedDict, total=False):
    """Inference params for curated model `xai:grok-imagine@video-1.5-preview` (slug: xai-grok-imagine-video-1-5-preview)."""

    model: Literal['xai:grok-imagine@video-1.5-preview']
    inputs: dict[str, object]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '720p']]
    duration: NotRequired[int]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class XaiGrokImagineVideo15PreviewResult(TypedDict, total=False):
    """Inference result for curated model `xai:grok-imagine@video-1.5-preview` (slug: xai-grok-imagine-video-1-5-preview)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class XaiTtsParams(TypedDict, total=False):
    """Inference params for curated model `xai:tts@0` (slug: xai-tts)."""

    model: Literal['xai:tts@0']
    speech: dict[str, object]
    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class XaiTtsResult(TypedDict, total=False):
    """Inference result for curated model `xai:tts@0` (slug: xai-tts)."""

    taskType: Literal['audioInference']
    taskUUID: str
    cost: NotRequired[float]
    audioUUID: str
    audioURL: NotRequired[str]
    audioBase64Data: NotRequired[str]
    audioDataURI: NotRequired[str]
    seed: NotRequired[int]

class XaiGrok43Params(TypedDict, total=False):
    """Inference params for curated model `xai:grok@4.3` (slug: xai-grok-4-3)."""

    model: Literal['xai:grok@4.3']
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    messages: list[dict[str, object]]
    toolChoice: NotRequired[dict[str, object]]
    tools: NotRequired[list[dict[str, object]]]
    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    includeUsage: NotRequired[bool]

class XaiGrok43Result(TypedDict, total=False):
    """Inference result for curated model `xai:grok@4.3` (slug: xai-grok-4-3)."""

    taskType: Literal['textInference']
    taskUUID: str
    cost: NotRequired[float]
    text: str
    finishReason: Literal['stop', 'length', 'content_filter', 'unknown']
    usage: dict[str, object]

class XaiGrokImagineImageQualityParams(TypedDict, total=False):
    """Inference params for curated model `xai:grok-imagine@image-quality` (slug: xai-grok-imagine-image-quality)."""

    model: Literal['xai:grok-imagine@image-quality']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['1K', '2K']]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class XaiGrokImagineImageQualityResult(TypedDict, total=False):
    """Inference result for curated model `xai:grok-imagine@image-quality` (slug: xai-grok-imagine-image-quality)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class XaiGrokImagineImageParams(TypedDict, total=False):
    """Inference params for curated model `xai:grok-imagine@image` (slug: xai-grok-imagine-image)."""

    model: Literal['xai:grok-imagine@image']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['1K']]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class XaiGrokImagineImageResult(TypedDict, total=False):
    """Inference result for curated model `xai:grok-imagine@image` (slug: xai-grok-imagine-image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class XaiGrokImagineVideoParams(TypedDict, total=False):
    """Inference params for curated model `xai:grok-imagine@video` (slug: xai-grok-imagine-video)."""

    model: Literal['xai:grok-imagine@video']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    resolution: NotRequired[Literal['480p', '720p']]
    duration: NotRequired[int]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class XaiGrokImagineVideoResult(TypedDict, total=False):
    """Inference result for curated model `xai:grok-imagine@video` (slug: xai-grok-imagine-video)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Hyper3dRodinGen2Params(TypedDict, total=False):
    """Inference params for curated model `hyper3d:rodin@gen-2` (slug: hyper3d-rodin-gen-2)."""

    model: Literal['hyper3d:rodin@gen-2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    seed: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    taskType: Literal['3dInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['GLB']]
    deliveryMethod: NotRequired[str]

class Hyper3dRodinGen2Result(TypedDict, total=False):
    """Inference result for curated model `hyper3d:rodin@gen-2` (slug: hyper3d-rodin-gen-2)."""

    taskType: Literal['3dInference']
    taskUUID: str
    cost: NotRequired[float]
    outputs: dict[str, object]
    seed: NotRequired[int]

class CreatifyAuroraV1Params(TypedDict, total=False):
    """Inference params for curated model `creatify:aurora@0` (slug: creatify-aurora-v1)."""

    model: Literal['creatify:aurora@0']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class CreatifyAuroraV1Result(TypedDict, total=False):
    """Inference result for curated model `creatify:aurora@0` (slug: creatify-aurora-v1)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class CreatifyAuroraV1FastParams(TypedDict, total=False):
    """Inference params for curated model `creatify:aurora@fast` (slug: creatify-aurora-v1-fast)."""

    model: Literal['creatify:aurora@fast']
    inputs: dict[str, object]
    positivePrompt: NotRequired[str]
    CFGScale: NotRequired[float]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class CreatifyAuroraV1FastResult(TypedDict, total=False):
    """Inference result for curated model `creatify:aurora@fast` (slug: creatify-aurora-v1-fast)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RunwayGen45Params(TypedDict, total=False):
    """Inference params for curated model `runway:1@2` (slug: runway-gen-4-5)."""

    model: Literal['runway:1@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: int
    height: int
    duration: NotRequired[Literal[5, 8, 10]]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RunwayGen45Result(TypedDict, total=False):
    """Inference result for curated model `runway:1@2` (slug: runway-gen-4-5)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RunwayAleph20Params(TypedDict, total=False):
    """Inference params for curated model `runway:aleph@2.0` (slug: runway-aleph-2-0)."""

    model: Literal['runway:aleph@2.0']
    inputs: dict[str, object]
    positivePrompt: str
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RunwayAleph20Result(TypedDict, total=False):
    """Inference result for curated model `runway:aleph@2.0` (slug: runway-aleph-2-0)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RunwayGen4ImageTurboParams(TypedDict, total=False):
    """Inference params for curated model `runway:4@2` (slug: runway-gen-4-image-turbo)."""

    model: Literal['runway:4@2']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RunwayGen4ImageTurboResult(TypedDict, total=False):
    """Inference result for curated model `runway:4@2` (slug: runway-gen-4-image-turbo)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RunwayAlephParams(TypedDict, total=False):
    """Inference params for curated model `runway:2@1` (slug: runway-aleph)."""

    model: Literal['runway:2@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RunwayAlephResult(TypedDict, total=False):
    """Inference result for curated model `runway:2@1` (slug: runway-aleph)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RunwayGen4TurboParams(TypedDict, total=False):
    """Inference params for curated model `runway:1@1` (slug: runway-gen-4-turbo)."""

    model: Literal['runway:1@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    duration: NotRequired[int]
    seed: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RunwayGen4TurboResult(TypedDict, total=False):
    """Inference result for curated model `runway:1@1` (slug: runway-gen-4-turbo)."""

    taskType: Literal['videoInference']
    taskUUID: str
    cost: NotRequired[float]
    videoUUID: str
    videoURL: NotRequired[str]
    videoBase64Data: NotRequired[str]
    videoDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class RunwayGen4ImageParams(TypedDict, total=False):
    """Inference params for curated model `runway:4@1` (slug: runway-gen-4-image)."""

    model: Literal['runway:4@1']
    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: NotRequired[int]
    height: NotRequired[int]
    providerSettings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class RunwayGen4ImageResult(TypedDict, total=False):
    """Inference result for curated model `runway:4@1` (slug: runway-gen-4-image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    cost: NotRequired[float]
    imageUUID: str
    imageURL: NotRequired[str]
    imageBase64Data: NotRequired[str]
    imageDataURI: NotRequired[str]
    seed: NotRequired[int]
    NSFWContent: NotRequired[bool]

class Sd15DistilledArchParams(TypedDict, total=False):
    """Inference params for architecture `sd-1-5-distilled`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Flux1SchnellArchParams(TypedDict, total=False):
    """Inference params for architecture `flux-1-schnell`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SdxlTurboArchParams(TypedDict, total=False):
    """Inference params for architecture `sdxl-turbo`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    refiner: NotRequired[dict[str, object]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Flux1DevArchParams(TypedDict, total=False):
    """Inference params for architecture `flux-1-dev`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    layerDiffuse: NotRequired[bool]
    pulid: NotRequired[dict[str, object]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SdxlHyperArchParams(TypedDict, total=False):
    """Inference params for architecture `sdxl-hyper`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    refiner: NotRequired[dict[str, object]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SdxlArchParams(TypedDict, total=False):
    """Inference params for architecture `sdxl`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    refiner: NotRequired[dict[str, object]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    photoMaker: NotRequired[dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Sd15ArchParams(TypedDict, total=False):
    """Inference params for architecture `sd-1-5`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SdxlDistilledArchParams(TypedDict, total=False):
    """Inference params for architecture `sdxl-distilled`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    refiner: NotRequired[dict[str, object]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Sd21ArchParams(TypedDict, total=False):
    """Inference params for architecture `sd-2-1`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class NoobaiArchParams(TypedDict, total=False):
    """Inference params for architecture `noobai`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    refiner: NotRequired[dict[str, object]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class PonyArchParams(TypedDict, total=False):
    """Inference params for architecture `pony`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    refiner: NotRequired[dict[str, object]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SdxlLcmArchParams(TypedDict, total=False):
    """Inference params for architecture `sdxl-lcm`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    refiner: NotRequired[dict[str, object]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class SdxlLightningArchParams(TypedDict, total=False):
    """Inference params for architecture `sdxl-lightning`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    refiner: NotRequired[dict[str, object]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Sd15HyperArchParams(TypedDict, total=False):
    """Inference params for architecture `sd-1-5-hyper`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Sd15LcmArchParams(TypedDict, total=False):
    """Inference params for architecture `sd-1-5-lcm`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class IllustriousArchParams(TypedDict, total=False):
    """Inference params for architecture `illustrious`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    clipSkip: NotRequired[int]
    promptWeighting: NotRequired[Literal['compel', 'sdEmbeds']]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ipAdapters: NotRequired[list[dict[str, object]]]
    refiner: NotRequired[dict[str, object]]
    hiresFix: NotRequired[Literal[True] | dict[str, object]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class Flux1KontextDevArchParams(TypedDict, total=False):
    """Inference params for architecture `flux-1-kontext-dev`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    acceleratorOptions: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    trueCFGScale: NotRequired[float]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ZImageArchParams(TypedDict, total=False):
    """Inference params for architecture `z-image`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ZImageTurboArchParams(TypedDict, total=False):
    """Inference params for architecture `z-image-turbo`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    negativePrompt: NotRequired[str]
    width: int
    height: int
    seed: NotRequired[int]
    steps: NotRequired[int]
    scheduler: NotRequired[Literal['DDIM', 'DDIMScheduler', 'DDPMScheduler', 'DEISMultistepScheduler', 'Default', 'DPM++', 'DPM++ 2M', 'DPM++ 2M Beta', 'DPM++ 2M Exponential', 'DPM++ 2M Karras', 'DPM++ 2M SDE', 'DPM++ 2M SDE Beta', 'DPM++ 2M SDE Exponential', 'DPM++ 2M SDE Karras', 'DPM++ 2M SDE Uniform', 'DPM++ 2M Uniform', 'DPM++ 3M', 'DPM++ 3M Beta', 'DPM++ 3M Exponential', 'DPM++ 3M Karras', 'DPM++ 3M SDE Uniform', 'DPM++ 3M Uniform', 'DPM++ Beta', 'DPM++ Exponential', 'DPM++ Karras', 'DPM++ SDE', 'DPM++ SDE Beta', 'DPM++ SDE Exponential', 'DPM++ SDE Karras', 'DPM++ Uniform', 'DPM++ Uniform Beta', 'DPM++ Uniform Exponential', 'DPM++ Uniform Karras', 'DPMSolverMultistepInverse', 'DPMSolverMultistepScheduler', 'DPMSolverSinglestepScheduler', 'EDMDPMSolverMultistepScheduler', 'EDMEulerScheduler', 'Euler', 'Euler a', 'Euler Beta', 'Euler Exponential', 'Euler Karras', 'EulerAncestralDiscreteScheduler', 'EulerDiscreteScheduler', 'FlowMatchEulerDiscreteScheduler', 'Heun', 'HeunDiscreteScheduler', 'Heun Karras', 'IPNDMScheduler', 'IPNDM Uniform', 'IPNDM Uniform Beta', 'IPNDM Uniform Exponential', 'IPNDM Uniform Karras', 'KDPM2AncestralDiscreteScheduler', 'KDPM2DiscreteScheduler', 'LCM', 'LCMScheduler', 'LMS', 'LMSDiscreteScheduler', 'LMS Karras', 'PNDMScheduler', 'TCDScheduler', 'UniPC', 'UniPC 2M', 'UniPC 2M Karras', 'UniPC 2M Uniform', 'UniPC 3M', 'UniPC 3M Karras', 'UniPC 3M Uniform', 'UniPC Karras', 'UniPC Uniform', 'UniPC Uniform Beta', 'UniPC Uniform Exponential', 'UniPC Uniform Karras']]
    CFGScale: NotRequired[float]
    strength: NotRequired[float]
    maskMargin: NotRequired[int]
    acceleratorOptions: NotRequired[dict[str, object]]
    outpaint: NotRequired[dict[str, object]]
    lora: NotRequired[list[dict[str, object]]]
    controlNet: NotRequired[list[dict[str, object]]]
    ultralytics: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ExactlyIllustrativeArchParams(TypedDict, total=False):
    """Inference params for architecture `exactly-illustrative`."""

    inputs: NotRequired[dict[str, object]]
    positivePrompt: str
    width: int
    height: int
    settings: NotRequired[dict[str, object]]
    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class VideoInferenceParams(TypedDict, total=False):
    """Loose params for the `videoInference` modality (slug: video)."""

    taskType: Literal['videoInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class ImageInferenceParams(TypedDict, total=False):
    """Loose params for the `imageInference` modality (slug: image)."""

    taskType: Literal['imageInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    outputQuality: NotRequired[int]
    deliveryMethod: NotRequired[str]
    safety: NotRequired[dict[str, object]]

class AudioInferenceParams(TypedDict, total=False):
    """Loose params for the `audioInference` modality (slug: audio)."""

    taskType: Literal['audioInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['MP3', 'WAV', 'FLAC', 'OGG']]
    deliveryMethod: NotRequired[str]
    audioSettings: NotRequired[dict[str, object]]

class ThreeDInferenceParams(TypedDict, total=False):
    """Loose params for the `3dInference` modality (slug: 3d)."""

    taskType: Literal['3dInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    numberResults: NotRequired[int]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['GLB']]
    deliveryMethod: NotRequired[str]

class TextInferenceParams(TypedDict, total=False):
    """Loose params for the `textInference` modality (slug: text)."""

    taskType: Literal['textInference']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    messages: list[dict[str, object]]
    outputFormat: NotRequired[Literal['TEXT']]
    deliveryMethod: NotRequired[str]
    numberResults: NotRequired[int]
    settings: NotRequired[dict[str, object]]
    includeUsage: NotRequired[bool]

class CaptionVideoParams(TypedDict, total=False):
    """Params for the `caption-video` operation."""

    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class RemoveBackgroundParams(TypedDict, total=False):
    """Params for the `remove-background` operation."""

    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]

class UpscaleVideoParams(TypedDict, total=False):
    """Params for the `upscale-video` operation."""

    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class CaptionParams(TypedDict, total=False):
    """Params for the `caption` operation."""

    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str

class RemoveBackgroundImageParams(TypedDict, total=False):
    """Params for the `remove-background-image` operation."""

    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class VectorizeParams(TypedDict, total=False):
    """Params for the `vectorize` operation."""

    taskType: Literal['vectorize']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['SVG']]
    deliveryMethod: NotRequired[str]

class RemoveBackgroundVideoParams(TypedDict, total=False):
    """Params for the `remove-background-video` operation."""

    taskType: Literal['removeBackground']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL']]
    outputFormat: NotRequired[Literal['MP4', 'WEBM', 'MOV']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class CaptionImageParams(TypedDict, total=False):
    """Params for the `caption-image` operation."""

    taskType: Literal['caption']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class UpscaleParams(TypedDict, total=False):
    """Params for the `upscale` operation."""

    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]

class UpscaleImageParams(TypedDict, total=False):
    """Params for the `upscale-image` operation."""

    taskType: Literal['upscale']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    outputQuality: NotRequired[int]
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    inputs: dict[str, object]

class MaskingParams(TypedDict, total=False):
    """Params for the `masking` operation."""

    taskType: Literal['imageMasking']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]
    settings: NotRequired[dict[str, object]]

class PromptEnhanceParams(TypedDict, total=False):
    """Params for the `prompt-enhance` operation."""

    taskType: Literal['promptEnhance']
    taskUUID: str
    webhookURL: NotRequired[str]
    deliveryMethod: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    prompt: str
    promptMaxLength: NotRequired[int]
    promptVersions: NotRequired[int]

class ControlnetPreprocessParams(TypedDict, total=False):
    """Params for the `controlnet-preprocess` operation."""

    taskType: Literal['controlNetPreprocess']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str
    outputType: NotRequired[Literal['URL', 'base64Data', 'dataURI']]
    outputFormat: NotRequired[Literal['JPG', 'PNG', 'WEBP']]
    deliveryMethod: NotRequired[str]
    uploadEndpoint: NotRequired[str]
    ttl: NotRequired[int]
    inputs: dict[str, object]

class TrainingParams(TypedDict, total=False):
    """Params for the `training` operation."""

    taskType: Literal['training']
    taskUUID: str
    webhookURL: NotRequired[str]
    includeCost: NotRequired[bool]
    model: str

class GetTaskDetailsParams(TypedDict, total=False):
    """Params for the `get-task-details` utility task."""

    taskType: Literal['getTaskDetails']
    taskUUID: str

class GetTaskDetailsResult(TypedDict, total=False):
    """Result for the `get-task-details` utility task."""

    taskType: Literal['getTaskDetails']
    taskUUID: str
    request: list[dict[str, object]]
    response: dict[str, object]

class ModelUploadParams(TypedDict, total=False):
    """Params for the `model-upload` utility task."""

    taskType: Literal['modelUpload']
    taskUUID: NotRequired[str]
    category: Literal['checkpoint', 'lora', 'lycoris', 'vae', 'embeddings']
    type: NotRequired[Literal['base', 'inpainting', 'positive', 'negative']]
    architecture: str
    format: Literal['safetensors']
    air: NotRequired[str]
    uniqueIdentifier: NotRequired[str]
    name: str
    version: str
    downloadURL: str
    defaultScheduler: NotRequired[str]
    defaultSteps: NotRequired[int]
    defaultCFG: NotRequired[float]
    defaultStrength: NotRequired[float]
    defaultWeight: NotRequired[float]
    private: NotRequired[bool]
    heroImageURL: NotRequired[str]
    tags: NotRequired[list[str]]
    positiveTriggerWords: NotRequired[str]
    shortDescription: NotRequired[str]
    comment: NotRequired[str]

class ModelUploadResult2(TypedDict, total=False):
    """Result for the `model-upload` utility task."""

    taskType: NotRequired[Literal['modelUpload']]
    taskUUID: str
    status: Literal['validated', 'downloaded', 'optimized', 'stored', 'ready', 'failed']
    message: str
    air: NotRequired[str]

class GetResponseParams(TypedDict, total=False):
    """Params for the `get-response` utility task."""

    taskType: Literal['getResponse']
    taskUUID: str

class GetResponseResult(TypedDict, total=False):
    """Result for the `get-response` utility task."""

    taskType: Literal['getResponse']
    taskUUID: str
    status: Literal['processing', 'success', 'error']
    progress: NotRequired[int]
    error: NotRequired[dict[str, object]]

class PingParams(TypedDict, total=False):
    """Params for the `ping` utility task."""

    taskType: Literal['ping']
    ping: Literal[True]

class PingResult(TypedDict, total=False):
    """Result for the `ping` utility task."""

    pong: Literal[True]

class ImageUploadParams(TypedDict, total=False):
    """Params for the `image-upload` utility task."""

    taskType: Literal['imageUpload']
    taskUUID: str
    image: str

class ImageUploadResult(TypedDict, total=False):
    """Result for the `image-upload` utility task."""

    taskType: Literal['imageUpload']
    taskUUID: str
    imageUUID: str

class AccountManagementParams(TypedDict, total=False):
    """Params for the `account-management` utility task."""

    taskType: Literal['accountManagement']
    taskUUID: str
    operation: Literal['getDetails']

class AccountManagementResult(TypedDict, total=False):
    """Result for the `account-management` utility task."""

    taskType: Literal['accountManagement']
    taskUUID: str
    organizationName: str
    organizationUUID: str
    balance: dict[str, object]
    team: list[dict[str, object]]
    apiKeys: list[dict[str, object]]
    usage: dict[str, object]

class ModelSearchParams(TypedDict, total=False):
    """Params for the `model-search` utility task."""

    taskType: Literal['modelSearch']
    taskUUID: NotRequired[str]
    search: str
    tags: NotRequired[list[str]]
    category: NotRequired[Literal['checkpoint', 'lora', 'lycoris', 'vae', 'embeddings']]
    type: NotRequired[Literal['base', 'inpainting', 'refiner']]
    architecture: NotRequired[str]
    conditioning: NotRequired[Literal['blur', 'canny', 'depth', 'gray', 'hed', 'inpaint', 'inpaintdepth', 'lineart', 'lowquality', 'normal', 'openmlsd', 'openpose', 'outfit', 'pix2pix', 'qrcode', 'scribble', 'seg', 'shuffle', 'sketch', 'softedge', 'tile']]
    visibility: NotRequired[Literal['public', 'private', 'all']]
    limit: NotRequired[int]
    offset: NotRequired[int]

class ModelSearchResult(TypedDict, total=False):
    """Result for the `model-search` utility task."""

    taskType: Literal['modelSearch']
    taskUUID: str
    totalResults: int
    results: list[dict[str, object]]

class AuthenticationParams(TypedDict, total=False):
    """Params for the `authentication` utility task."""

    taskType: Literal['authentication']
    apiKey: str
    connectionSessionUUID: NotRequired[str]

class AuthenticationResult(TypedDict, total=False):
    """Result for the `authentication` utility task."""

    taskType: Literal['authentication']
    connectionSessionUUID: str


# ----------------------------------------------------------- registry data

models: dict[str, ModelEntry] = {
    "alibaba:happyhorse@1.0": ModelEntry(task_type="videoInference", id="alibaba-happyhorse-1-0"),
    "alibaba:qwen-image@2.0": ModelEntry(task_type="imageInference", id="alibaba-qwen-image-2-0"),
    "alibaba:qwen-image@2.0-pro": ModelEntry(task_type="imageInference", id="alibaba-qwen-image-2-0-pro"),
    "alibaba:qwen-image@2512": ModelEntry(task_type="imageInference", id="alibaba-qwen-image-2512"),
    "alibaba:qwen-image@layered": ModelEntry(task_type="imageInference", id="alibaba-qwen-image-layered"),
    "alibaba:qwen@3-tts-1.7b-base": ModelEntry(task_type="audioInference", id="alibaba-qwen3-tts-1-7b-base"),
    "alibaba:qwen@3-tts-1.7b-customvoice": ModelEntry(task_type="audioInference", id="alibaba-qwen3-tts-1-7b-customvoice"),
    "alibaba:qwen@3-tts-1.7b-voicedesign": ModelEntry(task_type="audioInference", id="alibaba-qwen3-tts-1-7b-voicedesign"),
    "alibaba:qwen@3.5-27b": ModelEntry(task_type="textInference", id="alibaba-qwen3-5-27b"),
    "alibaba:qwen@3.5-397b": ModelEntry(task_type="textInference", id="alibaba-qwen3-5-397b"),
    "alibaba:wan@2.6": ModelEntry(task_type="videoInference", id="alibaba-wan2-6"),
    "alibaba:wan@2.6-flash": ModelEntry(task_type="videoInference", id="alibaba-wan2-6-flash"),
    "alibaba:wan@2.6-image": ModelEntry(task_type="imageInference", id="alibaba-wan2-6-image"),
    "alibaba:wan@2.7": ModelEntry(task_type="videoInference", id="alibaba-wan2-7"),
    "alibaba:wan@2.7-image": ModelEntry(task_type="imageInference", id="alibaba-wan2-7-image"),
    "alibaba:wan@2.7-image-pro": ModelEntry(task_type="imageInference", id="alibaba-wan2-7-image-pro"),
    "anthropic:claude@fable-5": ModelEntry(task_type="textInference", id="anthropic-claude-fable-5"),
    "anthropic:claude@haiku-4.5": ModelEntry(task_type="textInference", id="anthropic-claude-haiku-4-5"),
    "anthropic:claude@opus-4.7": ModelEntry(task_type="textInference", id="anthropic-claude-opus-4-7"),
    "anthropic:claude@opus-4.8": ModelEntry(task_type="textInference", id="anthropic-claude-opus-4-8"),
    "anthropic:claude@sonnet-4.6": ModelEntry(task_type="textInference", id="anthropic-claude-sonnet-4-6"),
    "baidu:ernie-image@0": ModelEntry(task_type="imageInference", id="baidu-ernie-image"),
    "baidu:ernie-image@turbo": ModelEntry(task_type="imageInference", id="baidu-ernie-image-turbo"),
    "bfl:1@2": ModelEntry(task_type="imageInference", id="bfl-flux-1-fill-pro"),
    "bfl:1@3": ModelEntry(task_type="imageInference", id="bfl-flux-1-expand-pro"),
    "bfl:2@1": ModelEntry(task_type="imageInference", id="bfl-flux-1-1-pro"),
    "bfl:2@2": ModelEntry(task_type="imageInference", id="bfl-flux-1-1-pro-ultra"),
    "bfl:3@1": ModelEntry(task_type="imageInference", id="bfl-flux-1-kontext-pro"),
    "bfl:4@1": ModelEntry(task_type="imageInference", id="bfl-flux-1-kontext-max"),
    "bfl:5@1": ModelEntry(task_type="imageInference", id="bfl-flux-2-pro"),
    "bfl:6@1": ModelEntry(task_type="imageInference", id="bfl-flux-2-flex"),
    "bfl:7@1": ModelEntry(task_type="imageInference", id="bfl-flux-2-max"),
    "bfl:flux@erase": ModelEntry(task_type="imageInference", id="bfl-flux-erase"),
    "bfl:flux@outpainting": ModelEntry(task_type="imageInference", id="bfl-flux-outpainting"),
    "bfl:flux@vto": ModelEntry(task_type="imageInference", id="bfl-flux-virtual-try-on"),
    "bria:10@1": ModelEntry(task_type="imageInference", id="bria-3-2"),
    "bria:11@1": ModelEntry(task_type="imageInference", id="bria-image-replace-background"),
    "bria:20@1": ModelEntry(task_type="imageInference", id="bria-fibo"),
    "bria:20@3": ModelEntry(task_type="imageInference", id="bria-fibo-lite"),
    "bria:21@1": ModelEntry(task_type="imageInference", id="bria-fibo-edit"),
    "bria:21@2": ModelEntry(task_type="imageInference", id="bria-fibo-edit-tools"),
    "bria:2@1": ModelEntry(task_type="removeBackground", id="bria-rmbg-v2-0"),
    "bria:50@1": ModelEntry(task_type="upscale", id="bria-video-increase-resolution"),
    "bria:51@1": ModelEntry(task_type="removeBackground", id="bria-video-background-removal"),
    "bria:52@1": ModelEntry(task_type="upscale", id="bria-image-increase-resolution"),
    "bria:60@1": ModelEntry(task_type="videoInference", id="bria-video-eraser"),
    "bytedance:2@1": ModelEntry(task_type="videoInference", id="bytedance-seedance-1-0-pro"),
    "bytedance:2@2": ModelEntry(task_type="videoInference", id="bytedance-seedance-1-0-pro-fast"),
    "bytedance:50@1": ModelEntry(task_type="upscale", id="bytedance-video-upscaler"),
    "bytedance:5@0": ModelEntry(task_type="imageInference", id="bytedance-seedream-4-0"),
    "bytedance:5@1": ModelEntry(task_type="videoInference", id="bytedance-omnihuman-1"),
    "bytedance:5@2": ModelEntry(task_type="videoInference", id="bytedance-omnihuman-1-5"),
    "bytedance:seedance@1.5-pro": ModelEntry(task_type="videoInference", id="bytedance-seedance-1-5-pro"),
    "bytedance:seedance@2.0": ModelEntry(task_type="videoInference", id="bytedance-seedance-2-0"),
    "bytedance:seedance@2.0-fast": ModelEntry(task_type="videoInference", id="bytedance-seedance-2-0-fast"),
    "bytedance:seedream@4.5": ModelEntry(task_type="imageInference", id="bytedance-seedream-4-5"),
    "bytedance:seedream@5.0-lite": ModelEntry(task_type="imageInference", id="bytedance-seedream-5-0-lite"),
    "civitai:101055@128078": ModelEntry(task_type="imageInference", id="stabilityai-stable-diffusion-xl-v1-0-vae-fix"),
    "creatify:aurora@0": ModelEntry(task_type="videoInference", id="creatify-aurora-v1"),
    "creatify:aurora@fast": ModelEntry(task_type="videoInference", id="creatify-aurora-v1-fast"),
    "deepseek:v4@flash": ModelEntry(task_type="textInference", id="deepseek-v4-flash"),
    "deepseek:v4@pro": ModelEntry(task_type="textInference", id="deepseek-v4-pro"),
    "exactly:illustrative@training": ModelEntry(task_type="modelUpload", id="exactly-illustrative-training"),
    "exactly:photo@bright-pulse": ModelEntry(task_type="imageInference", id="exactly-photo-bright-pulse"),
    "exactly:photo@distant-reality": ModelEntry(task_type="imageInference", id="exactly-photo-distant-reality"),
    "exactly:photo@extreme-contrast": ModelEntry(task_type="imageInference", id="exactly-photo-extreme-contrast"),
    "exactly:photo@grain-film-look": ModelEntry(task_type="imageInference", id="exactly-photo-grain-film-look"),
    "exactly:photo@journey": ModelEntry(task_type="imageInference", id="exactly-photo-journey"),
    "exactly:photo@warm-light": ModelEntry(task_type="imageInference", id="exactly-photo-warm-light"),
    "fishaudio:s2.1@pro": ModelEntry(task_type="audioInference", id="fish-audio-s2-1-pro"),
    "google:1@1": ModelEntry(task_type="imageInference", id="google-imagen-3"),
    "google:1@2": ModelEntry(task_type="imageInference", id="google-imagen-3-fast"),
    "google:2@0": ModelEntry(task_type="videoInference", id="google-veo-2"),
    "google:2@1": ModelEntry(task_type="imageInference", id="google-imagen-4-preview"),
    "google:2@2": ModelEntry(task_type="imageInference", id="google-imagen-4-ultra"),
    "google:2@3": ModelEntry(task_type="imageInference", id="google-imagen-4-fast"),
    "google:3@0": ModelEntry(task_type="videoInference", id="google-veo-3"),
    "google:3@1": ModelEntry(task_type="videoInference", id="google-veo-3-fast"),
    "google:3@2": ModelEntry(task_type="videoInference", id="google-veo-3-1"),
    "google:3@3": ModelEntry(task_type="videoInference", id="google-veo-3-1-fast"),
    "google:4@1": ModelEntry(task_type="imageInference", id="google-nano-banana"),
    "google:4@2": ModelEntry(task_type="imageInference", id="google-nano-banana-pro"),
    "google:4@3": ModelEntry(task_type="imageInference", id="google-nano-banana-2"),
    "google:gemini@3-flash": ModelEntry(task_type="textInference", id="google-gemini-3-flash"),
    "google:gemini@3.1-flash-lite": ModelEntry(task_type="textInference", id="google-gemini-3-1-flash-lite"),
    "google:gemini@3.1-flash-tts": ModelEntry(task_type="audioInference", id="google-gemini-3-1-flash-tts"),
    "google:gemini@3.1-pro": ModelEntry(task_type="textInference", id="google-gemini-3-1-pro"),
    "google:gemini@3.5-flash": ModelEntry(task_type="textInference", id="google-gemini-3-5-flash"),
    "google:gemma@4-31b": ModelEntry(task_type="textInference", id="google-gemma-4-31b"),
    "google:veo@3.1-lite": ModelEntry(task_type="videoInference", id="google-veo-3-1-lite"),
    "heygen:avatar@4": ModelEntry(task_type="videoInference", id="heygen-avatar-iv"),
    "heygen:avatar@5": ModelEntry(task_type="videoInference", id="heygen-avatar-v"),
    "heygen:video-agent@0": ModelEntry(task_type="videoInference", id="heygen-video-agent"),
    "hyper3d:rodin@gen-2": ModelEntry(task_type="3dInference", id="hyper3d-rodin-gen-2"),
    "ideogram:1@1": ModelEntry(task_type="imageInference", id="ideogram-1-0"),
    "ideogram:1@2": ModelEntry(task_type="imageInference", id="ideogram-1-0-remix"),
    "ideogram:2@1": ModelEntry(task_type="imageInference", id="ideogram-2a"),
    "ideogram:2@2": ModelEntry(task_type="imageInference", id="ideogram-2a-remix"),
    "ideogram:3@1": ModelEntry(task_type="imageInference", id="ideogram-2-0"),
    "ideogram:3@2": ModelEntry(task_type="imageInference", id="ideogram-2-0-remix"),
    "ideogram:3@3": ModelEntry(task_type="imageInference", id="ideogram-2-0-edit"),
    "ideogram:3@4": ModelEntry(task_type="imageInference", id="ideogram-2-0-reframe"),
    "ideogram:4@0": ModelEntry(task_type="imageInference", id="ideogram-4-0"),
    "ideogram:4@1": ModelEntry(task_type="imageInference", id="ideogram-3-0"),
    "ideogram:4@2": ModelEntry(task_type="imageInference", id="ideogram-3-0-remix"),
    "ideogram:4@3": ModelEntry(task_type="imageInference", id="ideogram-3-0-edit"),
    "ideogram:4@4": ModelEntry(task_type="imageInference", id="ideogram-3-0-reframe"),
    "ideogram:4@5": ModelEntry(task_type="imageInference", id="ideogram-3-0-replace-background"),
    "ideogram:layerize-text@0": ModelEntry(task_type="imageInference", id="ideogram-layerize-text"),
    "imagineart:1.5-pro@0": ModelEntry(task_type="imageInference", id="imagineart-1-5-pro"),
    "imagineart:1@5": ModelEntry(task_type="imageInference", id="imagineart-1-5"),
    "imagineart:2.0@0": ModelEntry(task_type="imageInference", id="imagineart-2-0"),
    "inworld:tts@1.5-max": ModelEntry(task_type="audioInference", id="inworld-tts-1-5-max"),
    "inworld:tts@1.5-mini": ModelEntry(task_type="audioInference", id="inworld-tts-1-5-mini"),
    "inworld:tts@2": ModelEntry(task_type="audioInference", id="inworld-tts-2"),
    "klingai:1@1": ModelEntry(task_type="videoInference", id="klingai-1-0-standard"),
    "klingai:1@2": ModelEntry(task_type="videoInference", id="klingai-1-0-pro"),
    "klingai:2@1": ModelEntry(task_type="videoInference", id="klingai-1-5-standard"),
    "klingai:2@2": ModelEntry(task_type="videoInference", id="klingai-1-5-pro"),
    "klingai:3@1": ModelEntry(task_type="videoInference", id="klingai-1-6-standard"),
    "klingai:3@2": ModelEntry(task_type="videoInference", id="klingai-1-6-pro"),
    "klingai:4@3": ModelEntry(task_type="videoInference", id="klingai-2-0-master"),
    "klingai:5@1": ModelEntry(task_type="videoInference", id="klingai-2-1-standard"),
    "klingai:5@2": ModelEntry(task_type="videoInference", id="klingai-2-1-pro"),
    "klingai:5@3": ModelEntry(task_type="videoInference", id="klingai-2-1-master"),
    "klingai:6@0": ModelEntry(task_type="videoInference", id="klingai-2-5-turbo-standard"),
    "klingai:6@1": ModelEntry(task_type="videoInference", id="klingai-2-5-turbo-pro"),
    "klingai:7@1": ModelEntry(task_type="videoInference", id="klingai-lip-sync"),
    "klingai:avatar@2.0-pro": ModelEntry(task_type="videoInference", id="klingai-avatar-2-0-pro"),
    "klingai:avatar@2.0-standard": ModelEntry(task_type="videoInference", id="klingai-avatar-2-0-standard"),
    "klingai:kling-image@3": ModelEntry(task_type="imageInference", id="klingai-image-3-0"),
    "klingai:kling-image@o1": ModelEntry(task_type="imageInference", id="klingai-image-o1"),
    "klingai:kling-image@o3": ModelEntry(task_type="imageInference", id="klingai-image-o3"),
    "klingai:kling-video@2.6-pro": ModelEntry(task_type="videoInference", id="klingai-video-2-6-pro"),
    "klingai:kling-video@2.6-standard": ModelEntry(task_type="videoInference", id="klingai-video-2-6-standard"),
    "klingai:kling-video@3-4k": ModelEntry(task_type="videoInference", id="klingai-video-3-0-4k"),
    "klingai:kling-video@3-pro": ModelEntry(task_type="videoInference", id="klingai-video-3-0-pro"),
    "klingai:kling-video@3-standard": ModelEntry(task_type="videoInference", id="klingai-video-3-0-standard"),
    "klingai:kling-video@3.0-turbo": ModelEntry(task_type="videoInference", id="klingai-video-3-0-turbo"),
    "klingai:kling-video@o3-4k": ModelEntry(task_type="videoInference", id="klingai-video-o3-4k"),
    "klingai:kling-video@o3-pro": ModelEntry(task_type="videoInference", id="klingai-video-o3-pro"),
    "klingai:kling-video@o3-standard": ModelEntry(task_type="videoInference", id="klingai-video-o3-standard"),
    "klingai:kling@o1": ModelEntry(task_type="videoInference", id="klingai-video-o1-pro"),
    "klingai:kling@o1-standard": ModelEntry(task_type="videoInference", id="klingai-video-o1-standard"),
    "krea:krea@2-large": ModelEntry(task_type="imageInference", id="krea-2-large"),
    "krea:krea@2-medium": ModelEntry(task_type="imageInference", id="krea-2-medium"),
    "krea:krea@2-turbo": ModelEntry(task_type="imageInference", id="krea-2-turbo"),
    "lightricks:2@0": ModelEntry(task_type="videoInference", id="lightricks-ltx-2-pro"),
    "lightricks:2@1": ModelEntry(task_type="videoInference", id="lightricks-ltx-2-fast"),
    "lightricks:3@1": ModelEntry(task_type="videoInference", id="lightricks-ltx-2-retake"),
    "lightricks:ltx@2": ModelEntry(task_type="videoInference", id="lightricks-ltx-2"),
    "lightricks:ltx@2.3": ModelEntry(task_type="videoInference", id="lightricks-ltx-2-3"),
    "lightricks:ltx@2.3-fast": ModelEntry(task_type="videoInference", id="lightricks-ltx-2-3-fast"),
    "luma:ray@3.2": ModelEntry(task_type="videoInference", id="luma-ray3-2"),
    "luma:uni@1": ModelEntry(task_type="imageInference", id="luma-uni-1"),
    "luma:uni@1-max": ModelEntry(task_type="imageInference", id="luma-uni-1-max"),
    "memories:1@1": ModelEntry(task_type="caption", id="memories-video-captioning"),
    "memories:2@1": ModelEntry(task_type="caption", id="memories-video-age-detection"),
    "meshy:meshy@6": ModelEntry(task_type="3dInference", id="meshy-6"),
    "meta:sam@3d": ModelEntry(task_type="3dInference", id="meta-sam-3d-objects"),
    "microsoft:trellis-2@4b": ModelEntry(task_type="3dInference", id="microsoft-trellis-2"),
    "minimax:1@1": ModelEntry(task_type="videoInference", id="minimax-01"),
    "minimax:2@1": ModelEntry(task_type="videoInference", id="minimax-01-director"),
    "minimax:2@3": ModelEntry(task_type="videoInference", id="minimax-01-live"),
    "minimax:3@1": ModelEntry(task_type="videoInference", id="minimax-hailuo-02"),
    "minimax:4@1": ModelEntry(task_type="videoInference", id="minimax-hailuo-2-3"),
    "minimax:4@2": ModelEntry(task_type="videoInference", id="minimax-hailuo-2-3-fast"),
    "minimax:m2.5@0": ModelEntry(task_type="textInference", id="minimax-m2-5"),
    "minimax:m2.7@0": ModelEntry(task_type="textInference", id="minimax-m2-7"),
    "minimax:m2.7@highspeed": ModelEntry(task_type="textInference", id="minimax-m2-7-highspeed"),
    "minimax:m3@0": ModelEntry(task_type="textInference", id="minimax-m3"),
    "minimax:music@2.6": ModelEntry(task_type="audioInference", id="minimax-music-2-6"),
    "minimax:music@cover": ModelEntry(task_type="audioInference", id="minimax-music-cover"),
    "minimax:speech@2.8": ModelEntry(task_type="audioInference", id="minimax-speech-2-8"),
    "mirelo:1@1": ModelEntry(task_type="audioInference", id="mirelo-sfx-1-5"),
    "moonshotai:kimi@k2.6": ModelEntry(task_type="textInference", id="moonshotai-kimi-k2-6"),
    "openai:1@1": ModelEntry(task_type="imageInference", id="openai-gpt-image-1"),
    "openai:1@2": ModelEntry(task_type="imageInference", id="openai-gpt-image-1-mini"),
    "openai:3@1": ModelEntry(task_type="videoInference", id="openai-sora-2"),
    "openai:3@2": ModelEntry(task_type="videoInference", id="openai-sora-2-pro"),
    "openai:4@1": ModelEntry(task_type="imageInference", id="openai-gpt-image-1-5"),
    "openai:gpt-image@2": ModelEntry(task_type="imageInference", id="openai-gpt-image-2"),
    "openai:gpt@5.4": ModelEntry(task_type="textInference", id="openai-gpt-5-4"),
    "openai:gpt@5.4-mini": ModelEntry(task_type="textInference", id="openai-gpt-5-4-mini"),
    "openai:gpt@5.4-nano": ModelEntry(task_type="textInference", id="openai-gpt-5-4-nano"),
    "openai:gpt@5.4-pro": ModelEntry(task_type="textInference", id="openai-gpt-5-4-pro"),
    "openai:gpt@5.5": ModelEntry(task_type="textInference", id="openai-gpt-5-5"),
    "picsart:1@1": ModelEntry(task_type="vectorize", id="picsart-image-vectorizer"),
    "pixverse:1@1": ModelEntry(task_type="videoInference", id="pixverse-v3-5"),
    "pixverse:1@2": ModelEntry(task_type="videoInference", id="pixverse-v4"),
    "pixverse:1@3": ModelEntry(task_type="videoInference", id="pixverse-v4-5"),
    "pixverse:1@5": ModelEntry(task_type="videoInference", id="pixverse-v5"),
    "pixverse:1@5-fast": ModelEntry(task_type="videoInference", id="pixverse-v5-fast"),
    "pixverse:1@6": ModelEntry(task_type="videoInference", id="pixverse-v5-5"),
    "pixverse:1@7": ModelEntry(task_type="videoInference", id="pixverse-v5-6"),
    "pixverse:1@8": ModelEntry(task_type="videoInference", id="pixverse-v6"),
    "pixverse:lipsync@1": ModelEntry(task_type="videoInference", id="pixverse-lipsync"),
    "pixverse:modify@0": ModelEntry(task_type="videoInference", id="pixverse-modify"),
    "prunaai:1@1": ModelEntry(task_type="imageInference", id="prunaai-p-image"),
    "prunaai:2@1": ModelEntry(task_type="imageInference", id="prunaai-p-image-edit"),
    "prunaai:p-image@try-on": ModelEntry(task_type="imageInference", id="prunaai-p-image-try-on"),
    "prunaai:p-image@upscale": ModelEntry(task_type="upscale", id="prunaai-p-image-upscale"),
    "prunaai:p-video@0": ModelEntry(task_type="videoInference", id="prunaai-p-video"),
    "prunaai:p-video@animate": ModelEntry(task_type="videoInference", id="prunaai-p-video-animate"),
    "prunaai:p-video@avatar": ModelEntry(task_type="videoInference", id="prunaai-p-video-avatar"),
    "prunaai:p-video@replace": ModelEntry(task_type="videoInference", id="prunaai-p-video-replace"),
    "recraft:1@1": ModelEntry(task_type="vectorize", id="recraft-vectorize"),
    "recraft:v4-pro@0": ModelEntry(task_type="imageInference", id="recraft-v4-pro"),
    "recraft:v4-pro@vector": ModelEntry(task_type="vectorize", id="recraft-v4-pro-vector"),
    "recraft:v4.1-pro@0": ModelEntry(task_type="imageInference", id="recraft-v4-1-pro"),
    "recraft:v4.1-utility-pro@0": ModelEntry(task_type="imageInference", id="recraft-v4-1-utility-pro"),
    "recraft:v4.1-utility@0": ModelEntry(task_type="imageInference", id="recraft-v4-1-utility"),
    "recraft:v4.1@0": ModelEntry(task_type="imageInference", id="recraft-v4-1"),
    "recraft:v4@0": ModelEntry(task_type="imageInference", id="recraft-v4"),
    "recraft:v4@vector": ModelEntry(task_type="vectorize", id="recraft-v4-vector"),
    "rundiffusion:110@101": ModelEntry(task_type="imageInference", id="rundiffusion-juggernaut-lightning-flux"),
    "rundiffusion:120@100": ModelEntry(task_type="imageInference", id="rundiffusion-juggernaut-base-flux"),
    "rundiffusion:130@100": ModelEntry(task_type="imageInference", id="rundiffusion-juggernaut-pro-flux"),
    "rundiffusion:200@100": ModelEntry(task_type="imageInference", id="rundiffusion-juggernaut-z"),
    "runware:100@1": ModelEntry(task_type="imageInference", id="bfl-flux-1-schnell"),
    "runware:101@1": ModelEntry(task_type="imageInference", id="bfl-flux-1-dev"),
    "runware:102@1": ModelEntry(task_type="imageInference", id="bfl-flux-1-fill-dev"),
    "runware:106@1": ModelEntry(task_type="imageInference", id="bfl-flux-1-kontext-dev"),
    "runware:107@1": ModelEntry(task_type="imageInference", id="krea-flux-1-krea-dev"),
    "runware:108@1": ModelEntry(task_type="imageInference", id="alibaba-qwen-image"),
    "runware:108@20": ModelEntry(task_type="imageInference", id="alibaba-qwen-image-edit"),
    "runware:108@22": ModelEntry(task_type="imageInference", id="alibaba-qwen-image-edit-plus"),
    "runware:109@1": ModelEntry(task_type="removeBackground", id="rembg-v1-4"),
    "runware:110@1": ModelEntry(task_type="removeBackground", id="bria-rmbg-v2-0-open"),
    "runware:111@1": ModelEntry(task_type="imageInference", id="flux-1-dev-srpo"),
    "runware:112@1": ModelEntry(task_type="removeBackground", id="birefnet-v1-base"),
    "runware:112@10": ModelEntry(task_type="removeBackground", id="birefnet-portrait"),
    "runware:112@2": ModelEntry(task_type="removeBackground", id="birefnet-v1-base-cod"),
    "runware:112@3": ModelEntry(task_type="removeBackground", id="birefnet-dis"),
    "runware:112@5": ModelEntry(task_type="removeBackground", id="birefnet-general"),
    "runware:112@6": ModelEntry(task_type="removeBackground", id="birefnet-general-resolution-512x512-fp16"),
    "runware:112@7": ModelEntry(task_type="removeBackground", id="birefnet-hrsod-dhu"),
    "runware:112@8": ModelEntry(task_type="removeBackground", id="birefnet-massive-tr-dis5k-tr-tes"),
    "runware:112@9": ModelEntry(task_type="removeBackground", id="birefnet-matting"),
    "runware:150@2": ModelEntry(task_type="caption", id="meta-llava-1-6-mistral-7b"),
    "runware:151@1": ModelEntry(task_type="caption", id="openai-clip-vit-l-14"),
    "runware:152@1": ModelEntry(task_type="caption", id="alibaba-qwen2-5-vl-3b-instruct"),
    "runware:152@2": ModelEntry(task_type="caption", id="alibaba-qwen2-5-vl-7b-instruct"),
    "runware:152@50": ModelEntry(task_type="caption", id="qwen2-5-vl-7b-age-detector"),
    "runware:153@1": ModelEntry(task_type="caption", id="vit-age-classifier"),
    "runware:154@1": ModelEntry(task_type="caption", id="open-age-detection"),
    "runware:180@1": ModelEntry(task_type="imageInference", id="tencent-hunyuanimage-3-0"),
    "runware:190@1": ModelEntry(task_type="videoInference", id="ovi"),
    "runware:200@6": ModelEntry(task_type="videoInference", id="alibaba-wan2-2-a14b"),
    "runware:200@8": ModelEntry(task_type="videoInference", id="alibaba-wan2-2-animate"),
    "runware:201@1": ModelEntry(task_type="videoInference", id="alibaba-wan2-5-preview"),
    "runware:201@10": ModelEntry(task_type="imageInference", id="alibaba-wan2-5-preview-image"),
    "runware:210@1": ModelEntry(task_type="videoInference", id="kandinsky-5-0-lite"),
    "runware:300@1": ModelEntry(task_type="imageInference", id="object-eraser"),
    "runware:35@1": ModelEntry(task_type="imageMasking", id="yolov8n-face"),
    "runware:35@10": ModelEntry(task_type="imageMasking", id="mediapipe-eyes-lips-mesh"),
    "runware:35@11": ModelEntry(task_type="imageMasking", id="mediapipe-nose-eyes-mesh"),
    "runware:35@12": ModelEntry(task_type="imageMasking", id="mediapipe-nose-lips-mesh"),
    "runware:35@13": ModelEntry(task_type="imageMasking", id="mediapipe-nose-mesh"),
    "runware:35@14": ModelEntry(task_type="imageMasking", id="mediapipe-lips-mesh"),
    "runware:35@15": ModelEntry(task_type="imageMasking", id="mediapipe-eyes-mesh"),
    "runware:35@2": ModelEntry(task_type="imageMasking", id="yolov8s-face"),
    "runware:35@3": ModelEntry(task_type="imageMasking", id="yolov8n-hand"),
    "runware:35@4": ModelEntry(task_type="imageMasking", id="yolov8n-person-seg"),
    "runware:35@5": ModelEntry(task_type="imageMasking", id="yolov8s-person-seg"),
    "runware:35@6": ModelEntry(task_type="imageMasking", id="mediapipe-face-full"),
    "runware:35@7": ModelEntry(task_type="imageMasking", id="mediapipe-face-short"),
    "runware:35@8": ModelEntry(task_type="imageMasking", id="mediapipe-face-mesh"),
    "runware:35@9": ModelEntry(task_type="imageMasking", id="mediapipe-face-mesh-eyes-only"),
    "runware:400@1": ModelEntry(task_type="imageInference", id="bfl-flux-2-dev"),
    "runware:400@2": ModelEntry(task_type="imageInference", id="bfl-flux-2-klein-9b"),
    "runware:400@3": ModelEntry(task_type="imageInference", id="bfl-flux-2-klein-9b-base"),
    "runware:400@4": ModelEntry(task_type="imageInference", id="bfl-flux-2-klein-4b"),
    "runware:400@5": ModelEntry(task_type="imageInference", id="bfl-flux-2-klein-4b-base"),
    "runware:400@6": ModelEntry(task_type="imageInference", id="bfl-flux-2-klein-9b-kv"),
    "runware:500@1": ModelEntry(task_type="upscale", id="clarity"),
    "runware:501@1": ModelEntry(task_type="upscale", id="ccsr"),
    "runware:502@1": ModelEntry(task_type="upscale", id="stable-diffusion-latent-upscaler"),
    "runware:503@1": ModelEntry(task_type="upscale", id="swinir"),
    "runware:504@1": ModelEntry(task_type="upscale", id="real-esrgan"),
    "runware:5@1": ModelEntry(task_type="imageInference", id="stabilityai-stable-diffusion-3"),
    "runware:97@1": ModelEntry(task_type="imageInference", id="hidream-i1-full"),
    "runware:97@2": ModelEntry(task_type="imageInference", id="hidream-i1-dev"),
    "runware:97@3": ModelEntry(task_type="imageInference", id="hidream-i1-fast"),
    "runware:ace-step@v1.5-base": ModelEntry(task_type="audioInference", id="ace-step-v1-5-base"),
    "runware:ace-step@v1.5-turbo": ModelEntry(task_type="audioInference", id="ace-step-v1-5-turbo"),
    "runware:ace-step@v1.5-xl-base": ModelEntry(task_type="audioInference", id="ace-step-v1-5-xl-base"),
    "runware:ace-step@v1.5-xl-sft": ModelEntry(task_type="audioInference", id="ace-step-v1-5-xl-sft"),
    "runware:ace-step@v1.5-xl-turbo": ModelEntry(task_type="audioInference", id="ace-step-v1-5-xl-turbo"),
    "runware:controlnet-preprocess@canny": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-canny"),
    "runware:controlnet-preprocess@depth": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-depth"),
    "runware:controlnet-preprocess@lineart": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-lineart"),
    "runware:controlnet-preprocess@lineart-anime": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-lineart-anime"),
    "runware:controlnet-preprocess@mlsd": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-mlsd"),
    "runware:controlnet-preprocess@normalbae": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-normalbae"),
    "runware:controlnet-preprocess@openpose": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-openpose"),
    "runware:controlnet-preprocess@scribble": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-scribble"),
    "runware:controlnet-preprocess@seg": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-seg"),
    "runware:controlnet-preprocess@shuffle": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-shuffle"),
    "runware:controlnet-preprocess@softedge": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-softedge"),
    "runware:controlnet-preprocess@tile": ModelEntry(task_type="controlNetPreprocess", id="controlnet-preprocess-tile"),
    "runware:dia2@2b": ModelEntry(task_type="audioInference", id="dia2-2b"),
    "runware:dia@1.6b": ModelEntry(task_type="audioInference", id="dia-1-6b"),
    "runware:glm-image@0": ModelEntry(task_type="imageInference", id="zai-glm-image"),
    "runware:kandinsky-5.0-image-lite@1": ModelEntry(task_type="imageInference", id="kandinsky-5-0-image-lite"),
    "runware:llama-3-1-8b@prompt-enhancer": ModelEntry(task_type="promptEnhance", id="llama-3-1-8b-prompt-enhancer"),
    "runware:twinflow-z-image-turbo@0": ModelEntry(task_type="imageInference", id="twinflow-z-image-turbo"),
    "runware:z-image@0": ModelEntry(task_type="imageInference", id="alibaba-z-image"),
    "runware:z-image@turbo": ModelEntry(task_type="imageInference", id="alibaba-z-image-turbo"),
    "runway:1@1": ModelEntry(task_type="videoInference", id="runway-gen-4-turbo"),
    "runway:1@2": ModelEntry(task_type="videoInference", id="runway-gen-4-5"),
    "runway:2@1": ModelEntry(task_type="videoInference", id="runway-aleph"),
    "runway:4@1": ModelEntry(task_type="imageInference", id="runway-gen-4-image"),
    "runway:4@2": ModelEntry(task_type="imageInference", id="runway-gen-4-image-turbo"),
    "runway:aleph@2.0": ModelEntry(task_type="videoInference", id="runway-aleph-2-0"),
    "skywork:skyreels@v4": ModelEntry(task_type="videoInference", id="skywork-skyreels-v4"),
    "sourceful:1@0": ModelEntry(task_type="imageInference", id="sourceful-riverflow-1-1-mini"),
    "sourceful:1@1": ModelEntry(task_type="imageInference", id="sourceful-riverflow-1-1"),
    "sourceful:1@2": ModelEntry(task_type="imageInference", id="sourceful-riverflow-1-1-pro"),
    "sourceful:2@1": ModelEntry(task_type="imageInference", id="sourceful-riverflow-2-preview-standard"),
    "sourceful:2@2": ModelEntry(task_type="imageInference", id="sourceful-riverflow-2-preview-fast"),
    "sourceful:2@3": ModelEntry(task_type="imageInference", id="sourceful-riverflow-2-preview-max"),
    "sourceful:riverflow-2.0@fast": ModelEntry(task_type="imageInference", id="sourceful-riverflow-2-0-fast"),
    "sourceful:riverflow-2.0@pro": ModelEntry(task_type="imageInference", id="sourceful-riverflow-2-0-pro"),
    "sourceful:riverflow-2.5@fast": ModelEntry(task_type="imageInference", id="sourceful-riverflow-2-5-fast"),
    "sourceful:riverflow-2.5@pro": ModelEntry(task_type="imageInference", id="sourceful-riverflow-2-5-pro"),
    "sync:lipsync-2-pro@1": ModelEntry(task_type="videoInference", id="sync-lipsync-2-pro"),
    "sync:lipsync-2@1": ModelEntry(task_type="videoInference", id="sync-lipsync-2"),
    "sync:lipsync@3": ModelEntry(task_type="videoInference", id="sync-3"),
    "sync:react-1@1": ModelEntry(task_type="videoInference", id="sync-react-1"),
    "tencent:hunyuan-3d@3.1-pro": ModelEntry(task_type="3dInference", id="tencent-hunyuan-3d-3-1-pro"),
    "tencent:hunyuan-3d@3.1-rapid": ModelEntry(task_type="3dInference", id="tencent-hunyuan-3d-3-1-rapid"),
    "topazlabs:starlight-precise@2.5": ModelEntry(task_type="upscale", id="topazlabs-starlight-precise-2-5"),
    "tripo:v3.1@0": ModelEntry(task_type="3dInference", id="tripo-v3-1"),
    "veed:fabric@1.0": ModelEntry(task_type="videoInference", id="veed-fabric-1-0"),
    "vidu:1@0": ModelEntry(task_type="videoInference", id="vidu-q1-classic"),
    "vidu:1@1": ModelEntry(task_type="videoInference", id="vidu-q1"),
    "vidu:1@5": ModelEntry(task_type="videoInference", id="vidu-1-5"),
    "vidu:2@0": ModelEntry(task_type="videoInference", id="vidu-2-0"),
    "vidu:3@1": ModelEntry(task_type="videoInference", id="vidu-q2-pro"),
    "vidu:3@2": ModelEntry(task_type="videoInference", id="vidu-q2-turbo"),
    "vidu:4@1": ModelEntry(task_type="videoInference", id="vidu-q3"),
    "vidu:4@2": ModelEntry(task_type="videoInference", id="vidu-q3-turbo"),
    "vidu:q1@image": ModelEntry(task_type="imageInference", id="vidu-q1-image"),
    "xai:grok-imagine@image": ModelEntry(task_type="imageInference", id="xai-grok-imagine-image"),
    "xai:grok-imagine@image-quality": ModelEntry(task_type="imageInference", id="xai-grok-imagine-image-quality"),
    "xai:grok-imagine@video": ModelEntry(task_type="videoInference", id="xai-grok-imagine-video"),
    "xai:grok-imagine@video-1.5-preview": ModelEntry(task_type="videoInference", id="xai-grok-imagine-video-1-5-preview"),
    "xai:grok@4.3": ModelEntry(task_type="textInference", id="xai-grok-4-3"),
    "xai:tts@0": ModelEntry(task_type="audioInference", id="xai-tts"),
    "zai:glm@4.7": ModelEntry(task_type="textInference", id="zai-glm-4-7"),
    "zai:glm@5.1": ModelEntry(task_type="textInference", id="zai-glm-5-1"),
}

architecture_task_types: dict[str, str] = {
    "exactly-illustrative": "imageInference",
    "flux-1-dev": "imageInference",
    "flux-1-kontext-dev": "imageInference",
    "flux-1-schnell": "imageInference",
    "illustrious": "imageInference",
    "noobai": "imageInference",
    "pony": "imageInference",
    "sd-1-5": "imageInference",
    "sd-1-5-distilled": "imageInference",
    "sd-1-5-hyper": "imageInference",
    "sd-1-5-lcm": "imageInference",
    "sd-2-1": "imageInference",
    "sdxl": "imageInference",
    "sdxl-distilled": "imageInference",
    "sdxl-hyper": "imageInference",
    "sdxl-lcm": "imageInference",
    "sdxl-lightning": "imageInference",
    "sdxl-turbo": "imageInference",
    "z-image": "imageInference",
    "z-image-turbo": "imageInference",
}

modality_task_types: dict[str, str] = {
    "3d": "3dInference",
    "audio": "audioInference",
    "image": "imageInference",
    "text": "textInference",
    "video": "videoInference"
}

operation_task_types: dict[str, str] = {
    "caption": "caption",
    "caption-image": "caption",
    "caption-video": "caption",
    "controlnet-preprocess": "controlNetPreprocess",
    "masking": "imageMasking",
    "prompt-enhance": "promptEnhance",
    "remove-background": "removeBackground",
    "remove-background-image": "removeBackground",
    "remove-background-video": "removeBackground",
    "training": "training",
    "upscale": "upscale",
    "upscale-image": "upscale",
    "upscale-video": "upscale",
    "vectorize": "vectorize"
}
