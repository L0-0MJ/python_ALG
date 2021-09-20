#점수계산하기
# import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
ox = list(map(int, input().split()))

score = [0]*n
cnt=0
for index,i in enumerate(ox):
    if i == 1:
        cnt+=1
        score[index]=cnt
    else:
        cnt=0
        score[index]=cnt

print(sum(score))


#다른풀이
# n = int(input())
# a=list(map(int, input().split()))
# sum = 0
# cnt = 0
# for x in a:
#     if x == 1:
#         cnt+=1
#         sum+=cnt
#     else:
#         cnt=0
#