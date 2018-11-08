import functools
import sys


@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n in (0, 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(sys.argv[1])
if n < 0:
    print('_invalid_')
else:
    print(fibonacci(n))
