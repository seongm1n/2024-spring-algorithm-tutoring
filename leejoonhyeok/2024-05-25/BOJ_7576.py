import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

arr = []
queue = deque()
directinos = [(-1,0), (0,1), (1,0), (0,-1)]
answer = 0

for i in range(M):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(M):
    for j in range(N):
        if(arr[i][j] == 1):
            queue.append((i,j))

while(queue):
    cury, curx = queue.popleft()
    for dy, dx in directinos:
        ny, nx = cury + dy, curx + dx
        if(0 <= nx < N and 0 <= ny < M and arr[ny][nx] == 0):
            arr[ny][nx] = arr[cury][curx] + 1
            queue.append((ny,nx))

for i in range(M):
    for j in range(N):
        if(arr[i][j] == 0):
            print(-1)
            exit(0)
        answer = max(answer, arr[i][j])

print(answer-1)
