from __future__ import annotations

from dataclasses import dataclass

from pants.engine.target import (
    COMMON_TARGET_FIELDS,
    Dependencies,
    FieldSet,
    MultipleSourcesField,
    SingleSourceField,
    Target,
    TargetFilesGenerator,
)

JULIA_FILE_EXTENSIONS = (".jl",)


class JuliaSourceField(SingleSourceField):
    expected_file_extensions = JULIA_FILE_EXTENSIONS


class JuliaGeneratorSourcesField(MultipleSourcesField):
    expected_file_extensions = JULIA_FILE_EXTENSIONS


# -----------------------------------------------------------------------------------------------
# `julia_source` and `julia_sources` targets
# -----------------------------------------------------------------------------------------------


class JuliaSourceTarget(Target):
    alias = "julia_source"
    core_fields = (
        *COMMON_TARGET_FIELDS,
        Dependencies,
        JuliaSourceField,
    )
    help = "A single Julia source file."


class JuliaSourcesGeneratorSourcesField(JuliaGeneratorSourcesField):
    default = tuple(f"*{ext}" for ext in JULIA_FILE_EXTENSIONS)


class JuliaSourcesGeneratorTarget(TargetFilesGenerator):
    alias = "julia_sources"
    core_fields = (
        *COMMON_TARGET_FIELDS,
        JuliaSourcesGeneratorSourcesField,
    )
    generated_target_cls = JuliaSourceTarget
    copied_fields = COMMON_TARGET_FIELDS
    moved_fields = (Dependencies,)
    help = "Generate a `julia_source` target for each file in the `sources` field."


class JuliaDependenciesField(Dependencies):
    required = True


@dataclass(frozen=True)
class JuliaFieldSet(FieldSet):
    required_fields = (JuliaSourceField,)

    source: JuliaSourceField


@dataclass(frozen=True)
class JuliaGeneratorFieldSet(FieldSet):
    required_fields = (JuliaGeneratorSourcesField,)

    sources: JuliaGeneratorSourcesField
