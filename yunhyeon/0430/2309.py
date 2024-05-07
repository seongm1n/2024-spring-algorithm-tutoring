#https://www.acmicpc.net/problem/2309

height = []
for i in range(9):
    height.append(int(input()))
    
height.sort()

_sum = sum(height)

for i in range(len(height)):
    for j in range(i + 1, len(height)):
        if _sum - height[i] - height[j] == 100:
            for k in range(len(height)):
                if k == i or k ==j:
                    pass
                else:
                    print(height[k])
            exit()
