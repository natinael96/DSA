n, targ = map(int, input().split())
mod = 10**9 + 7
coins = list(map(int, input().split()))

dp = [0] * (targ+1)

dp[0] = 1

for i in range(targ+1):
    for coin in coins:
        if i >= coin:
            dp[i] = (dp[i] + dp[i - coin]) % mod
            
print(dp[targ])

