from __future__ import annotations

from typing import Iterable
from pants.core.util_rules.external_tool import ExternalTool
from pants.engine.platform import Platform
from pants.engine.unions import UnionRule
from pants.engine.rules import Rule, collect_rules



class Julia(ExternalTool):
    """Julia interpreter (https://julialang.org/)."""

    options_scope = "julia"
    name = "Julia"
    help = "Julia"
    default_version = "v1.10.0"
    default_known_versions = [
        "v1.10.0|macos_arm64 |dc4ca01b1294c02d47b33ef26d489dc288ac68655a03774870c6872b82a9a7d6|146725702",
        "v1.10.0|macos_x86_64|eb1cdf2d373ee40412e8f5ee6b4681916f1ead6d794883903619c7bf147d4f46|145105467",
        "v1.10.0|linux_arm64 |048d96b4398efd524e94be3f49e8829cf6b30c8f3f4b46c75751a4679635e45b|160875701",
        "v1.10.0|linux_x86_64|a7298207f72f2b27b2ab1ce392a6ea37afbd1fbee0f1f8d190b054dcaba878fe|168592090",
    ]

    # We set this because we need the mapping for both `generate_exe` and `generate_url`.
    platform_mapping = {
        "macos_arm64": "darwin_arm64",
        "macos_x86_64": "darwin_amd64",
        "linux_arm64": "linux_arm64",
        "linux_x86_64": "linux_amd64",
    }
    os_mapping = {
        "macos_arm64": "mac",
        "macos_x86_64": "mac",
        "linux_arm64": "linux",
        "linux_x86_64": "linux",
    }
    arch_mapping = {
        "macos_arm64": "aarch64",
        "macos_x86_64": "x64",
        "linux_arm64": "aarch64",
        "linux_x86_64": "x64",
    }

    def generate_url(self, plat: Platform) -> str:
        version = self.version[1:]
        short_version = version.rsplit('.', 1)[0]
        os = self.os_mapping[plat.value]
        arch = self.arch_mapping[plat.value]
        short_arch = '64' if arch == 'x64' else arch
        return f"https://julialang-s3.julialang.org/bin/{os}/{arch}/{short_version}/julia-{version}-{os}{short_arch}.tar.gz"

    def generate_exe(self, plat: Platform) -> str:
        version = self.version[1:]
        return f"./julia-{version}/bin/julia"

def rules() -> Iterable[Rule | UnionRule]:
    return (
        *collect_rules(),
        *Julia.rules(),  # type: ignore[call-arg]
    )
