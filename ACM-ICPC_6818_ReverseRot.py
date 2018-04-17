"""
10/26/2017
ACM-ICPC 6818 Reverse Rot
Accepted by OJ
"""

import sys

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z', '_', '.', ]

# lines = open('ACM-ICPC_6818.txt').readlines()
# for line in lines:
for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    num, code = line.split()
    reverse = code[::-1]
    encode = ''
    for i in reverse:
        index = alphabet.index(i) + int(num)
        if index >= len(alphabet):
            index -= len(alphabet)
        encode += alphabet[index]
    print(encode)
