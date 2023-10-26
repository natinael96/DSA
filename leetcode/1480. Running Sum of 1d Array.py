class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runninSum = nums[0]
        for i in range(1,len(nums)):
            runninSum.append(runninSum[i-1] + nums[i])
        return runninSum