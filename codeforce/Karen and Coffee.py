n, k, q = map(int, input().split())

recipes = [0] * (200000 + 2)
result = []

for i in range(n):
    li, ri = map(int, input().split())
    recipes[li] += 1
    recipes[ri + 1] -= 1

count = 0
for i in range(1, len(recipes)):
    count += recipes[i]
    recipes[i] = 1 if count >= k else 0

for i in range(1, len(recipes)):
    recipes[i] += recipes[i - 1]

for i in range(q):
    a, b = map(int, input().split())
    result.append(recipes[b] - recipes[a-1])

print("/".join(map(str,result)))