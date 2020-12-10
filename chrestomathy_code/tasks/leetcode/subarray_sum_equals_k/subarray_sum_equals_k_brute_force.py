import sys
import json


def subarray_sum_equals_k(nums, k):
    count = 0
    for i in range(len(nums)):
        sum_ = 0
        for j in range(i, len(nums)):
            sum_ += nums[j]
            if sum_ == k:
                count += 1
    return count


k, nums = json.load(sys.stdin)
print(subarray_sum_equals_k(nums, k))
