for i in range(1,11):
    if i%2 == 0:
        continue
    print(i)

# #for else
msg = "It is Time"

for i in range(len(msg)):
    print(msg[i], end=' ')
#>>I t   i s   T i m e
#
for x in msg:
    print(x, end=' ')
#>>I t   i s   T i m e

for x in msg:
    if x.islower():
        print(x, end=' ')
#>>t i s i m e

msg = "It is Time"
for x in msg:
    if x.isupper():
        print(x, end=' ')
print()
#>>I T


for x in msg:
    if x.isalpha():
        print(x, end=' ')

#>> I t i s T i m e

tmp = 'AZ'
for x in tmp:
    print(ord(x))
#알파벳을 유니코드로

a= [1,2,3,4,5]
b = list(range(1,11))
c = a+b
#>>[1,2,3,4,5,6,7,8,9,10]

a = [1,2,3,4,5]
a.insert(3,7)
#>>[1,2,3,7,4,5]
#3번 인덱스자리에 7이 들어감

a=[1,2,3,4,5]
a.pop()
#[1,2,3,4]
#맨 뒤자리 빼기

a=[1,2,3,4,5]
a.pop(3)
#3번 인덱스를 뺌

a=[1,2,3,4,5]
a.remove(4)
#4라는 값을 지워라

a=[1,2,3,4,5]
print(a.index(5))
#>>4
#값5의 인덱스 출력


import random as r

a=[23,12,36,53,19]
r.shuffle(a)
#a를 섞어라

a.sort()
#오름차순 정렬

a.sort(reverse=True)
#내림차순 정렬

for x in enumerate(a):
    print(x, end=' ')
#인덱스 번호와 값을 함께 접근(0,23)
#>> (0,23) (1,12) (2,36) (3,53) (4,19)

#튜플값은 변경 불가
#리스트값은 변경 가능

b=(1,2,3,4,5)
#b[0]=7 하면 에러남
#
a=[23,12,36,53,19]
for x in enumerate(a):
    print(x[0], x[1])
# 0 23
# 1 12
# 2 36
# 3 53
# 4 19

#####많이 쓰임
a=[23,12,36,53,19]
for index, value in enumerate(a):
    print(index, value)
print()

#all
a=[23,12,36,53,19]
if all(60>x for x in a):
    print("yes")
else:
    print("no")
#접근한 리스트 값이 모두!! 60미만이면 yes

#any
if any(15>x for x in a):
    print("YES")
else:
    print("no")
#조건을 돌면서 한번이라도 참이 있으면 참
#모두다 거짓이면 거짓

#1차원 리스트 초기화
a=[0]*3
#>>[0,0,0]

#2차원 리스트
a=[[0]*3 for _ in range(3)]
print(a)
#>>[[0,0,0],[0,0,0],[0,0,0]]

#표처럼 출력하기
for x in a:
    print(x)

#[0, 0, 0]
#[0, 0, 0]
#[0, 0, 0]

