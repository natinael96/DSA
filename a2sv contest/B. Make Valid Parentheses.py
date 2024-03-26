par = input()

stack = []
cnt = 0
for i in par:
    if i == "(":
        stack.append(i)
    if stack:
        if stack[-1] == "(" and i == ")":
            stack.pop()
            cnt += 1
print(cnt*2)