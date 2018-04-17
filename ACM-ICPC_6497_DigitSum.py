'''
ACM-ICPC 6497 Digit Sum
Accepted by OJ
'''

import sys


def change(list):
    num = ''.join(list)
    index = zeroTreat(num, 0)
    if index != 0:
        num = num[index] + ''.join('0' for i in range(index)) + num[index + 1:]
    return int(num)


def zeroTreat(list, index):
    if list[index] == '0':
        return zeroTreat(list, index + 1)
    return index


# test purpose
# lines = open('ACM-ICPC_6497.txt').readlines()
# for line in lines:
for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    nums = line.split()[1:]
    sort = sorted(nums)
    left = []
    right = []
    zero = 0
    for i in range(len(sort)):
        if sort[i] == '0':
            zero += 1
        if i % 2 == 0:
            left.append(sort[i])
        else:
            right.append(sort[i])
    if len(sort) > 3 and len(sort) % 2 == 1 and zero % 2 == 1:
        index = int(zero / 2)
        leftNum = left[index + 1]
        rightNum = right[index]
        left[index + 1] = rightNum
        right[index] = leftNum
    print(change(left) + change(right))
