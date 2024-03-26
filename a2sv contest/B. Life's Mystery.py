strng = input()
stack = []

for i in strng:
    if len(stack) == 0:
        stack.append(i)
    elif i == stack[-1]:
        stack.pop()
    else:
        stack.append(i)
print("".join(stack))
    