"""string = input().strip()
n = len(string)
m = int(input())

ans = [0]*m
for i in range(m):
    l, r = map(int, input().split())
    for j in range(l,r):
        if string[j] == ".":
            ans[i] += 1

print("/".join(map(str,ans)))"""

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
