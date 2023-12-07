# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = float('inf')


        l, r = 1, n
        
        while l <= r:
            mid = l + (r- l)//2
            
            if isBadVersion(mid):
                first = min(first, mid)
                r = mid - 1
            else:
                l = mid + 1
        return first