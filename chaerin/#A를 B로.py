#A -> B
A, B = map(int, input('정수 A, B를 입력하세요. : ').split())

while A != B:
  if A < B:
   if (B - A) % 2 == 0:
     count = (B - A) // 2
   else:
     count = (B - A) // 2 + 1
  else:
    break

if A == B:
  print(count+1)
else:
  print(-1)