import sys
import json


def two_sum(nums, target):
    diffs = {}
    for i, num in enumerate(nums):
        if num in diffs:
            return diffs[num], i
        diffs[target - num] = i


target, nums = json.load(sys.stdin)
print('\n'.join(map(str, two_sum(nums, target))))
