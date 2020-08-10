import os
import sys
import subprocess
from . import register_wrapper, ToolWrapper

class CppLintWrapper(ToolWrapper):
    def run(self, ctx):
        args = [self.get_tool_path(ctx), self.get_tool_option(ctx)]
        REPORT = None
        if ctx.output_path:
            REPORT = open(os.path.join(ctx.output_path, "cpplint_report.txt"), "w")
        args += ctx.get_src_list()
        os.chdir(ctx.src_path)
        subprocess.call(" ".join(args), shell=True, stderr=REPORT)

        if REPORT:
            REPORT.close()
            with open(os.path.join(ctx.output_path, "cpplint_report.txt")) as f:
                sys.stderr.write(f.read())


register_wrapper("cpplint", CppLintWrapper)