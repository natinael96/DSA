class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p = s1
        s = s2
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
                    return True
                
                window[s[l]] -= 1
                if window[s[l]] == 0: 
                    del window[s[l]]
                l += 1
                
        return False