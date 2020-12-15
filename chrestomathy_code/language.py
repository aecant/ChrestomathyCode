import shutil
from typing import Optional

import config
from models import Language


def parse_config() -> list[Language]:
    return list(map(_get_lang_from_dict, config.LANGUAGES))


def _get_lang_from_dict(lang_dict):
    is_available = _is_available(lang_dict['run'], lang_dict.get('compile'))
    return Language(**lang_dict, is_available=is_available)


def _is_available(run_cmd: str, compile_cmd: Optional[str]) -> bool:
    cmd = compile_cmd or run_cmd
    to_check = cmd.split()[0]
    return shutil.which(to_check) is not None
