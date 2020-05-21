import numpy as np
import math
A, B, C, K = map(int, input().split())

# ans = 0
# if K<=A:
#     ans = K
# else:
#     if K-A <= B:
#         ans = A
#     else:
#         ans = A - (K - A - B)

xa = min(A, K) # Aの枚数
K -= xa # 残り枚数をへらす
xb = min(B,K) # Bの枚数
K -= xb # 残り枚数をへらす
xc = K # Cの枚数
ans = xa - xc
print(ans)


## 線形計画問題（LP）
# 1次式の制約がたくさん用意されている。線形なので、2乗は現れない
# 今回は整数なのでIP(Integral Plannign)
# 1 * xa + 0 * xb + (-1) * xc
# を最大化する問題。多項式時間で解けるらしい。
