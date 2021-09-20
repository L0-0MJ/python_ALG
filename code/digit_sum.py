#자릿수의 합

import sys
sys.stdin = open("input.txt","rt")

n = int(input())
num = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x>0:
        sum += x%10
        x = x//10
    return sum
max = -1
for x in num:
    tot=digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)


