from collections import deque

n = int(input())
q = deque([i for i in range(1, n + 1)])

answer = q.popleft()
while q:
    q.append(q.popleft())
    answer = q.popleft()
print(answer)