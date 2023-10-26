from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        countDict = defaultdict(int) 
        

        n = len(s)
        
        for r in range(10,n+1):
            l = r - 10
            countDict[s[l:r]] += 1
            
        out = []
        for i in countDict.keys():
            if countDict[i] > 1 and i not in out:
                out.append(i)
        
        return out