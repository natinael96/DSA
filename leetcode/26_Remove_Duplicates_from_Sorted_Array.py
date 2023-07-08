class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        new_nums = []

        for i in nums:
            if i not in new_nums:
                new_nums.append(i)
        nums[:len(new_nums)] = new_nums
        nums[len(new_nums):] = ["_"]*(len(nums)-len(new_nums))

        return len(new_nums)

