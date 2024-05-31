n = int(input())
arr = list(map(int, input().split()))

mx = 1
l = 0

for r in range(1, n):
    if arr[r] > arr[r - 1]:
        cur = r - l + 1
        mx = max(mx, cur)
    else:
        l = r
print(mx)