import sys
import json


def merge_two_sorted_arrays(list1, list2):
    result = []
    i1, i2 = 0, 0

    for ir in range(len(list1) + len(list2)):
        if i1 >= len(list1):
            result.extend(list2[i2:])
            break
        elif i2 >= len(list2):
            result.extend(list1[i1:])
            break
        elif list1[i1] < list2[i2]:
            result.append(list1[i1])
            i1 += 1
        else:
            result.append(list2[i2])
            i2 += 1

    return result


list1, list2 = json.load(sys.stdin)
print('\n'.join(map(str, merge_two_sorted_arrays(list1, list2))))
