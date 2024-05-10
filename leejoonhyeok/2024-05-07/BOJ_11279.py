from heapq import heappush, heappop
import sys

heap = []

N = int(sys.stdin.readline())

for i in range(N):
    ps = int(sys.stdin.readline())
    if(ps == 0):
        if(len(heap) == 0):
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (-ps,ps))