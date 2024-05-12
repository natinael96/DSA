for _ in range(int(input())):
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    dp = [0] * (n + 1)    
    for i in range(n, 0, -1):
        if i + arr[i - 1] <= n:
            dp[i] = arr[i - 1] + dp[i + arr[i - 1]]
        else:
            dp[i] = arr[i - 1]
    #print(dp)
    print(max(dp[1:]))
