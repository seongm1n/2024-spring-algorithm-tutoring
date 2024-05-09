from collections import deque

N = int(input())
n1 = []

# n1 배열에 값 추가
for i in range(1, N + 1, 1):
    n1.append(i)

n1 = deque(n1)

# n1.popleft()
# print(n1)

while True:
    if len(n1) == 1:
        print(n1[0])
        break
    # 0번째 인덱스 지우기
    n1.popleft()
    # print(n1)
  
    # 0번째 인덱스 추가하고 0번째 인덱스 지우기
    n1.append(n1[0])
    n1.popleft()
    # print(n1)

