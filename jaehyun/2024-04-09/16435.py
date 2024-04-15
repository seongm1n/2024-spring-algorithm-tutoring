# 과일의 개수, 스네이크버드 초기 길이
fruit_num, snake_length = map(int, input().split())
# 과일 높이
height = list(map(int, input().split()))
height.sort()

for i in range(len(height)):
    if snake_length >= height[i]:
        snake_length += 1
    else:
        break
    
print(snake_length)
