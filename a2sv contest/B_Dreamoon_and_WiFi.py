s1 = input()
s2 = input()

n = len(s2)
target = sum(1 if x == '+' else -1 for x in s1)

dp = [[0] * (2*n+1) for _ in range(n+1)]
dp[0][n] = 1  

if s2[0] == '+' or s2[0] == '?':
    dp[1][n+1] += dp[0][n]
if s2[0] == '-' or s2[0] == '?':
    dp[1][n-1] += dp[0][n]

for i in range(1, n):  
    for j in range(1, 2*n+1):  
        if dp[i][j]:
            if s2[i] == '+' or s2[i] == '?':
                dp[i+1][j+1] += dp[i][j]
            if s2[i] == '-' or s2[i] == '?':
                dp[i+1][j-1] += dp[i][j]
#for i in dp:
#    print(i)
print(dp[n][n + target] / sum(dp[n]))