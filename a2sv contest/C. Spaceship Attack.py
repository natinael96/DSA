s, b = map(int, input().split())

arr = list(map(int, input().split()))

qrs = []
for _ in range(b):
    d, g = map(int, input().split())
    qrs.append([d, g])

qrs.sort(key=lambda x: x[0])

for j in range(1, b):
    qrs[j][1] += qrs[j - 1][1]

ans = [0]*s
for i in range(s):
    l, r = 0, b - 1
    while l < r:
        mid = (l + r) // 2
        if qrs[mid][0] > arr[i]:
            r = mid
        else:
            l = mid + 1
    if r == 0:
        ans[i] = qrs[0][1] if qrs[0][0] <= arr[i] else 0
    else:
        ans[i] = qrs[r - 1][1]
print(*ans)