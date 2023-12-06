class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newNums = sorted(nums1 + nums2)
        median = 0
        if len(newNums) % 2 == 1:
            mid = (len(newNums) - 1)//2
            median = newNums[mid]
        else:
            mid1 = len(newNums)/2
            mid2 = mid1 - 1
            median = (newNums[mid1] + newNums[mid2]) / 2
        return median