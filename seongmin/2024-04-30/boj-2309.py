dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))
dwarfs.sort()

for i in range(9):
    for j in range(i + 1, 9):
        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
            ans = [i, j]

for i in range(9):
    if i == ans[0] or i == ans[1]:
        continue
    print(dwarfs[i])