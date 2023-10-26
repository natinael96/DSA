from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)  
        n = len(t)
        if m < n:
            return ""
        
        tStore = defaultdict(int)
        for i in t:
            tStore[i] += 1
        
        sStore = defaultdict(int)
        rt = ""
        l = 0
        minWinSize = float('inf')
        for r in range(m):
            sStore[s[r]] += 1
            while self.allIn(sStore,tStore):
                winSize = r - l + 1
                if winSize < minWinSize:
                    minWinSize = winSize
                    rt = s[l:r+1]
                if s[l] in tStore:
                    sStore[s[l]] -= 1
                l+=1
                
        return rt if minWinSize != float('inf') else ""
    
    def allIn(self, sStore, tStore):
        for char,count in tStore.items():
            if sStore[char] < count:
                return False
        return True
        
                