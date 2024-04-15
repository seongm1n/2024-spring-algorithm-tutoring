A, B = map(int, input().split())
save = 0

while A != B:
    if B % 2 != 0:
        B = (B - 1) / 10
        save += 1
        if B < A:
            print("-1")
            exit()
    else:
        B = B / 2
        save += 1

print(save + 1)
