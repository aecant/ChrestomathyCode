import json
import fnmatch
from pathlib import Path
from typing import Optional, Callable, Union

import config
from models import Task, Test


def load_tasks(tasks_dir: Path) -> list[Task]:
    tasks = []
    task_files = (f for f in tasks_dir.rglob('*.json') if not _is_excluded(f))
    for task_file in task_files:
        try:
            task = parse_task(task_file)
            tasks.append(task)
        except json.JSONDecodeError:
            print(f'Error parsing {task_file.name}')
    return tasks


def is_valid(expected_output, output: Union[str, list[str]]):
    return expected_output == _adapt_output(output)


def parse_task(task_file: Path) -> Task:
    with task_file.open() as file_in:
        test_dict_list = json.load(file_in)
        tests = [_from_json_dict(dic, task_file.parent) for dic in test_dict_list]
        return Task(task_file.stem, task_file.parent, tests)


def _from_json_dict(dic: dict, task_dir: Path):
    args = _adapt_args(dic.get('args'))
    input_ = _adapt_input(dic, task_dir)
    expected_out = _adapt_output(dic['out'])
    return Test(args, input_, expected_out)


def _adapt_args(args: Union[str, list[str]]) -> list[str]:
    if args is None:
        return []
    if isinstance(args, list):
        return list(map(str, args))
    return [str(args)]


def _adapt_input(dic: dict, task_dir: Path) -> Optional[str]:
    input_adapters: dict[str, Callable[[str], str]] = {
        'in': str,
        'file_in': lambda file_name: (task_dir / file_name).read_text(),
        'json_in': str
    }
    for input_type, adapter in input_adapters.items():
        if input_ := dic.get(input_type):
            return adapter(input_)
    return None


def _adapt_output(output) -> str:
    if isinstance(output, list):
        return '\n'.join(map(str, output))
    return str(output).strip()


def _is_excluded(task_file):
    return any(fnmatch.fnmatch(str(task_file), pattern) for pattern in config.IGNORED_TASKS)
