import contextlib
import hashlib
import json
from pathlib import Path
from typing import Iterator, Optional

import config

_CACHE_DIR = config.BASE_PATH / '.chrestomathy_cache'
_METADATA_FILE = _CACHE_DIR / 'metadata.json'

_files: dict[str, Path] = {}
_hashes: dict[Path, str] = {}


@contextlib.contextmanager
def manage_cache() -> Iterator[None]:
    _load_metadata()
    yield
    _save_metadata()


def get(source_file: Path) -> Optional[Path]:
    return _files.get(_compute_hash(source_file))


def add(source_file: Path, compiled_file: Path) -> None:
    old_hash = _hashes.get(compiled_file)
    if old_hash:
        del _files[old_hash]
        del _hashes[compiled_file]

    hash_ = _compute_hash(source_file)
    _files[hash_] = compiled_file
    _hashes[compiled_file] = hash_


def get_compiled_file_path(source: Path) -> Path:
    return _CACHE_DIR / source.name.replace('.', '_')


def _load_metadata() -> None:
    _CACHE_DIR.mkdir(exist_ok=True)
    with contextlib.suppress(FileNotFoundError), _METADATA_FILE.open() as fin:
        json_data = json.load(fin)
        for hash_, path_str in json_data.items():
            path = Path(path_str)
            _files[hash_] = path
            _hashes[path] = hash_


def _compute_hash(file: Path) -> str:
    return hashlib.sha256(file.read_bytes()).hexdigest()


def _save_metadata() -> None:
    with _METADATA_FILE.open('w') as fout:
        json_data = {hash_: str(path) for hash_, path in _files.items()}
        json.dump(json_data, fout)
