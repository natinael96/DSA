class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindowSize = 0
                
        for i in range(len(s)):
            currSub = ""
            for j in range(i,len(s)):
                if s[j]  in currSub:
                    break
                currSub += s[j]
                maxWindowSize = max(j - i, maxWindowSize)
                    
                
        return maxWindowSize