import json
from pathlib import Path
from typing import Dict, List, Set

BASEPATH = Path(__file__).resolve().parent

with open(BASEPATH / 'config.json') as fin:
    _config = json.load(fin)

TASKS_DIR = BASEPATH / _config['tasks_dir']
LANGUAGES: List[Dict] = _config['languages']
IGNORED_EXTS: Set[str] = set(_config['ignored_extensions'])
