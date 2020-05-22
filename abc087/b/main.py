#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)

a = int(input())
b = int(input())
c = int(input())
x = int(input())

xx = x/50
count=0

for na in range(a+1):
    for nb in range(b+1):
        for nc in range(c+1):
            if na*10 + nb*2 + nc == xx:
                count+=1

print(count)
