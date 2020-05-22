#!/usr/bin/env python3

h, w = map(int, input().split())
map = [list(list(input())) for i in range(h)]

s = [[i, j] for i in range(h) for j in range(w) if map[i][j] == 's'][0]

def search(i, j):

    # 範囲外と壁の判定
    if i<0 or h-1<i :
        return
    if j<0 or w-1<j:
        return
    if map[i][j] == '#':
        return
    if map[i][j] == 'X':
        return

    # 探索地点に応じた処理
    if map[i][j] == '.' or 'g':
        map[i][j] = 'X'

    search(i+1, j)
    search(i-1, j)
    search(i, j+1)
    search(i, j-1)

# 探索
search(s[0],s[1])

# mapにgが残っていない＝探索できた
m = sum(map,[])
if 'g' in m:
    print('No')
else:
    print('Yes')
