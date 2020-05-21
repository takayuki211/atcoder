#!/usr/bin/env python3

s = input()

for i in range(1<<3):
    sum = int(s[0])
    ans = s[0]
    for k in range(3):
        # print(k)
        if i>>k&1:
            sum += int(s[k+1])
            ans += '+' + s[k+1]
        else:
            sum -= int(s[k+1])
            ans += '-' + s[k+1]
    if sum == 7:
        print(ans + '=7')
        break
