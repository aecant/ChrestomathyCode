import sys


def is_palindrome(string):
    lower_alpha = [char.casefold() for char in string if char.isalpha()]
    return lower_alpha == lower_alpha[::-1]


print('_true_' if is_palindrome(sys.argv[1]) else '_false_')
