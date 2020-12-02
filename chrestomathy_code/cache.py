from __future__ import annotations

import contextlib
import hashlib
import json
from pathlib import Path
from typing import Dict, Iterator, Optional

import config

CACHE_DIR = config.BASEPATH / '.chrestomathy_cache'
METADATA_FILE = CACHE_DIR / 'metadata.json'

_files_by_hash: Dict[str, Path] = {}
_hashes_by_file: Dict[Path, str] = {}


@contextlib.contextmanager
def manage_cache() -> Iterator[None]:
    _load_metadata()
    yield
    _save_metadata()


def get(source_file: Path) -> Optional[Path]:
    hash = _compute_hash(source_file)
    return _files_by_hash.get(hash)


def add(source_file: Path, compiled_file: Path) -> None:
    old_hash = _hashes_by_file.get(compiled_file)
    if old_hash:
        del _files_by_hash[old_hash]
        del _hashes_by_file[compiled_file]

    hash = _compute_hash(source_file)
    _files_by_hash[hash] = compiled_file
    _hashes_by_file[compiled_file] = hash


def _compute_hash(file: Path) -> str:
    bytes = file.read_bytes()
    return hashlib.sha256(bytes).hexdigest()


def _load_metadata() -> None:
    CACHE_DIR.mkdir(exist_ok=True)
    with contextlib.suppress(FileNotFoundError), METADATA_FILE.open() as fin:
        json_data = json.load(fin)
        for hash, path in json_data.items():
            _files_by_hash[hash] = Path(path)
            _hashes_by_file[Path(path)] = hash


def _save_metadata() -> None:
    with METADATA_FILE.open('w') as fout:
        json_data = { hash: str(path) for hash, path in _files_by_hash.items() }
        json.dump(json_data, fout)
