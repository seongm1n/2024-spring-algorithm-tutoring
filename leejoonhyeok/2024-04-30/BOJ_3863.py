#시간초과 해결을 못했습니다.

import sys

while(1):
    N, M = map(int,sys.stdin.readline().split())
    if(N == 0 and M == 0):
        break
    call = []
    
    for i in range(N):
        sou, des, start, duration = map(int,sys.stdin.readline().split())
        call.append([start,start+duration])
    
    for ch in range(M):
        dochung = list(map(int,input().split()))
        cnt = 0
        
        for i in range(len(call)):
            for j in [t for t in range(dochung[0]+1, dochung[0]+dochung[1]+1)]:
                if(j in [i for i in range(call[i][0]+1, call[i][1]+1)]):
                    cnt += 1
                    break
        sys.stdout.write(str(cnt)+"\n")
