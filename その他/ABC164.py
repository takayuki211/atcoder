# AtCoder Beginner Contest 164
#A
S, W = map(int, input().split())
if W >= S:
    print('unsafe')
else:
    print('safe')

#B
A, B, C, D = map(int, input().split())
TN = A // D
Tmod = A % D
AN = C // B
Amod = C % B
if Tmod>0:
    TN+=1 # 青木くんに必要な攻撃回数
if Amod>0:
    AN+=1# 高橋くんに必要な攻撃回数
if AN<=TN:
    print('Yes')
else:
    print('No')

#C
N = int(input())
S =[]
for i in range(N):
    S.append(str(input()))
SS = set(S)
print(len(SS))

#D・・・時間切れ
S = list(map(int, list(input())))
n = len(S)
ans=0
for i in range(n-4):
    for j in range(i+3,n):
        NUM=0
        cnt=0
        for p in range(j,i-1,-1):
            NUM += S[p] * 10**cnt
            cnt += 1
        if NUM!=0:
            if NUM%2019==0:
                ans+=1
print(ans)
