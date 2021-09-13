#k번째 수
import sys
sys.stdin = open("input.txt", "rt")

T = int(input())

for t in range(T):
    n,s,e,k = map(int, input().split())
    a = list(map(int, input().split()))
    b=a[s-1:e] #원본은 영향받지 않음
    b.sort()
    print("#%d %d" %(t+1,b[k-1]))








