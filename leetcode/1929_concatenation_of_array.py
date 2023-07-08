class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        listlen = len(nums)
        ans = [0] * 2 * listlen
        for i in range(listlen):
            ans[i] = ans[i + listlen] = nums[i]
        return ans


