#!/usr/bin/env python3

S = input()
n = len(S)

f = 0

if S == S[::-1]:
    L = S[:int((n-1)/2)]
    R = S[int((n+1)/2):]
    if len(L) == 1:
        f == 1
    elif L == L[::-1] and R == R[::-1]:
        f = 1
if f ==0:
    print('No')
else:
    print('Yes')
