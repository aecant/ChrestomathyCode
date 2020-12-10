import sys
import re


def atoi(s):
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    match = re.match(r'^ *([+-]?\d+).*', s)

    if not match:
        return 0

    num = int(match.group(1))
    num = max(num, INT_MIN)
    num = min(num, INT_MAX)
    return num


print(atoi(sys.argv[1]))
