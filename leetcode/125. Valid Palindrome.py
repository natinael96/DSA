class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = []
        for i in str:
            if i.isalnum():
                s.append(i.lower())
                
        return s[:] == s[::-1]