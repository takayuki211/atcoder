#!/usr/bin/env python3
import re
s = input()


while True:

    # re.subを使うと処理時間超過した。
    # s = re.sub('dream$|dreamer$|erase$|eraser$','',s)

    # リストのスライスを利用するほうが高速
    l = len(s)
    if s.rfind('dream') == l-5:
        s = s[:-5]
    elif s.rfind('dreamer') == l-7:
        s = s[:-7]
    elif s.rfind('erase') == l-5:
        s = s[:-5]
    elif s.rfind('eraser') == l-6:
        s = s[:-6]
    else:
        break

    # ※文字を逆にすれば先頭から操作できる。

if len(s)==0:
    print('YES')
else:
    print('NO')
