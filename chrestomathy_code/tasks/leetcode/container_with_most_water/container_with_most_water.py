import sys


def container_with_most_water(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        area = calculate_area(left, height[left], right, height[right])

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

        max_area = max(max_area, area)

    return max_area


def calculate_area(i1, a1, i2, a2):
    return min(a1, a2) * abs(i2 - i1)


print(container_with_most_water([int(arg) for arg in sys.argv[1:]]))
