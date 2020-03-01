import sys
import collections

numbers = (int(arg) for arg in sys.argv[1::])

num_freq = collections.defaultdict(lambda: 0)

for number in numbers:
    num_freq[number] = num_freq[number] + 1

max_freq = max(num_freq.values())
most_frequent = next(num for num, freq in num_freq.items() if freq == max_freq)
print(most_frequent)