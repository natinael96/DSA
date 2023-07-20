from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Initialize the search range for the minimized largest sum.
        left, right = max(nums), sum(nums)

        # Check if it is possible to split `nums` into `k` subarrays.
        if len(nums) < k:
            return -1

        # Helper function to check if it is possible to split `nums`
        # into `k` subarrays with the maximum sum not exceeding `mid`.
        def isPossible(mid):
            cur_sum = 0  # Variable to track the current sum of elements in a subarray.
            count_of_sub = 1  # Variable to count the number of subarrays.

            for num in nums:
                cur_sum += num

                # If the current sum exceeds `mid`, start a new subarray
                # and update the current sum to the current number.
                if cur_sum > mid:
                    count_of_sub += 1
                    cur_sum = num

            # Check if it is possible to split the array into `k` subarrays
            # with the maximum sum not exceeding `mid`.
            return count_of_sub <= k

        # Perform binary search to find the minimized largest sum.
        while left <= right:
            mid = left + (right - left) // 2

            if isPossible(mid):  # If it is possible, reduce the search range to the left half.
                right = mid - 1
            else:  # If it is not possible, increase the search range to the right half.
                left = mid + 1

        # At this point, `left` represents the minimized largest sum.
        return left
