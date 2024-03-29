#!/usr/bin/env python3
import sys
from typing import TypeVar

import config
import validate
import task
import language
from models import Task, Language

T = TypeVar('T', Task, Language)


def filter_command_line_args(list_to_filter: list[T]) -> list[T]:
    to_filter = {elem.name.casefold() for elem in list_to_filter}
    chosen = to_filter & to_choose
    if not chosen:
        chosen = to_filter
    chosen -= to_avoid
    return [elem for elem in list_to_filter if elem.name.casefold() in chosen]


to_choose = {arg.casefold()
             for arg in sys.argv[1:] if not arg.startswith('-')}
to_avoid = {arg.partition('-')[-1].casefold()
            for arg in sys.argv[1:] if arg.startswith('-')}

all_tasks = task.load_tasks(config.TASKS_DIR)
tasks = filter_command_line_args(all_tasks)

all_languages = language.parse_config()
languages = filter_command_line_args(all_languages)
filtered_out_exts = {lang.extension for lang in all_languages if lang not in languages}
not_available_exts = {lang.extension for lang in all_languages if not lang.is_available}
ignored_exts = config.IGNORED_EXTS | filtered_out_exts | not_available_exts

validate.validate_all(tasks, languages, ignored_exts)
