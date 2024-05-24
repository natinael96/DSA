n, w = map(int, input().split())
wei = []
val = []
for _ in range(n):
    rw = list(map(int, input().split()))
    wei.append(rw[0])
    val.append(rw[1])

mx = 10**5
dp =[float('inf')] * (mx + 1)
dp[0] = 0

for i in range(n):
    for j in range(mx, val[i] - 1, -1):
        dp[j] = min(dp[j], dp[j - val[i]] + wei[i])
# print(dp)
for i in range(mx, -1, -1):
    if dp[i] <= w:
        print(i)
        break