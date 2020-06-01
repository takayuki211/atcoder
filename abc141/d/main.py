#!/usr/bin/env python3

from heapq import heapify, heappop, heappush

n, m = map(int, input().split())
a = list(map(lambda x: int(x)*-1, input().split()))

heapify(a)

for i in range(m):
    min = heappop(a)
    heappush(a, (-1)*(-1*min//2)) # 要素の挿入

ans = -sum(a)

print(ans)
