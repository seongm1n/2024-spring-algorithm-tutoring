a , b = map(int, input().split())
s = 0
while (b>=a):
    if b <= a:
        break
    elif b % 10 == 1:
        b = (b - 1) // 10
        s += 1
    elif b % 2 == 0:
        b = b // 2
        s += 1
if a == b:
    print(s+1)
else:
    print(-1)
