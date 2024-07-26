n = int(input())
arr = list(map(int, input().split()))   

dp = [1]*(n+1)
health = [0]*(n+1)
for i in range(1, n+1):
    if health[i-1] + arr[i-1] >= 0: # drink 
        dp[i] = max(dp[i], 1 + dp[i-1])
        health[i] = health[i-1] + arr[i-1]
    else:
        health[i] = health[i-1]
        dp[i] = dp[i-1] 

print(dp[-1])


# n = int(input())
# nums = list(map(int, input().split()))   
# dp = [1] * len(nums)

# for i in range(len(nums)):
#     for j in range(i):
#         if nums[i] + nums[j] >= 0:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
# print(max(dp)) 