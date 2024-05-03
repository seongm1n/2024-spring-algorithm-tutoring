import itertools

arr = []

for i in range(9):
    arr.append(int(input()))

ncr = list(itertools.combinations(arr,7))

for i in range(len(ncr)):
    if(sum(ncr[i]) == 100):
        result = list(ncr[i])
        
for i in (sorted(result)):
    print(i)