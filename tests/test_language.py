from pathlib import Path

import context

import code_run
import language

def test_language():
    cmd = 'gcc $source_file'
    source_file = Path('prova.c')
    assert code_run.fill_placeholders(cmd, source_file) == "gcc prova.c"
