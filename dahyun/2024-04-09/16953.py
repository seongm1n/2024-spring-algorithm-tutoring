a, b = map(int, input().split())
c = 1

while 1:
    if a == b:
        break
    elif (b % 2 != 0 and b % 10 != 1) or b<a:
        c = -1
        break
    else:
        if b % 10 == 1:
            b = b // 10
            c += 1
        else:
            b = b // 2
            c += 1
    
print(c)