n = int(input())
arr = list(map(int, input().split()))

card = sorted([(i, arr[i]) for i in range(n)], key=lambda x: x[1])
ans = []

while card:
    cur = []
    cur.append(card.pop(0)[0])
    cur.append(card.pop()[0])

    ans.append(cur)

for i in ans:
    print(i[0]+1, i[1]+1)
    

    