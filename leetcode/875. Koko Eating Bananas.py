from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
                
        l, r = 1, max(piles)
        res = r
        
        def isValid(speed):
            time = 0
            for n in piles:
                time += ceil(n/speed)
            return time <= h
        
        while l <= r:
            
            mid = l + (r - l)//2
            
            if isValid(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res 
    