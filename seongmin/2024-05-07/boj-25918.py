n = map(int, input())
s = input()

stack = []
ans = 0
for i in s:
    if i == '(':
        if stack == []:
            stack.append(i)
            ans = max(ans, len(stack))
        elif stack[-1] == ')':
            stack.pop()
        else:
            stack.append(i)
            ans = max(ans, len(stack))
    else:
        if stack == []:
            stack.append(i)
            ans = max(ans, len(stack))
        elif stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)
            ans = max(ans, len(stack))

if stack == []:
    print(ans)
else:
    print(-1)