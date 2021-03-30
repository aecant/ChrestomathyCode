from pathlib import Path

import cache
import code_run
from task import is_valid
from models import Task, Test, ExecutionResult, Language, CompilationError


def validate_all(tasks: list[Task], languages: list[Language], ignored_extensions: set[str]) -> None:
    languages_ext = {lang.extension: lang for lang in languages if lang.is_available}
    with cache.manage_cache():
        for task in tasks:
            for source in task.dir_path.glob('[!.]*.*'):
                ext = source.suffix
                if ext in languages_ext:
                    validate_task(task, source, languages_ext[ext])
                elif ext not in ignored_extensions:
                    print(f'Unknown extension: "{ext}", cannot run {source}')


def validate_task(task: Task, source: Path, lang: Language) -> None:
    try:
        with code_run.manage_compilation(lang.compile, source) as compiled_file:
            print(f'{source.name}: ', end='')
            all_ok = True
            total_runtime_ns = 0
            run_cmd = code_run.fill_placeholders(lang.run, source, compiled_file)

            for test in task.tests:
                result = code_run.run(run_cmd, test, source.parent)
                total_runtime_ns += result.runtime_ns
                if not is_valid(test.expected_output, result.stdout):
                    if all_ok:
                        print()  # just formatting the output
                        all_ok = False
                    print_failure(test, result)

            if all_ok:
                average_elapsed_ns = total_runtime_ns / len(task.tests)
                print(f'ok: {average_elapsed_ns * 1e-06:.0f} ms')
    except CompilationError:
        print(f'Failed to compile {source}')


def print_failure(test: Test, result: ExecutionResult):
    print(f'\tfailed: for arguments {test.args!r}, stdin {test.input!r}, '
          f'expected {test.expected_output!r}, got {result.stdout.strip()!r}')
    print(result.stderr, end='')
