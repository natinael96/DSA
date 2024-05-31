


t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    dp = [0] * (n + 1)  
    open = 0  

    for i in range(1, n + 1):
        if s[i - 1] == '(':
            open += 1
        else:
            open -= 1
            if open > 0:
                dp[i] = dp[i - 1] + 1

    print(sum(dp))