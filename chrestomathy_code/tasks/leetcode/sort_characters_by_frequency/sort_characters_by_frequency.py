import sys
from collections import Counter


def sort_by_frequency(s):
    freq_dict = Counter(s)
    chars_with_freq = sorted(freq_dict.items(), key=lambda t: t[1], reverse=True)
    return ''.join(char * freq for char, freq in chars_with_freq)


print(sort_by_frequency(sys.argv[1]))
