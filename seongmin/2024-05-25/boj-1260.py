from collections import deque

def dfs(x):
    ans.append(x)
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 1:
            continue
        dfs(i)

def bfs(x):
    q = deque()
    q.appendleft(x)
    visited[x] = 1
    while q:
        x = q.pop()
        ans.append(x)
        for i in graph[x]:
            if visited[i] == 1:
                continue
            q.appendleft(i)
            visited[i] = 1

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n + 1):
    graph[i].sort()

visited = [0] * (n + 1)
ans = []
dfs(v)
for i in ans:
    print(i, end = " ")
print()

visited = [0] * (n + 1)
ans = []
bfs(v)
for i in ans:
    print(i, end = " ")