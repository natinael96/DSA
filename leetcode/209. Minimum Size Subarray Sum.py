class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSubArray = float("inf")
        runninSum = 0
        
        l = 0
        for r in range(len(nums)):
            runninSum += nums[r]
            
            while runninSum >= target:
                minSubArray = min(minSubArray, r - l +1)
                runninSum -= nums[l]
                l += 1
        return minSubArray if minSubArray != float("inf") else 0