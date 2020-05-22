#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)

n, x = map(int, input().split())
m = [int(input()) for i in range(n)]
gram = x - sum(m)
count = n
d = min(m)
ans = count + gram//d
print(ans)
