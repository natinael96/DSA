import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for l in range(int(math.sqrt(c)) + 1): 
            r = int(math.sqrt(c - l**2))
            if l**2 + r**2 == c:
                return True
        return False