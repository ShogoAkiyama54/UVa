'''
ACM-ICPL 6095 Digit Solitaire
Accepted by OJ
'''

# test sample input
# lines = open('ACM-ICPC_6095.txt').readlines()
# for line in lines:

import sys

for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    if len(line) == 1:
        print(line)
        continue
    else:
        numbers = [line]
        while True:
            num = 1
            for i in range(len(line)):
                num *= int(line[i])
            num_s = str(num)
            numbers.append(num_s)
            line = num_s
            if len(num_s) == 1:
                break
        print(' '.join(numbers))
