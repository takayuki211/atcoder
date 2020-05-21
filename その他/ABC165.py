
# AtCoder Beginner Contest 165

#A
K = int(input())
A, B = map(int, input().split())
flag=0
for i in range(A,B+1):
  if i%K==0:
    print('OK')
    flag=1
    break
if flag==0:
	print('NG')

#B
X = int(input())
f=0
c=0
y=100
if y<X:
  while f==0:
    c+=1
    y = int(float(y)*1.01)
    if y>=X:
      f=1
  print(c)
else:
  print(0)

#D
A, B, N = map(int, input().split())
Ymax=0
if A*N < B:
  print(0)
elif N<B:
  Ymax = A*N // B
  print(Ymax)
else:
  x = B-1
  Ymax = A*x//B - A*(x//B)
  print(Ymax)
