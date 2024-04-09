#method 1. 2를 곱한다.
#method 2. 1의 수의 가장 오른쪽에 추가한다.

from collections import deque

def me2(pl):
    return int(str(pl)+str(1))

queue = deque()
visited = []
A, B = 4,42
cnt = 0
queue.append(A)

while(len(queue) != 0):
    tmp = queue.popleft()
    if(tmp == B):
        break
    else:
        visited.append(tmp)
        queue.append(tmp*2)
        queue.append(me2(tmp))

calc = len(visited)

while(1):
    if(calc != 1):
        calc = calc//2
        cnt += 1
    else:
        break
print(cnt+1)

# 1. 만들 수 없는 경우를 구현하지 못함.
# 2. 시간복잡도에서 걸릴거 같음.
