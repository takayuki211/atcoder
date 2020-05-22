#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)

import math

n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(n):
    for j in range(n):
        l = (x[j]-x[i])**2 + (y[j]-y[i])**2
        if ans < l:
            ans = l
print(math.sqrt(ans))
