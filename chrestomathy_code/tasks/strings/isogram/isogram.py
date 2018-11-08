import sys


def is_isogram(s):
    return len(set(s.casefold())) == len(s)


print("_true_" if is_isogram(sys.argv[1]) else "_false_")
