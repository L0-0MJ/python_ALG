#주사위 게임
import sys
sys.stdin = open("input.txt","rt")

n = int(input())
res = 0
for i in range(n):
    dice = input().split()
    dice.sort()
    a,b,c, = map(int, dice)
    if a==b and b==c:
        money = 10000+a*1000
    elif a==b or a==c:
        money = 1000+a*100
    elif b==c:
        money = 1000+b*100
    else:
        money = c*100
    if money > res:
        res = money
print(res)