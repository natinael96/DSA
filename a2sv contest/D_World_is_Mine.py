
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [0] * (n)
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)
    print(max(dp))
    