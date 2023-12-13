n = int(input())
heights = list(map(int, input().split()))

dp = [0] * n
dp[0] = 0
dp[1] = abs(heights[1] - heights[0])

for i in range(2, n):
    dp[i] = min(dp[i-1] + abs(heights[i] - heights[i-1]),
               dp[i-2] + abs(heights[i] - heights[i-2]))

print(dp[-1])
