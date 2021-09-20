a, b = map(int, input("숫자를 입력하세요:").split())

# 1씩 작아지기
for i in range(10, 0, -1):
    print(i)
#>>10 9 8 7 6 5 4 3 2 1

# 2씩 작아지기
for i in range(10,0,-2):
    print(i)
#>>10 8 6 4 2

#무한반복 멈추기기
i = 1
while True:
    print(i)
    if i == 10:
        break
    i+=1

#짝수면 출력안하고 반복문으로 돌아감
for i in range(1, 11):
    if i%2==0:
        continue
    print(i)


#for-else문
#for문이 정상적으로 종료되면 else문 출력
#for문이 중간에break당하면 else출력 X
for i in range(1,11):
    print(i)
    if i>15:
        break
else:
    print(11)
#>>1 2 3 4 5 6 7 8 9 10 11

#대문자 만들기,원본이 바뀌는 건 아님
msg = "It is Time"
print(msg.upper())

#소문자 만들기
print(msg.lower())

#대문자화 된 변수 설정
tmp = msg.upper()

#T라는 문자를 찾아서 인덱스 번호 출력
print(tmp.find('T'))
#>>1

#tmp문자열의 T갯수 출력
print(tmp.count('T'))
#>>2

#슬라이스
print(msg[:2]) #0~1까지 부분문자 뽑아냄 =>It
print(msg[3:5]) #3~4까지 뽑아냄=>is

#공백포함 문자길이
print(len(msg))#10

#문자 하나하나 접근하기
for i in range(len(msg)):
    print(msg[i], end=' ') #I t  i s  T i m e
#문자 하나하나 접급 2
for x in msg:
    print(x, end=' ')
print() #I t  i s  T i m e

#대문자만 뽑아서 출력
for x in msg:
    if x.isupper():
        print(x, end=' ')

#소문자만 뽑아서 출력
for x in msg:
    if x.islower():
        print(x, end=' ')
print()

#알파벳일때만 참
for x in msg:
    if x.isalpha():
        print(x, end='')
print()

tmp = 'AZ'
for x in tmp:
    print(ord(x))
    #97
    #122

tmp=65
print(chr(tmp))
#A


#7/25
#####5
#1부터 n까지 홀수 출력
n=int(input())
for i in range(1,n+1):
    if i%2==1:
        print(i)

#1부터 N까지 합
sum = 0
for i in range(1,n+1):
    sum+=i
print(i)

#N의 약수
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=' ')

#리스트와 내장함수

a=[]
#는 아래와 같이 표현가능
b=list()

a=[1,2,3,4,5]
b=list(range(1,11))
c=a+b
#[1,2,3,4,5,6,7,8,9,10]

a.append(6)
#[1,2,3,4,5,6]

a=[1,2,3,4,5]
a.insert(3,7)
#[1,2,3,7,4,5,6]
#3번 인덱스에 7이 들어간다

a=[1,2,3,4,5]
a.pop()
#[1,2,3,4]
#맨 뒤자리를 뺀다

a=[1,2,3,4,5]
a.pop(3)
#[1,2,3,5]
#3번 인덱스를 뺀다

a=[1,2,3,4,5]
a.remove(4)
#[1,2,3,5]
#4라는 값을 지워라

a=[1,2,3,4,5]
print(a.index(5))
#>>4
#5라는 값의 인덱스 번호 출력

a=list(range(1,11))
sum(a)
#리스트 내 1~10까지 합

print(min(7,5))
#7과 5중에서 최솟값 =>5

print(min(7,3,5))
#7,3,5중에서 최솟값 =>3

import random as r

a=list(range(1,11))
#[1,2,3,4,5,6,7,8,9,10]
r.shuffle(a) #a를 섞어라
#[10,6,3,4,1,8,5,9,2,7]
#게임만들 때 많이 사용

a.sort()
#[1,2,3,4,5,6,7,8,9,10]
#오름차순으로 정렬됨

a.sort(reverse=True)
#[10,9,8,7,6,5,4,3,2,1]
#내림차순으로 정렬

a.clear()
#[]
#리스트에 있는 값을 비워줌

a=[23,12,36,53,19]
print(a[:3])
#인덱스 0부터 2까지
#[23,12,36]

print(a[1:4])
#[12,36,53]

print(len(a))
#인덱스 길이
#5

#리스트 접근
a=[23,12,36,53,19]
for i in range(len(a)):
    print(a[i],end=' ')
#23 12 36 53 19

for x in a:
    print(x, end=' ')
#23 12 36 53 19

#인덱스 번호를 함께 출력
for x in enumerate(a):
    print(x, end=' ')
#인덱스 번호와 값을 함께 접근 (0,23)
#>> (0,23) (1, 12) (2,36) (3,53) (4,19)

#리스트와 튜플의 차이
#튜플값은 변경이 불가능 , 리스트는 가능
b=(1,2,3,4,5)
#b[0]=7 하면 에러남

a=[23,12,36,53,19]
for x in enumerate(a):
    print(x[0], x[1])
#>> 0 23 식으로 출력됨

#enumerate많이 쓰이는 접근법
a=[23,12,36,53,19]
for index, value in enumerate(a):
    print(index, value)
print()

#######all
#for 문을 통해 접근한 리스트 값이 모두 60미만이면 참을 리턴
#하나라도 조건에 안 맞으면 거짓
a=[23,12,36,53,19]
if all(60>x for x in a):
    print("yes")
else:
    print("no")

######any
#조건을 돌면서 한번이라도 참이 있으면 참을 리턴
#모두다 거짓이면 거짓
if any(15>x for x in a):
    print("YES")
else:
    print("NO")

#1차원 리스트 초기화
a=[0]*3
#[0,0,0]

#2차원리스트
a=[[0]*3 for _ in range(3)]
print(a)
#[[0,0,0],[0,0,0],[0,0,0]]

#표처럼 출력하기
for x in a:
    print(x)
# [0,0,0]
# [0,0,0]
# [0,0,0]

#리스트의 값들만 표처럼 출력
for x in a:
    for y in x:
        print(y, end=' ')
    print()
# 0 0 0
# 0 0 0
# 0 0 0

#최대값
item = [5, 13, 66, 12, 78, 1, 78]
max(item)
##78

#역순으로
num=789
int(str(num)[::-1])

##역순 2
x = int(input())
res = 0
while x>0:
    t = x%10
    res = res*10+t
    x = x//10
print(res)
