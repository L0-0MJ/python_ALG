#최솟값

arr=[5,3,7,9,2,5,2,6]
arrMin = float('inf') #파이썬에서 가장 큰 값
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)

#2
arr=[5,3,7,9,2,5,2,6]
arrMin = arr[0]
for i in range(1, len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)