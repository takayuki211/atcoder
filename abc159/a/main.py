#!/usr/bin/env python3

M, N = map(int, input().split())

ans=0

if M<=1:
    if N<=1:
        ans = 0
    else:
        ans = N*(N-1)/2
elif N<=1:
    ans = M*(M-1)/2

if M>1 and N>1:
    ans = M*(M-1)/2 + N * (N-1)/2

print(int(ans))
