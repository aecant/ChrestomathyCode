import sys
import collections

print(collections.Counter(sys.argv[1::]).most_common()[0][0])