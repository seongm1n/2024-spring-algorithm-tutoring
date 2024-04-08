money = 1000 - int(input())
changes = [500, 100, 50, 10, 5, 1]
result = 0
while money:
    for change in changes:
        if change <= money:
            money -= change
            result += 1
            break
print(result)