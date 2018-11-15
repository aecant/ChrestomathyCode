from pathlib import Path

import context
import language

def test_language():
    cmd = 'gcc $source_file'
    source_file = Path('prova.c')
    assert language.adapt_to_context(cmd, source_file) == "gcc prova.c"
