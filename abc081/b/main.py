#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)

import numpy as np

n = int(input())
a = list(map(int, input().split()))

c = 0

def div(a):
    global c
    for i in a:
        if i%2==1:
            print(c)
            sys.exit()
    ll = list(map(lambda x : x/2, a))
    c += 1
    div(ll)

div(a)
