n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 0

for i in range(2, n + 1):
    ans = float('inf')
    for x in range(1, k + 1):
        if x < i:
            ans = min(ans, abs(arr[i] - arr[i - x]) + dp[i - x])
    dp[i] = ans

print(dp[n])
