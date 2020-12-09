import sys
import json


def merge_two_sorted_arrays(list1, list2):
    return sorted(list1 + list2)


list1, list2 = json.load(sys.stdin)
print('\n'.join(map(str, merge_two_sorted_arrays(list1, list2))))
