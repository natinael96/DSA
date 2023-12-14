arr = list(map(int, input().split()))
n = len(arr)

dp = [0]*(n+1)
dp[0] = 0
for i in range(n):
    dp[i+1] = max(arr[i], arr[i] + dp[i-1])
    
print(dp[-1])

# local_maximum at index i is the maximum of A[i] 
# and the sum of A[i] and local_maximum at index i-1.