#K번째 큰 수
import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set() #중복을 방지하는 구조, 집합자료형
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m])
#값 한 개 추가 .add
#여러 개 한번에 추가 .update
res = list(res)
res.sort(reverse=True)
print(res[k-1])



