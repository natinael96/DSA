def knapsack1(val, wt, W, n):
    dp = [0] * (W + 1)
    dp[0] = 0
    
    print("       ", end="")
    for i in range(1, W + 1):
        print(f"{i:7}", end="")
    print("\n" + "-" * (8 * W + 8))
    
    for w in range(1, W + 1):
        for i in range(n):
            if wt[i] <= w:
                dp[w] = max(dp[w - wt[i]] + val[i], dp[w])
        
        print(f"{w:5} |", end="")
        for item in dp[1:]:
            print(f"{item:7}", end="")
        print()
    
    return dp[W]

def knapsack2(val, wt, W, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    print("       ", end="")
    for i in range(W + 1):
        print(f"{i:7}", end="")
    print("\n" + "-" * (8 * (W + 1) + 8))

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            else:
                if wt[i - 1] <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt[i - 1]] + val[i - 1])
                else:
                    dp[i][w] = dp[i - 1][w]

        print(f"{i:5} |", end="")
        for item in dp[i][1:]:
            print(f"{item:7}", end="")
        print()

    return dp[n][W]

values = [44, 21, 38, 11, 40, 37, 13]
weights = [4, 7, 5, 2, 7, 10, 3]
n = len(values)
W = 22

print("Unbound:")
print(knapsack1(values, weights, W, n))
print("\nBound:")
print(knapsack2(values, weights, W, n))
