n = input().strip()

hello = "hello"
indx = 0

for i in n:
    if i == hello[indx]:
        indx += 1
        if indx == len(hello):
            print("YES")
            break

if indx < len(hello):
    print("NO")
