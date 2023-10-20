class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        arr = nums
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return start
    
    