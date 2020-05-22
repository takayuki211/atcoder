#!/usr/bin/env python3
import sys
# sys.setrecursionlimit(10**7)

n = int(input())

for i in range(26):
    for j in range(15):
        if n == 4*i + 7*j:
            print('Yes')
            sys.exit()
print('No')
