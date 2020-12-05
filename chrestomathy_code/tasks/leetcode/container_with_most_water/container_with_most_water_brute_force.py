import sys
from itertools import combinations


def container_with_most_water(height: list[int]) -> int:
    return max(calculate_area(i1, a1, i2, a2) for (i1, a1), (i2, a2) in combinations(enumerate(height), 2))


def calculate_area(i1, a1, i2, a2):
    return min(a1, a2) * abs(i2 - i1)


print(container_with_most_water(map(int, sys.argv[1:])))
