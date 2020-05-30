#!/usr/bin/env python3

import numpy as np
INF = 10**9

n, k = map(int, input().split())
h = np.array(list(map(int, input().split())) + [0]*(k+2), dtype = np.int32)
cost = np.array([INF]*(n+k+2), np.int32)
cost[0] = 0

for i in range(n):
    # np.minimumを使うと2つの配列の各要素の最小値を取得できる
    cost[i+1:i+k+1] = np.minimum(cost[i+1:i+k+1],
                                 cost[i] + np.abs(h[i+1:i+k+1]-h[i]))

print(cost[n-1])
