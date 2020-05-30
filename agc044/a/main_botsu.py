#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)

t = int(input())
n=[0]*t
a=[0]*t
b=[0]*t
c=[0]*t
d=[0]*t
for i in range(t):
    n[i],a[i],b[i],c[i],d[i] = map(int, input().split())

min_cost = float('inf')
cost = 0
num = 0
flag = 0

dic = {}

def dfs(case, action):
    global num, cost, flag, dic, min_cost

    if action == '+1':
        nnum = num+1
        ncost = cost+d[case]
        flag = 1
    if action == '-1':
        nnum = num-1
        ncost = cost+d[case]
        flag = -1
    if action == '*2':
        nnum = num*2
        ncost = cost+a[case]
        flag = 0
    if action == '*3':
        nnum = num*3
        ncost = cost+b[case]
        flag = 0
    if action == '*5':
        nnum = num*5
        ncost = cost+c[case]
        flag = 0
    print(nnum, ncost)

    # 数が大きい場合
    if nnum > n[case]:
        for num, cost in dic.items():
            if num > n[case] and num < nnum and cost<ncost:
                return

    if nnum not in dic.keys():
        dic[nnum] = cost + d[case]
    else:
        if dic[nnum] > cost + d[case]: # コストが小さいならテーブルを更新
            dic[nnum] = cost + d[case]
        else: # 同じ数値になるためのコストが大きいなら終了
            return

    # 値を更新
    num = nnum
    cost = ncost

    if num == n[case]:
        if min_cost > cost:
            min_cost = cost
        return

    if flag != -1:
        dfs(case, '+1')
    if flag != 1:
        dfs(case, '-1')
    dfs(case, '*2')
    dfs(case, '*3')
    dfs(case, '*5')

for case in range(t):
    min_cost = float('inf')
    dic = {}
    dfs(case, '+1')
    print(dic)

    print(min_cost)
