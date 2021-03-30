from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Test:
    args: list[str]
    input: Optional[str]
    expected_output: str


@dataclass
class Task:
    name: str
    dir_path: Path
    tests: list[Test]


@dataclass
class Language:
    name: str
    extension: str
    run: str
    is_available: bool
    compile: Optional[str] = None


@dataclass
class ExecutionResult:
    runtime_ns: int
    returncode: int
    stdout: str
    stderr: str


class CompilationError(Exception):
    pass
