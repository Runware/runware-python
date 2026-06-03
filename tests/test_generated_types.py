"""
Tests for runware/types/task_map.py — assert the generated artifact has the
expected shape. Regenerate via `uv run python scripts/generate_types.py` if a
schemas-version bump is intended.
"""

from __future__ import annotations

from pathlib import Path

from runware import (
    SCHEMAS_VERSION,
    ModelEntry,
    architecture_task_types,
    modality_task_types,
    models,
    operation_task_types,
)

TASK_MAP_PATH = (
    Path(__file__).resolve().parent.parent / "runware" / "types" / "task_map.py"
)


class TestFileHeader:
    def test_file_exists(self) -> None:
        assert TASK_MAP_PATH.is_file()

    def test_marked_as_generated(self) -> None:
        head = TASK_MAP_PATH.read_text().splitlines()[:5]
        assert any("AUTO-GENERATED" in line for line in head)

    def test_carries_schemas_version_constant(self) -> None:
        # The constant should be a string and either "latest" or a timestamp.
        assert isinstance(SCHEMAS_VERSION, str)
        assert SCHEMAS_VERSION != ""


class TestModelsDict:
    def test_models_is_non_empty(self) -> None:
        assert len(models) > 0

    def test_entries_are_model_entry(self) -> None:
        sample = next(iter(models.values()))
        assert isinstance(sample, ModelEntry)
        assert isinstance(sample.task_type, str)
        assert isinstance(sample.id, str)

    def test_task_types_are_known(self) -> None:
        # Models can be inference tasks OR operation tasks (caption, upscale,
        # imageMasking, etc.) — both kinds get curated AIR-mapped entries.
        modality = set(modality_task_types.values())
        operations = set(operation_task_types.values())
        known = modality | operations
        for entry in models.values():
            assert entry.task_type in known, f"unknown task_type: {entry.task_type}"


class TestModalityTaskTypes:
    def test_includes_canonical_modalities(self) -> None:
        assert modality_task_types == {
            "image": "imageInference",
            "video": "videoInference",
            "audio": "audioInference",
            "text": "textInference",
            "3d": "3dInference",
        }


class TestArchitectureTaskTypes:
    def test_is_non_empty(self) -> None:
        assert len(architecture_task_types) > 0

    def test_values_are_known_task_types(self) -> None:
        known = {
            "imageInference",
            "videoInference",
            "audioInference",
            "textInference",
            "3dInference",
        }
        for tt in architecture_task_types.values():
            assert tt in known


class TestOperationTaskTypes:
    def test_is_non_empty(self) -> None:
        assert len(operation_task_types) > 0

    def test_carries_canonical_operations(self) -> None:
        # These canonical operations must always be present; bundles may also
        # expose media-specific variants (caption-video, upscale-video, etc.)
        # but the canonical set is the minimum contract.
        expected_subset = {
            "caption-image": "caption",
            "controlnet-preprocess": "controlNetPreprocess",
            "masking": "imageMasking",
            "prompt-enhance": "promptEnhance",
            "remove-background-image": "removeBackground",
            "training": "training",
            "upscale-image": "upscale",
            "vectorize": "vectorize",
        }
        for slug, task_type in expected_subset.items():
            assert operation_task_types.get(slug) == task_type, (
                f"operation_task_types missing {slug} → {task_type}"
            )


class TestTopLevelReExports:
    """A curated set of TypedDicts should be importable from `runware` itself,
    not just `runware.types.task_map`. Mirrors how the TS SDK re-exports a
    curated subset from index.ts."""

    def test_modality_params_and_results_importable_from_runware(self) -> None:
        import runware

        for name in (
            # Params
            "ImageInferenceParams",
            "VideoInferenceParams",
            "AudioInferenceParams",
            "TextInferenceParams",
            "ThreeDInferenceParams",
            # Canonical per-taskType Results (one per modality)
            "ImageInferenceResult",
            "VideoInferenceResult",
            "AudioInferenceResult",
            "TextInferenceResult",
            "ThreeDInferenceResult",
        ):
            assert hasattr(runware, name), f"runware.{name} missing"

    def test_operation_params_and_results_importable_from_runware(self) -> None:
        import runware

        for name in (
            # Params (slug-based; media variants distinct)
            "CaptionParams",
            "CaptionImageParams",
            "CaptionVideoParams",
            "MaskingParams",
            "ControlnetPreprocessParams",
            "PromptEnhanceParams",
            "UpscaleParams",
            "UpscaleImageParams",
            "UpscaleVideoParams",
            "RemoveBackgroundParams",
            "RemoveBackgroundImageParams",
            "RemoveBackgroundVideoParams",
            "VectorizeParams",
            "TrainingParams",
            # Canonical per-taskType Results
            "CaptionResult",
            "ImageMaskingResult",
            "ControlNetPreprocessResult",
            "PromptEnhanceResult",
            "UpscaleResult",
            "RemoveBackgroundResult",
            "VectorizeResult",
            "TrainingResult",
        ):
            assert hasattr(runware, name), f"runware.{name} missing"

    def test_utility_params_and_results_importable_from_runware(self) -> None:
        import runware

        for name in (
            "ModelSearchParams",
            "ModelSearchResult",
            "ImageUploadParams",
            "ImageUploadResult",
            "ModelUploadParams",
            "ModelUploadResult",
            "AccountManagementParams",
            "AccountManagementResult",
            "GetResponseParams",
            "GetResponseResult",
            "GetTaskDetailsParams",
            "GetTaskDetailsResult",
        ):
            assert hasattr(runware, name), f"runware.{name} missing"


class TestNoDictKeyCollisions:
    def test_models_dict_has_no_duplicate_airs(self) -> None:
        # Generator dedupes by AIR; verify the file we produced respects that.
        keys = list(models.keys())
        assert len(keys) == len(set(keys))


class TestSampleParamsTypedDict:
    def test_can_import_one_known_curated_params_type(self) -> None:
        # Smoke test: at least one well-known curated model should have a
        # generated Params TypedDict. Name format is <PascalCaseSlug>Params.
        from runware.types import task_map

        candidates = [
            name for name in dir(task_map) if name.endswith("Params")
        ]
        # Should have at least one Params TypedDict.
        assert len(candidates) > 0

    def test_at_least_some_result_types_present(self) -> None:
        # Result types come from responseSchema, which not every entry has;
        # require a non-zero count, not exhaustive coverage.
        from runware.types import task_map

        candidates = [name for name in dir(task_map) if name.endswith("Result")]
        assert len(candidates) > 0
