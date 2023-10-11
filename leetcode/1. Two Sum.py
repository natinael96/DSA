class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        out = []
        for i in range(len(nums)):
            other = target - nums[i]
            if other in nums[i+1:]:
                j = nums.index(other, i+1)
                if i != j:
                    out.append(i)
                    out.append(j)
                    return out
        return out