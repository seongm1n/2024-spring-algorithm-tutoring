from collections import deque

play = int(input())
queue = deque(i for i in range(1,play+1))

while(len(queue) != 1):
    queue.popleft()
    goback = queue.popleft()
    queue.append(goback)

print(queue[-1])
