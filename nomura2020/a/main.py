#!/usr/bin/env python3

# import sys
# import math
# sys.setrecursionlimit(10**8)
# INF = float('inf')
# PI = math.pi()
# from functools import lru_cache
# @lru_cache(maxsize=None)

# n = int(input())
h1, m1, h2, m2, k = map(int, input().split())
# c = list(map(int, input().split()))
# s = [list(map(int,list(input()))) for i in range(h)]

if h1<=h2:
    ans = h2*60+m2 - (h1*60+m1) - k
else:
    ans = (24+h2)*60+m2 - (h1*60+m1) -k
print(ans)
