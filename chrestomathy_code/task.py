from __future__ import annotations

import json
import fnmatch
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Union, Optional, Dict, Callable

import config


@dataclass(frozen=True)
class Task:
    name:       str
    dirpath:    Path
    tests:      List[Test] = field(hash=False)

    @staticmethod
    def from_json(task_file: Path) -> Task:
        with task_file.open() as file_in:
            test_dict_list = json.load(file_in)
            tests = [Test.from_json_dict(dic, task_file.parent)
                     for dic in test_dict_list]
            return Task(task_file.stem, task_file.parent, tests)


@dataclass(frozen=True)
class Test:
    args:               List[str]
    input:              Optional[str]
    expected_output:    str

    def is_valid(self, output: Union[str, List[str]]):
        return self.expected_output == Test._adapt_output(output)

    @staticmethod
    def from_json_dict(dic: dict, task_dir: Path):
        args = Test._adapt_args(dic.get('args'))
        input = Test._adapt_input(dic, task_dir)
        expected_out = Test._adapt_output(dic['out'])
        return Test(args, input, expected_out)

    @staticmethod
    def _adapt_args(args) -> List[str]:
        if args is None:
            return []
        if not isinstance(args, list):
            args = [args]
        return [str(arg) for arg in args]

    @staticmethod
    def _adapt_input(dic: dict, task_dir: Path) -> Optional[str]:
        input_adapters: Dict[str, Callable[[str], str]] = {
            'in': str,
            'file_in': lambda file_name: (task_dir / file_name).read_text(),
            'json_in': json.dumps
        }
        for input_type, adapter in input_adapters.items():
            if input_ := dic.get(input_type):
                return adapter(input_)
        return None

    @staticmethod
    def _adapt_output(output) -> str:
        if isinstance(output, list):
            return '\n'.join(map(str, output))
        return str(output).strip()


def _is_excluded(task_file):
    return any(fnmatch.fnmatch(str(task_file), pattern) for pattern in config.IGNORED_TASKS)


def load_tasks(tasks_dir: Path) -> List[Task]:
    tasks = []
    task_files = (f for f in tasks_dir.rglob('*.json') if not(_is_excluded(f)))
    for task_file in task_files:
        try:
            task = Task.from_json(task_file)
            tasks.append(task)
        except json.JSONDecodeError:
            print(f'Error parsing {task_file.name}')
    return tasks
