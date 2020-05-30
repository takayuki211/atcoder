#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)

n, a, b = map(int, input().split())

ans = 0

# for i in range(1, n+1):
#     s = str(i)
#     sum = 0
#     for j in s:
#         sum += int(j)
#     if a <= sum <= b:
#         ans += i

for i in range(1, n+1):
    sum = 0
    num = i
    while num > 0:
        sum += num%10 # 10で割ったあまりを取得することで最下位桁を取る
        num = num//10 # 10で割った商を取得することで一桁ずらす
    if a <= sum <=b:
        ans += i

print(ans)
