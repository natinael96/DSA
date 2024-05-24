n = int(input())
dp = [[0]*3 for _ in range(n + 1)]

for i in range(1, n + 1):
    rw = list(map(int, input().split()))
    # print(rw)
    dp[i][0] = rw[0] + max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = rw[1] + max(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = rw[2] + max(dp[i - 1][0], dp[i - 1][1])

print(max(dp[-1]))
