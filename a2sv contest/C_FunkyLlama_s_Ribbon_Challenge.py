n, a, b, c = map(int, input().split())

dp = [-1] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    if i - a >= 0 and dp[i - a] > -1:
        dp[i] = max(dp[i], dp[i - a] + 1)
    if i - b >= 0 and dp[i - b] > -1:
        dp[i] = max(dp[i], dp[i - b] + 1)
    if i - c >= 0 and dp[i - c] > -1:
        dp[i] = max(dp[i], dp[i - c] + 1)
print(dp)
print(dp[-1])

