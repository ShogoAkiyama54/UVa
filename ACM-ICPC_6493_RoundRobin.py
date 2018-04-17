'''
ACM-ICPC 6493 Round Robin
Accepted by OJ
'''

import sys

# test input
# lines = open('ACM-ICPC_6493.txt').readlines()
# for line in lines:
for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    people, num = (int(s) for s in line.split())
    group = [0 for i in range(people)]
    lastIndex = 0

    while True:
        for i in range(num):
            group[(lastIndex + i) % len(group)] += 1
        lastIndex = (lastIndex + num) % len(group) - 1
        del group[lastIndex]
        isFinished = True
        for val in group:
            if not val == group[0]:
                isFinished = False
                break
        if isFinished:
            print('%d %d' % (len(group), group[0]))
            break
