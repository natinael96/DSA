def distinctSub(nums, k):
    n = len(nums)
    ans = [0]*(n - k + 1)
    
    for i in range(k-1, n):
        
        subArr = nums[i - k + 1 : i + 1]
        ans[i - k + 1] = len(set(subArr))
    return ans

a = distinctSub(nums = [1,1,1,1,2,3,4], k = 4)
print(a)