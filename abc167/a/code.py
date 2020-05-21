import numpy as np
import math

S = input()
T = input()
# import re
# TT = re.sub('.$','',T)
# if TT == S:
#     print('Yes')
# else:
#     print('No')

if S == T[:-1]:
    print('Yes')
else:
    print('No')
