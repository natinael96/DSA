for _ in range(int(input())):
    n = int(input())
    MOD = 10**9 + 7
    dp = [[0, 0] for _ in range(n)] # join , separate
    dp[0] = [1, 1]
    for i in range(1,n):
        dp[i][0] = (2 * dp[i - 1][0] + dp[i - 1][1]) % MOD
        dp[i][1] = (dp[i - 1][0] + 4 * dp[i - 1][1]) % MOD
    # print(dp)
    print(sum(dp[-1]) % MOD)