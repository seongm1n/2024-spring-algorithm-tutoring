from heapq import heappop, heappush

N = int(input())

heap = []
number = [int(input()) for i in range(N)] # number라는 리스트에 N 갯수만큼 값 입력.

for num in number:
    if num == 0: # number의 인덱스 중 하나가 0일 때
        if heap: # heap 리스트에 힙이 비어있는지 안 비어있는지
            print(-heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, -num)

  #시간초과때문에 계속 실패..ㅠㅠㅠ
