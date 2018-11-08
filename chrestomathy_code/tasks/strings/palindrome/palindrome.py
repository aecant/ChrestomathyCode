import sys


def is_palindrome(s):
    low_alpha = list(map(str.casefold, filter(str.isalpha, s)))
    return low_alpha == low_alpha[::-1]


print('_true_' if is_palindrome(sys.argv[1]) else '_false_')
