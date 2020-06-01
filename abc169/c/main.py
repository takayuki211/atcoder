#!/usr/bin/env python3
import sys
import math
from decimal import Decimal

a, b = map(Decimal, input().split())

if a==0 or b==0.00:
    print(0)
    sys.exit()

ans = int(a*b)

print(ans)
