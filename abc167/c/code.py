import numpy as np
# N, M, X = map(int, input().split())
#
# A = []
# C = []
#
# for i in range(N):
#     L = list(map(int, input().split()))
#     C.append(L[0])
#     A.append(L[1:])
#
# CC = np.array(C)
# AA = np.array(A)
#
# if np.min(np.sum(AA, axis=0)) < X:
#     print('-1')
# else:
#   ans=np.sum(CC)
#
#   import itertools
#   origin_list = list(range(N))
#   for i, _ in enumerate(origin_list, 1):
#       for j in itertools.permutations(origin_list, r=i):
#           SA = np.zeros(M)
#           COST = 0
#           for id in j:
#               SA += AA[id]
#               COST += CC[id]
#           if np.min(SA)>=X and ans > COST:
#               ans = COST
#   print(ans)

n, m, x = map(int, input().split())
c = []
a = []

for i in range(n):
    L = list(map(int, input().split()))
    c.append(L[0])
    a.append(L[1:])

INF = 1001001001
ans = INF

# n = ビット数とみなしてfor文を回す
for s in range(0,1<<n): # 2のn乗.
    cost = 0
    d = [0]*m
    for i in range(n): #
        if s>>i&1: # sのiビット目が1かどうか判定する
            cost += c[i]
            for j in range(m):
                d[j] += a[i][j]
    ok = True
    for j in range(m):
        if d[j] < x:
            ok = False
    if ok:
        ans = min(ans, cost)

if ans == INF:
    print('-1')
else:
    print(ans)
