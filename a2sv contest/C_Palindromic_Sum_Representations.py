# for _ in range(int(input())):
#     n = int(input())
#     dp = [0] * (n + 1)
#     dp[0] = 1
    
#     for i in range(1, n + 1):
#         for j in range(i, n + 1):
#             dp[j] += dp[j - i]
            
#     print((dp[-1]))
    



for _ in range(int(input())):
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    
    pal = set()
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            pal.add(i)
    
    pals = sorted(p for p in pal if p <= n)
    for p in pals:
        for i in range(p, n + 1):
            dp[i] += dp[i - p]
    # print(dp)
    print(dp[-1] % (10 ** 9 + 7))