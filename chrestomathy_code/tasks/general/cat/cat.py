import sys
from pathlib import Path

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print(Path(arg).read_text(), end='')
else:
    print(sys.stdin.read())
