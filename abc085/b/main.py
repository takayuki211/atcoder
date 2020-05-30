#!/usr/bin/env python3

n = int(input())
d = [0]*n
for i in range(n):
    d[i] = int(input())

ans = len(set(d))
print(ans)
