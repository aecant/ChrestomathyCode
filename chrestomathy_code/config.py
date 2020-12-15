import json
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent

default_config = BASE_PATH / 'config.json'
local_config = BASE_PATH.parent / '.chrestomathy_config.json'

config_file = local_config if local_config.exists() else default_config

with open(config_file) as fin:
    _config = json.load(fin)

TASKS_DIR = BASE_PATH / _config['tasks_dir']
LANGUAGES: list[dict] = _config['languages']
IGNORED_EXTS: set[str] = set(_config['ignored_extensions'])
IGNORED_TASKS: list[str] = _config['ignored_tasks']
