import sys


def factorial(n):
    if n < 0:
        raise ValueError
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = int(sys.argv[1])
try:
    print(factorial(n))
except ValueError:
    print('_invalid_')
