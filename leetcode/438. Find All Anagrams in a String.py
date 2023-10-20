from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        window_size = len(p)
        indices = []
        
        pCount = defaultdict(int)
        for char in p:
            pCount[char] += 1
            
        window = defaultdict(int)  
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if r >= window_size-1: 
                if window == pCount:
                    indices.append(l)
                
                window[s[l]] -= 1
                if window[s[l]] == 0: 
                    del window[s[l]]
                l += 1
                
        return indices