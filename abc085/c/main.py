#!/usr/bin/env python3

N, Y = map(int, input().split())
for x in range(N+1):
    for y in range(N-x+1):
        z = N-x-y
        if 0<=z<=2000 and x*10000+y*5000+z*1000 == Y:
            print(x,y,z)
            exit()
print(-1,-1,-1)
