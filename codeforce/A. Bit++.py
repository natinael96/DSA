n= int(input())

num = 0
for i in range(n):
    op = input()
    if "++" in op:
        num += 1
    elif "--" in op:
        num -= 1
print(num)
    