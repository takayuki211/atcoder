#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)

n = int(input())
c = [0]*n

def div(num):
    if num%2==0:
        c[num-1] += 1
        div(num/2)
    else:
        return

for i in range(1,n+1):
    div(i)

ans = argmax(c)
print(ans)
