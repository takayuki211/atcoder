# AtCoder Beginner Contest 163

# pi=3.14159265358979323846264338327950288
import math
pi = math.pi
R=int(input())
L=2*pi*R
print(L)

# B input
314 15
9 26 5 35 8 9 79 3 23 8 46 2 6 43 3
# B Code
N, M = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
day = N - S
if day < 0:
    day = -1
print(day)

# C
N = int(input())
A = list(map(int, input().split()))
[print(A.count(i+1)) for i in range(N)]

# D
from itertools import combinations
from collections import Counter
N, K = map(int, input().split())
l = [ i for i in range(N+1)]
sum=0
for i in range(K,N+2):
    sum += Counter(combinations(l,i))
print(sum)

import math
N, K = map(int, input().split())
NN = math.factorial(N + 1)%1000000007
NR = math.factorial(N + 1 - K)%1000000007
R = math.factorial(K)%1000000007
print(NN//(NR*R))
# //は割り算。小数点以下は切り捨てる。



# E
N = int(input())
A = list(map(int, input().split()))
ocuppied = [0] * N
sum=0

while(max(A)!=0):
    # 最大活発度
    m = max(A)
    # 最大活発度のインデックスリストを取得
    max_val_index = [i for i, j in enumerate(A) if j == m]

    # 嬉しさスコアが最大になる移動前要素と移動後位置を特定する
    max_dist_position = []*len(max_val_index)
    ureshisa_score = []*len(max_val_index)
    for ind in range(len(max_val_index)):
        # 空いているインデックスを取得
        pos_after_candidate_index = [i for i, j in enumerate(ocuppied) if j == 0]
        # 最大距離になる位置とそのときのスコアの取得
        distance_list = map(lambda x: abs(x - max_val_index[ind]), pos_after_candidate_index)
        max_dist = max(distance_list)
        max_dist_position[ind] = [i for i, j in enumerate(distance_list) if j == max_dist][0]
        ureshisa_score[ind] = A[max_val_index[ind]]*max_dist
    max_score = max(ureshisa_score)
    ind = [i for i, j in enumerate(ureshisa_score) if j == max_score][0]
    # 移動の情報の計算
    pos_before = max_val_index[ind]
    pos_after = max_dist_position[ind]
    score = ureshisa_score[ind]
    # 移動処理(値の更新)
    A[pos_before] = 0
    ocuppied[pos_after] = 1
    sum += score
print(sum)
