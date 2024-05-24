n = int(input())
hgt = list(map(int, input().split()))

dp = [0] * n
dp[0] = 0
dp[1] = abs(hgt[1] - hgt[0])

for i in range(2, n):
    dp[i] = min(dp[i-1] + abs(hgt[i] - hgt[i-1]),
               dp[i-2] + abs(hgt[i] - hgt[i-2]))

print(dp[-1])
