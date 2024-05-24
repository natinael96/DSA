n, w = map(int, input().split())
arr = []
wei = []
for i in range(n):
    rw = list(map(int, input().split()))
    wei.append(rw[0])
    arr.append(rw[1])

dp = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, w + 1):
        if wei[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wei[i - 1]] + arr[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])
