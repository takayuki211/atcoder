# import numpy as np
import math

A, B, H, M = map(int, input().split())

L = (2*math.pi*H + (math.pi*M)/30.0)
S = ((math.pi*H)/6.0 + (math.pi*M)/360.0)
ans = math.sqrt(A**2 + B**2 -2*A*B*math.cos(abs(L-S)))
print(ans)
