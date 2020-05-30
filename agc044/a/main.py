#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
# from functools import lru_cache
# @lru_cache(maxsize=None)

t = int(input())
INF = float('inf')

for _ in range(t):
    n, a, b, c, d = map(int, input().split())
    mem = {}

    def solve(n):
        if n==0: return 0
        if n==1: return d

        if n in mem: return mem[n]

        tmp = n*d
        if n%2==0:
            tmp = min(tmp, solve(n//2)+a)
        else:
            # 2で割り切れないときは、1たして2で割るケースと1ひいて2で割るケース
            tmp = min(tmp, solve(n//2)+a+d, solve(n//2+1)+a+d)

        if n%3==0:
            tmp = min(tmp, solve(n//3)+b)
        else:
            p = n%3
            u = 3-p
            # 3で割り切れないときは、p回1引いて3で割るケースと、u回1たして3で割るケース
            tmp = min(tmp, solve(n//3)+b+p*d, solve(n//3+1)+b+u*d)

        if n%5==0:
            tmp = min(tmp, solve(n//5)+c)
        else:
            p = n%5
            u = 5-p
            # 5で割り切れないときは、p回1引いて5で割るケースと、u回1たして5で割るケース
            tmp = min(tmp, solve(n//5)+c+p*d, solve(n//5+1)+c+u*d)
        mem[n] = tmp
        return tmp

    print(solve(n))
