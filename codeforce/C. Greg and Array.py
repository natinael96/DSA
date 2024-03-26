n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr1 = [0] * (n + 1)
ops = []

for _ in range(m):
    l, r, d = map(int, input().split())
    ops.append([l, r, d])

qr = [0] * (m + 1)

for _ in range(k):
    x, y = map(int, input().split())
    qr[x - 1] += 1
    qr[y] -= 1

for i in range(1, m):
    qr[i] += qr[i - 1]

for i in range(m):
    ops[i][2] *= qr[i]

for i in range(m):
    l, r, d = ops[i]
    arr1[l - 1] += d
    arr1[r] -= d

for i in range(1, n + 1):
    arr1[i] += arr1[i - 1]

for i in range(n):
    arr[i] += arr1[i]

print(*arr[:n])
