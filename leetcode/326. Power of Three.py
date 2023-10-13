class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def powerThree(n):
                if n == 1:
                    return True
                elif n < 1:
                    return False
                else:
                    return powerThree(n/3)
        return powerThree(n)
    