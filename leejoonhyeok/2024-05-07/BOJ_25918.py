n = int(input())

string = str(input())

cnt, day = 0, 0

for i in string:
    if i == '(': cnt += 1
    else: cnt -= 1
    
    if abs(cnt) > day:
        day = abs(cnt)

if cnt == 0: print(day)
else: print(-1)
