#함수

def add(a,b):
    c=a+b
    print(c)

add(3,2)
#>>5

def add2(a, b):
    c = a + b
    return c
print(add2(3,2))


def add3(a, b):
    c = a+b
    d = a-b
    return c, d #튜플로 리턴

print(add3(3,2))
#>>(5, 1)

#소수이면 참, 아니면 거짓
def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

a=[12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=' ')
#>>13 7 19

#람다함수
#익명의 함수, 표현식
def plus_one(x):
    return x+1
print(plus_one(1))

plus_two = lambda x: x+2
print(plus_two(1))


def plus_one(x):
    return x+1
print(plus_one(1))

a=[1,2,3]
print(list(map(plus_one, a)))

#map(함수, 자료명)

print(list(map(lambda x: x+1, a)))