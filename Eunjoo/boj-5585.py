a = int(input())
b = 1000 - a
c = [500, 100, 50, 10, 5, 1]
d = 0

for i in c:
    d += b // i
    b %= i

print(d)
