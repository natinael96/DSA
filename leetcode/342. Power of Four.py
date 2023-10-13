class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def powerFour(n):
            if n == 1:
                return True
            elif n < 1:
                return False
            else:
                return powerFour(n/4)
        return powerFour(n)