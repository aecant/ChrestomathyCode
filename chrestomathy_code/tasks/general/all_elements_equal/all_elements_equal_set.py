import sys


def all_elements_equal(array):
    return len(set(array)) == 1


print('_true_' if all_elements_equal(sys.argv[1:]) else '_false_')
