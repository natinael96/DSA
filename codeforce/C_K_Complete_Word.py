for t in range(int(input())):
    
    n, k = map(int, input().split())
    
    s = [ord(char) - 97 for char in input()]
    
    half = (k+1)//2
    dp = [[0 for _ in range(26)] for _ in range(half)]
    for i in range(n):
        r = i % k
        r = min(r, k - 1 - r) # 
        dp[r][s[i]] += 1 

    noCng = 0
    for i in range(half):
        for j in range(26):
            if dp[i][j] > dp[i][0]:
                dp[i][0] = dp[i][j]
        noCng += dp[i][0]
    print(n-noCng)
