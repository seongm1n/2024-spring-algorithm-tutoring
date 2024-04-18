f, s = map(int, input().split())
h = list(map(int, input().split()))

for i in range(f):
    for j in h:
        if j <= s:
            s += 1
            h.remove(j)
print(s)
