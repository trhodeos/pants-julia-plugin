import logging

from experimental.julia.subsystems.julia import Julia
from pants.core.goals.repl import ReplImplementation, ReplRequest
from pants.core.util_rules.external_tool import (
    DownloadedExternalTool,
    ExternalToolRequest,
)
from pants.engine.platform import Platform
from pants.engine.rules import Get, collect_rules, rule
from pants.engine.unions import UnionRule
from pants.util.logging import LogLevel

log = logging.getLogger(__name__)


class JuliaRepl(ReplImplementation):
    name = "julia"


@rule(level=LogLevel.DEBUG)
async def create_julia_repl_request(
    repl: JuliaRepl, julia: Julia, platform: Platform
) -> ReplRequest:
    # TODO: pull this out into a Julia environment
    downloaded_julia = await Get(
        DownloadedExternalTool, ExternalToolRequest, julia.get_request(platform)
    )

    return ReplRequest(
        digest=downloaded_julia.digest, args=("{chroot}/" + downloaded_julia.exe,)
    )


def rules():
    return [
        *collect_rules(),
        UnionRule(ReplImplementation, JuliaRepl),
    ]
