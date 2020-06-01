#!/usr/bin/env python3

import math
import sys
n = int(input())

# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1


if n==1:
    print(0)
    sys.exit()

ns = int(math.sqrt(n))


# s = make_divisors(n)
# s.remove(1)
#
# ss = [item for item in s if is_prime(item)]
#
# sss = []
# for i in ss:
#     for p in range(2,1000):
#         nn = i**p
#         if nn > n:
#             break
#         sss.append(nn)
#
# ssss = sss + ss
# ssss = list(dict.fromkeys(ssss))
# ssss.sort()
#
# print(ssss)
#
# cnt=0
# for i, num in enumerate(ssss):
#     if n%num==0:
#         n = n//num
#         cnt+=1
#         if n==1:
#             print(cnt)
#             sys.exit()
