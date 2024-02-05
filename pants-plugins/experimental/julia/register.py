from __future__ import annotations

from typing import Iterable

from experimental.julia.goals import (
    tailor
)
from experimental.julia.target_types import (
    JuliaSourcesGeneratorTarget,
    JuliaSourceTarget,
)
from pants.engine.rules import Rule
from pants.engine.target import Target
from pants.engine.unions import UnionRule


def rules() -> Iterable[Rule | UnionRule]:
    return (*tailor.rules(),)


def target_types() -> Iterable[type[Target]]:
    return (JuliaSourceTarget, JuliaSourcesGeneratorTarget)
