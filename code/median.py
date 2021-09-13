#대표값

import sys
sys.stdin = open("input.txt","rt")
subMin = float('inf')
n = int(input())
scoreList = list(map(int, input().split()))
avg = round(sum(scoreList)/n)

for idx, x in enumerate(scoreList):
    tmp = abs(x-avg)
    if tmp < subMin:
        subMin = tmp
        score = x
        res = idx+1
    elif tmp == subMin:
        if x > score:
            score = x
            res = idx+1
print(avg, res)


#round => round_half_even
#4.5를 반올림하면 4
#4,5는 똑같이 0.5차이가 나므로 이 경우 짝수인 4로 반올림
#5.5 -> 6 짝수로

#소수 첫째자리에서 무조건 반올림 하고 싶으면
a=66.5
a=a+0.5
a = int(a)



