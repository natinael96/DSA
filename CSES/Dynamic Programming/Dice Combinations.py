n = int(input())
mod = 10**9 + 7
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    for x in range(1, 7):
        if i - x >= 0:
            dp[i] = (dp[i] + dp[i - x]) % mod

print(dp[n])


"""dp = [1]
for i in range(int(input())):
	dp.append(sum(dp[-6:]) % 1000000007)
print(dp[-1])"""