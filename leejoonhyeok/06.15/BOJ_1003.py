play = int(input())
for j in range(play):
    fibo = []
    arr = [1,1]
    N = int(input())
    
    try:
        for i in range(N):
            fibo.append(arr[0])
            asi = arr[0]
            arr[0] = arr[1]
            arr[1] += asi
        
        print(fibo[-2], fibo[-1])
    except:
        if(N == 0):
            print(1, 0)
        elif(N == 1):
            print(0, 1)
