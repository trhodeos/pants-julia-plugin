from pants.engine.platform import Platform

from pants.core.goals.repl import ReplRequest
from pants.core.util_rules.external_tool import DownloadedExternalTool, ExternalToolRequest



from pants.engine.rules import Get, rule
from pants.util.logging import LogLevel
from pants.core.goals.repl import ReplImplementation
from pants.engine.rules import collect_rules
from pants.engine.unions import UnionRule

from experimental.julia.subsystems.julia import Julia

import logging

log = logging.getLogger(__name__)

class JuliaRepl(ReplImplementation):
    name = "julia"

@rule(level=LogLevel.DEBUG)
async def create_julia_repl_request(repl: JuliaRepl, julia: Julia, platform: Platform) -> ReplRequest:
    # TODO: pull this out into a Julia environment
    downloaded_julia = await Get(
        DownloadedExternalTool,
        ExternalToolRequest,
        julia.get_request(platform)
    )

    return ReplRequest(
        digest=downloaded_julia.digest, args=("{chroot}/" + downloaded_julia.exe,)
    )


def rules():
    return [
        *collect_rules(),
        UnionRule(ReplImplementation, JuliaRepl),
    ]
