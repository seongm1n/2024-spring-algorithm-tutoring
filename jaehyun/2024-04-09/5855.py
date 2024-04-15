stuff = int(input()) # 물건 가격
money = 1000 
changes = [500, 100, 50, 10, 5, 1]
change_money = money - stuff # 거스름돈
save = 0 # 잔돈 갯수

for i in changes:
    if change_money >= i:
        save += change_money // i
        change_money %= i 

print(save)
