import sys

num = int(sys.argv[1])

for i in range(1, num + 1):
    out = ''
    if i % 3 == 0:
        out += 'Fizz'
    if i % 5 == 0:
        out += 'Buzz'

    print(out if out != '' else i)
