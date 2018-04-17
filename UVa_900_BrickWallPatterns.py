'''
UVa 900 Blick Wall Patterns
Accepted by OJ
'''

import sys

store = {1: 1, 2: 2}


def fibonacci(brick):
    if brick in store.keys():
        return store[brick]
    num = fibonacci(brick - 2) + fibonacci(brick - 1)
    store[brick] = num
    return num


for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    brick = int(line)
    pattern = fibonacci(brick)
    print(pattern)
