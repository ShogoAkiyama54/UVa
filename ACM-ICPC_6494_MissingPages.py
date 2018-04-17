'''
ACM-ICPC 6494 Missing Pages
Accepted by OJ
'''

import sys

for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    nums = line.split()
    paper = int(nums[0])
    num = int(nums[1])
    pages = []
    if num % 2 == 0:
        pages.append(num - 1)
        pages.append(paper - num + 1)
        pages.append(paper - num + 2)
    else:
        pages.append(num + 1)
        pages.append(paper - num)
        pages.append(paper - num + 1)
    pages = sorted(pages)
    result = ''
    for i in range(len(pages)):
        result += str(pages[i]) + ' '

    print(result.strip())
