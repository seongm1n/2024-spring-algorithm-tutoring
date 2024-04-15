n = 1000 - int(input())
c = [500, 100, 50, 10, 5, 1]
a = 0

for i in c:
    a += n // i
    n %= i

print(a)