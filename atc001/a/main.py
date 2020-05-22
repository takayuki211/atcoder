#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**7)

h, w = map(int, input().split())
map = [list(input()) for i in range(h)]

# スタート位置を取得
s = [[i, j] for i in range(h) for j in range(w) if map[i][j] == 's'][0]

def dfs(i, j):
    # 範囲外と壁の判定
    if not 0 <= i < h :
        return
    if not 0 <= j < w :
        return
    if map[i][j] == '#':
        return

    # ゴールに到達したら終了
    if map[i][j] == 'g':
        print('Yes')
        sys.exit()

    map[i][j] = '#'

    # 隣を探索する
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

# 探索
dfs(s[0],s[1])
print('No')
