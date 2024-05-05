tall_list = []

for i in range(9):
    tall_list.append(int(input()))

#tall_list = [20, 7, 23, 19, 10, 15, 25, 8, 13]

tall_list.sort()
tall_sum = 0

for tall in tall_list:
    tall_sum += int(tall)

#print(tall_sum)

for i in range(len(tall_list)):  # i 값 
    for j in range(i + 1, len(tall_list)): # j 값 -> i가 0이면 1 ~ 8 범위 /  max 범위 = i가 7일때 -> 8 ~ 8 범위
        if tall_sum - tall_list[i] - tall_list[j] == 100:   # tall_list의 i번째 인덱스와 j번째 인덱스를 100에서 뺌
            for k in range(len(tall_list)): # k = (0 ~ 8)
                if k == i or k == j: # k가 i 또는 j와 같아지면 건너뛰기
                    pass
                else: # i, j 제외한 값 출력
                    #print(tall_sum - tall_list[i] - tall_list[j])
                    print(tall_list[k])
            exit() #여러가지의 경우의 수가 있을 때 한가지의 경우의 수만 출력하기 위한 exit()
