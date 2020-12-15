import sys


def count_half(height: list[int]) -> int:
    sorted_tuples = sorted(enumerate(height), key=lambda t: t[1])
    max_pos = 0
    trapped = 0

    while sorted_tuples:
        next_max_pos, next_max_height = sorted_tuples.pop()

        if next_max_pos <= max_pos:
            continue

        for h in height[max_pos + 1: next_max_pos]:
            trapped += next_max_height - h

        max_pos = next_max_pos

    return trapped


def count_trap_water(height: list[int]) -> int:
    if not height:
        return 0

    max_pos, _ = max(enumerate(height), key=lambda t: t[1])

    left_half = height[max_pos::-1]
    right_half = height[max_pos:]

    return count_half(left_half) + count_half(right_half)


print(count_trap_water(list(map(int, sys.argv[1:]))))
