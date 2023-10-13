from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recurSoln(strng, i):
            n = len(strng)
            if i == n // 2:
                return
            else:
                strng[i], strng[n - i - 1] = strng[n - i - 1], strng[i]
                recurSoln(strng, i + 1)
        
        recurSoln(s, 0)