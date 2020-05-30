#!/usr/bin/env python3
# import sys
# import math
# sys.setrecursionlimit(10**8)
# INF = float('inf')
# PI = math.pi()
# from functools import lru_cache
# @lru_cache(maxsize=None)

import numpy as np
n = int(input())
dp = np.zeros((3,n), dtype=np.int64)
s = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    
