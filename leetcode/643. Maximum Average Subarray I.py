class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        windowSum = sum(nums[:k])
        maxAve = windowSum/k
        for i in range(k,len(nums)):
            windowSum += nums[i] - nums[i - k]
            currAve = windowSum/k
            maxAve = currAve if currAve >= maxAve else maxAve
        
        return maxAve
