#스네이크버드
N = int(input('과일의 개수를 입력하세요. : ')) #과일의 개수를 왜 입력해야 하는지 모르겠음
L = int(input('스네이크버드의 초기 길이를 입력하세요. : '))
height = list(map(int, input('과일들의 높이를 입력하세요. : ').split()))
height.sort()


for i in height:
  if L >= i:
    L += 1

print(L)