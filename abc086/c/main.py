#!/usr/bin/env python3
import sys
n = int(input())
t = [0] * (n+1)
x = [0] * (n+1)
y = [0] * (n+1)

for i in range(1,n+1):
    t[i], x[i], y[i] = map(int, input().split())

for i in range(n):
    length = abs((x[i+1]-x[i])+(y[i+1]-y[i]))
    move = t[i+1]-t[i]
    if move < length:
        print('No')
        sys.exit()
    if (move - length)%2==1:
        print('No')
        sys.exit()
print('Yes')
