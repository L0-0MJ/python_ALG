#k번째 약수
import sys
sys.stdin = open("input.txt", "rt")
#나
a= []
n, k = map(int, input().split())

for i in range(1,n+1):
    if n%i == 0:
        a.append(i)

try:
    if a[k-1]:
        print(a[k-1])
except:
    print(-1)


#풀이
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)

