#정다면체

import sys
sys.stdin = open("input.txt","rt")
n,m = map(int, input().split())
cnt = [0]*(n+m)

for i in range(1,n+1):
    for j in range(1,m+1):
        k=i+j
        cnt[k]+=1

