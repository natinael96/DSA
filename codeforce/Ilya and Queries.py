string = input().strip()
n = len(string)
m = int(input())

count = [0] * n

for i in range(1, n):
    count[i] = count[i - 1] + (string[i] == string[i-1])

res = []
for _ in range(m):
    l, r = map(int, input().split())
    res.append(count[r - 1] - count[l - 1])

print("\n".join(map(str, res)))
