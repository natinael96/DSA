class Solution:
    def maxSumRangeQuery(self, nums: list[int], requests: list[list[int]]) -> int:
        mod =10**9 + 7
        freq = [0] * len(nums)

        # freq of requests
        for start, end in requests:
            freq[start] += 1
            if end + 1 < len(freq):
                freq[end + 1] -= 1

        # prefix sum of freq
        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]

        nums.sort(reverse=True)
        freq.sort(reverse=True)

        max_sum = 0
        for i in range(len(nums)):
            max_sum += nums[i] * freq[i]
            max_sum %= mod
