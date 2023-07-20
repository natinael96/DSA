class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1: return 0

        low, high = 0, n - 1

        while low < high:
            mid = low + (high - low) // 2
            if 0 < mid < n - 1:
                if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid - 1] > nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if mid == 0:
                    if nums[0] > nums[1]: return 0
                    else: return 1
                if mid == n-1:
                    if nums[n-1] > nums[n-2]:
                        return n-1
                    else:
                        return n-2 
                
        return low