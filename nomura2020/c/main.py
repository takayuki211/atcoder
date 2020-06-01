#!/usr/bin/env python3

import sys
import math
# sys.setrecursionlimit(10**8)
# INF = float('inf')
# PI = math.pi()
# from functools import lru_cache
# @lru_cache(maxsize=None)

n = int(input())
a = list(map(int, input().split()))

min = a[n]
max = a[n]
sum = a[n]

for d in range(n-1,-1,-1):
    min = a[d] + math.ceil(min/2)
    max = a[d] + math.ceil(max)
    if max > 2**d-a[d]:
        max = 2**d-a[d]
    # print(min,max,sum)
    sum+=max

if 1<min or max<1:
    print(-1)
    sys.exit()

print(sum)
