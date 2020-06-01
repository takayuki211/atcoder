#!/usr/bin/env python3

import sys
import numpy as np

n = int(input())
aa = list(map(int, input().split()))

if 0 in aa:
    print(0)
    sys.exit()

a = [s for s in aa if s != 1]
a.sort(reverse=True)

prod = 1
for item in a:
    prod*=item
    if prod>10**18:
        print(-1)
        sys.exit()

print(prod)
