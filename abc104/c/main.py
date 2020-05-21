d, g = map(int, input().split())
p = []
c = []
for i in range(d):
    pi, ci = map(int, input().split())
    p.append(pi)
    c.append(ci)

ans = sum(p) # 全部解いた場合を初期値にする

for i in range(1<<d): # 組み合わせループ（2^dパターン）
    score = 0
    count = 0

    # 完答問題の組み合わせから点数を計算する
    for k in range(d):
        if i>>k&1: # 1になっているビットに対応するボーナスポイントを獲得したとする
            score += (k+1)*100*p[k] # 通常得点を加算
            score += c[k] # ボーナスポイントを加算
            count += p[k] # 問題数を加算

    # 完答問題だけでスコアが目標を超えていなければ、残りの問題をスコアが目標に達するまで解く
    if score < g:
        flag = 0
        add_count = 0
        for k in range(d,0,-1): # k桁の上の桁からサーチ
            if not i>>(k-1)&1: # 完答していない問題(k桁目が0になっているビット)について
                for j in range(1, p[k-1], 1): # j問解いたとき
                    score += k*100 # 加算点
                    add_count += 1
                    if score >= g:
                        flag = 1
                        break
            if flag == 1:
                break
        count += add_count

    # スコアが目標を超えていれば回数を更新
    if score >= g and ans > count:
        ans = count

print(ans)
