from __future__ import annotations

import shutil
import string
from dataclasses import dataclass
from pathlib import Path
from typing import List

import config


@dataclass(frozen=True)
class Language:
    name:       str
    extension:  str
    run:        str
    compile:    str = ''

    def is_available(self):
        cmd = self.compile if self.compile else self.run
        to_check = cmd.split()[0]
        return shutil.which(to_check) is not None


def list_from_config() -> List[Language]:
    return [Language(**lang_dict) for lang_dict in config.LANGUAGES]


def adapt_to_context(command: str, source_file: Path, compiled_file: Path = None) -> str:
    substitutions = {
        'source_file':          str(source_file),
        'source_dir':           str(source_file.parent),
        'source_without_ext':   source_file.stem
    }
    if compiled_file is not None:
        substitutions.update(
            {
                'compiled_file':    str(compiled_file),
                'compiled_dir':     str(compiled_file.parent)
            }
        )
    return string.Template(command).substitute(substitutions)
