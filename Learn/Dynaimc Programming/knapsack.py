def knapsack1(val, wt, W, n):
    dp = [0] * (W+1)
    dp[0] = 0
    for w in range(1, W+1):
        for i in range(n):
            if wt[i] <= w:
                dp[w] = max(dp[w - wt[i]] + val[i], dp[w])
            
    return dp[W]

def knapsack2(val, wt, W, n):
    
    dp = [[0]*(W+1) for _ in range(n+1)]
    
    for  i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w] = 0
            else:
                if wt[i-1] <= w:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w - wt[i -1]] + val[i-1])
                else:
                    dp[i][w] = dp[i - 1][w]
    return dp[n][W]
                    
values = [30, 14, 16, 9]
weights = [6, 3, 4, 2]
n = len(values)
W = 10

print("Unbound: ",knapsack1(values, weights, W, n))
print(">>Bound: ",knapsack2(values, weights, W, n))