import string
import subprocess
import time
from pathlib import Path
from contextlib import contextmanager
from typing import Iterator, Optional

import cache
from models import Test, ExecutionResult, CompilationError

PROCESS_TIMEOUT = 5


@contextmanager
def manage_compilation(compile_cmd: str, source: Path) -> Iterator[Optional[Path]]:
    if not compile_cmd:
        yield None
        return

    if cached_compiled_file := cache.get(source):
        yield cached_compiled_file
        return

    yield _do_compile(compile_cmd, source)


def run(run_cmd, test: Test, source_dir: Path) -> ExecutionResult:
    return _execute(run_cmd, test.args, input=test.input, capture_output=True, cwd=source_dir)


def fill_placeholders(command: str, source_file: Path, compiled_file: Path = None) -> str:
    substitutions = {
        'source_file': str(source_file),
        'source_dir': str(source_file.parent),
        'source_without_ext': source_file.stem
    }

    if compiled_file is not None:
        substitutions.update({
            'compiled_file': str(compiled_file),
            'compiled_dir': str(compiled_file.parent)
        })

    return string.Template(command).substitute(substitutions)


def _execute(cmd: str, args: list[str] = None, **kwargs) -> ExecutionResult:
    if args is None:
        args = []
    cmd_list = cmd.split() + args

    start = time.perf_counter_ns()
    result = subprocess.run(cmd_list, encoding='utf-8', timeout=PROCESS_TIMEOUT, **kwargs)
    end = time.perf_counter_ns()

    return ExecutionResult(end - start, result.returncode, result.stdout, result.stderr)


def _do_compile(compile_cmd, source):
    try:
        compiled = cache.get_compiled_file_path(source)
        cmd = fill_placeholders(compile_cmd, source, compiled)
        _execute(cmd, check=True)
        cache.add(source, compiled)
        return compiled
    except subprocess.CalledProcessError as error:
        raise CompilationError from error
