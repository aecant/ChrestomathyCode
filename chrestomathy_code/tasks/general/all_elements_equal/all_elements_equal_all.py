import sys


def all_elements_equal(array):
    return all(elem == array[0] for elem in array)


print('_true_' if all_elements_equal(sys.argv[1:]) else '_false_')
