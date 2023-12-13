n = int(input())

dp = [[0]*3 for _ in range(n+1)]

for i in range(n):
    row = list(map(int, input().split()))
    
    dp[i+1][0] = max(dp[i][1] + row[0], dp[i][2] + row[0])
    dp[i+1][1] = max(dp[i][0] + row[1], dp[i][2] + row[1])
    dp[i+1][2] = max(dp[i][0] + row[2], dp[i][1] + row[2])
    
ans = max(dp[n][0], dp[n][1],dp[n][2])
print(ans)

"""
n = int(input())

dp = [[0] * 3 for _ in range(n + 1)]

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(3):
        dp[i + 1][j] = max(dp[i][(j + 1) % 3], dp[i][(j + 2) % 3]) + row[j]

ans = max(dp[n][0], dp[n][1], dp[n][2])
print(ans)

"""