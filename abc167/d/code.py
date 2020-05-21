import numpy as np
import math

# K = int(input())
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 街番号をいれると行き先街番号を返す
def pos(now):
    return A[now-1]

# 1回目
now = 1
PL=[]
PL.append(now)
POS = pos(now)
PL.append(POS)

if K==1:
    print(POS)

cnt = 1
LOOP_CNT = 0
LOOP_START_POS = -1

if K>1:
    # 2回目〜N回目
    for i in range(1,N):
        POS = pos(POS)
        if POS in PL:
            LOOP_START_POS = POS
            # print('loop start',POS)
            break
        PL.append(POS)

if LOOP_START_POS == 1:
    cnt = 0
else:
    for i in range(1,N):
        if POS == LOOP_START_POS:
            break
        POS = pos(POS)
        cnt+=1

print(LOOP_START_POS)
print(cnt)
