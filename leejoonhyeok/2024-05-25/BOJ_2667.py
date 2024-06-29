from collections import deque

n = int(input())
cnt = 0
arr = []
queue = deque()
result = []

for i in range(n):
    arr.append(list(map(int,input())))

directions = [(-1,0), (0,1), (1,0), (0,-1)]

for i in range(n):
    for j in range(n):
        if(arr[i][j] == 1):
            cnt = 0
            queue.append((i,j))
            while(queue):
                cury, curx = queue.popleft()
                cnt += 1
                arr[cury][curx] = 0
                for dy, dx in directions:
                    ny, nx = cury+dy, curx+dx
                    if(0 <= nx < n and 0 <= ny < n and arr[ny][nx] == 1):
                        queue.append((ny,nx))
                        arr[ny][nx] = 0
            result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)
