#https://www.acmicpc.net/problem/2309

array = []
for i in range(9):
    array.append(int(input()))
    
array.sort()

_sum = sum(array)

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if _sum - array[i] - array[j] == 100:
            for k in range(len(array)):
                if k == i or k ==j:
                    pass
                else:
                    print(array[k])
            exit()
