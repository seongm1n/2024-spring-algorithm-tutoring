#거스름돈
thing = int(input('물건의 가격을 입력하세요. : '))
change = 1000 - thing

change_500 = change // 500
change_100 = (change % 500) // 100
change_50 = (change % 100) // 50
change_10 = (change % 50) // 10
change_5 = (change % 10) // 5
change_1 = change % 5

print('잔돈의 개수 :', change_500 + change_100 + change_50 + change_10 + change_5 + change_1)