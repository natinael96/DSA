def findmaxlen(nums,k):
    counDict = {1:0,0:0}
    l = 0
    maxLen = 0
    for r in range(len(nums)):
        char = nums[r]
        counDict[char] += 1
        
        winSize = r - l + 1
        
        if counDict[0] <= k: 
            maxLen = max(maxLen, winSize)
        else:
            counDict[nums[l]] -= 1
            l += 1
    return maxLen

print(findmaxlen([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))