import json
from pathlib import Path
from typing import Dict, List, Set

BASEPATH = Path(__file__).resolve().parent

default_config = BASEPATH / 'config.json'
local_config = BASEPATH.parent / '.chrestomathy_config.json'

config_file = local_config if local_config.exists() else default_config

with open(config_file) as fin:
    _config = json.load(fin)

TASKS_DIR = BASEPATH / _config['tasks_dir']
LANGUAGES: List[Dict] = _config['languages']
IGNORED_EXTS: Set[str] = set(_config['ignored_extensions'])
