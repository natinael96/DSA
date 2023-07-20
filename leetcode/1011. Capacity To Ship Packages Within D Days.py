class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low , high = max(weights), sum(weights)
        def ispossible(mid):
            day = 1
            cur = 0
            for i in weights:
                if cur + i > mid: 
                    day += 1
                    cur = i
                cur += i
            return day <= days
        
        while low < high:
            mid = low + (high - low)
            if ispossible(mid):
                high = mid
            else:
                low = mid + 1
        return low 