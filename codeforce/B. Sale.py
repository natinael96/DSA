n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

s = 0
for i in range(m):
    if a[i] >= 0:
        break
    s += a[i]

print(-s)
