n = 1000-int(input())

changes = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in changes:
    if(n >= i):
        cnt += (n // i)
        n %= i
        
print(cnt)
