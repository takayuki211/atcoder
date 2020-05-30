#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = sum(a[::2]) - sum(a[1::2])
print(ans)
