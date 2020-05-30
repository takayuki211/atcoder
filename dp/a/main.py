#!/usr/bin/env python3
# import sys
# import math
# sys.setrecursionlimit(10**8)
# INF = float('inf')
# PI = math.pi()
# from functools import lru_cache
# @lru_cache(maxsize=None)


n = int(input())
h = list(map(int, input().split()))
cost = [0]*n

cost[0] = 0
cost[1] = abs(h[1]-h[0])

for i in range(2,n):
    cost[i] = min(cost[i-1]+abs(h[i]-h[i-1]), cost[i-2]+abs(h[i]-h[i-2]))
print(cost[n-1])
