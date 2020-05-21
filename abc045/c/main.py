#!/usr/bin/env python3

s = input()
n = len(s)-1

ss = []
for l in s:
    ss.append(l)
    ss.append('')
s_list = ss[:-1]
s_list_tmp = s_list.copy()

ans = 0

for i in range(1<<n):
    s_list_tmp = s_list.copy()
    for k in range(n): # 桁数でループ
        if i>>k&1:
            # print(bin(i), k)
            s_list_tmp[2*k+1] = '_'
    s_str = ''.join(s_list_tmp)
    p_str = s_str.split('_')
    p_list = list(map(int, p_str))
    ans += sum(p_list)

print(ans)
