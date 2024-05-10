N = int(input())
S = input()
min_day = 0
cnt = 0
for char in S:
    if char == '(':
        cnt += 1
    else:
        cnt -= 1
    if abs(cnt) > min_day:
        min_day = abs(cnt)
if cnt == 0:
    print(min_day)
else:
    print(-1)
