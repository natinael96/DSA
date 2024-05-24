n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 0

for i in range(2, n + 1):
    dp[i] = float('inf')
    for j in range(1, k + 1):
        if j < i:
            dp[i] = min(dp[i], abs(arr[i] - arr[i - j]) + dp[i - j])
    
print(dp[-1])

