arr=[]

for i in range(9):
    arr.append(int(input()))

sum = sum(arr)
arr.sort()

for i in range(9):
    for j in range(i+1,9):
        if sum - (arr[i]+arr[j]) == 100:
            a = arr[i]
            b = arr[j]

arr.remove(a)
arr.remove(b)

for i in arr:
    print(i)
