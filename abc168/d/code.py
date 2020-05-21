
import itertools
N, M = map(int, input().split())

if N > M+1:
    print('No')
else:
    L = []

    for i in range(M):
        A, B = map(int, input().split())
        L.append([A,B])

    key = 1
    D = [-1]*N
    D[0] = 'Yes'

    def rec(L,D,key):
        print('key=',key)
        # keyが含まれる部分を抽出する
        LL = [ item for item in L if key in item]
        # 終了条件
        if len(LL) == 0:
            return

        # Lからkeyが含まれる辺を削除
        for index, item in enumerate(L):
            if item in LL:
                del L[index]

        # keyから接続されたノードリストを得る
        cn = [i for i in list(itertools.chain.from_iterable(LL)) if i!=key]
        print('cn:',cn)

        ## keyから接続されたノードについてkeyの方を指すようにする
        for item in cn:
            if D[item-1] == -1:
                D[item-1] = key
        print('D=',D)

        for item in cn:
            rec(L,D,item)

    rec(L,D,key)

    if -1 in D:
        D[0] = 'No'
    else:
        D[0] = 'Yes'

    for item in D:
        print(item)
