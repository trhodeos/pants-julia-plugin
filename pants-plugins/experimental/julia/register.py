from __future__ import annotations

from collections.abc import Iterable

from experimental.julia.goals import repl, tailor
from experimental.julia.subsystems import julia
from experimental.julia.target_types import (
    JuliaSourcesGeneratorTarget,
    JuliaSourceTarget,
)
from pants.engine.rules import Rule
from pants.engine.target import Target
from pants.engine.unions import UnionRule


def rules() -> Iterable[Rule | UnionRule]:
    return (
        *tailor.rules(),
        *repl.rules(),
        *julia.rules(),
    )


def target_types() -> Iterable[type[Target]]:
    return (JuliaSourceTarget, JuliaSourcesGeneratorTarget)
