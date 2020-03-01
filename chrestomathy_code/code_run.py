from __future__ import annotations

import contextlib
import pathlib
import subprocess
import time
from dataclasses import dataclass
from typing import List, Iterator, Optional

import cache
import task
import language


@contextlib.contextmanager
def manage_compilation(compile_cmd: str, source: pathlib.Path) -> Iterator[Optional[pathlib.Path]]:
    if not compile_cmd:
        yield None
        return

    cached_compiled_file = cache.get(source)
    if cached_compiled_file:
        yield cached_compiled_file
        return

    try:
        compiled = cache.CACHE_DIR / source.name.replace('.', '_')
        cmd = language.adapt_to_context(compile_cmd, source, compiled)
        execute(cmd, check=True)
        cache.add(source, compiled)
        yield compiled
    except subprocess.CalledProcessError:
        raise CompilationError


def run(run_cmd, test: task.Test, source_dir: pathlib.Path) -> ExecutionResult:
    return execute(run_cmd, test.args, input=test.input, capture_output=True, cwd=source_dir)


@dataclass
class ExecutionResult:
    runtime_ns: int
    returncode: int
    stdout:     str
    stderr:     str


def execute(cmd: str, args: List[str] = None, **kwargs) -> ExecutionResult:
    if args is None:
        args = []
    cmd_list = cmd.split() + args

    start = time.perf_counter_ns()
    result = subprocess.run(cmd_list, encoding='utf-8', timeout=5, **kwargs)
    end = time.perf_counter_ns()

    return ExecutionResult(end - start, result.returncode, result.stdout, result.stderr)


class CompilationError(Exception):
    pass
