arr = [int(input()) for i in range(9)]
total = sum(arr)
e = total - 100
rm = []

for i in range(9):
    for j in range(i + 1,9):
            if arr[i] + arr[j] == e:
                rm = [arr[i], arr[j]]
                break
arr.remove(rm[0])
arr.remove(rm[1])

arr.sort()
print(arr)
