N, M = map(int,input().split())
arr = list(map(int,input().split()))
left = 0
right = 0

for i in arr:
    if left < i:
        left = i
    right += i
#시작 left 는 9, right = 45
#할당된 크기에서 left를 늘려서 찾거나,
#right를 줄여서 최소한의 값이 나오는 때를 찾는다.


while(left <= right):
    mid = (left + right) // 2
    cnt = 0                             #끊는점
    temp = 0                            #시간 합

    for i in range(N):
        if(temp + arr[i] > mid):
            cnt += 1
            temp = 0                    #0으로 재설정 해주지 않으면 다시 계산할 때 수가 넘친다.
        temp += arr[i]
    
    if(temp != 0):
        cnt += 1

    if(cnt > M):                        #cnt가 M값을 넘긴다는 것은 현재 나눈 개수로는 모든 영상 저장 불가
        left = mid + 1                  #left 값을 늘려서 최소값 증가
    else:
        right = mid - 1                   #cnt가 더 작다면 더 작게 구할 수도 있으니 right값을 축소

print(left)                             #left가 right보다 크다면 종료해서 나온 left(최소 크기)
