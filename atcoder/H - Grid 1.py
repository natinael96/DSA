MOD = 10**9 + 7

rw, col = map(int, input().split())
grid = [input().strip() for _ in range(rw)]

dp = [[0] * (col + 1) for _ in range(rw + 1)]
dp[0][0] = 1

for i in range(rw):
    for j in range(col):
        if grid[i][j] == '.':
            if i > 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
        else:
            dp[i][j] = 0

print(dp[rw-1][col-1])