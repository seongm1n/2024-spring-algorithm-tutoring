h = []

for _ in range(9):
    h.append(int(input()))
h.sort()

tot = 0

for i in range(9):
    tot += h[i]

for i in range(9):
    for j in range(9):
        if tot - h[i] - h[j] == 100:
            a = h[i]
            b = h[j]

for i in h:
    if i == a or i == b:
        continue
    else:
        print(i)
