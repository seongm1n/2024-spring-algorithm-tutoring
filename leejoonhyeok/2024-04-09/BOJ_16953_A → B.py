#def me2(pl):
#    return int(str(pl)+str(1))
# 1을 추가하기 위해 만들었으나 B를 줄여가는게 훨씬 효율적임.
    
A, B = map(int,input().split())
play = 0

while(A != B):
    tmp = B
    play += 1
    if((B%10) == 1):
        B //= 10
    elif((B%2)==0):
        B //= 2
        
    if(B == tmp):
        play = -2
        break
        
print(play+1)
