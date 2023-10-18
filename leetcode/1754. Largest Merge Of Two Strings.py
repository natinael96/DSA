class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
  
        newStr = ""
        
        while word1 and word2:
        
            if word1[0] > word2[0]:
                newStr += word1[0]
                word1 = word1[1:]
            
            elif word1[0] < word2[0]:  
                newStr += word2[0]
                word2 = word2[1:]
            
            else:
            
                for i in range(1, min(len(word1), len(word2))):
                    if word1[i] != word2[i]:
                        if word1[i] > word2[i]:
                            newStr += word1[0] 
                            word1 = word1[1:]
                        else:
                            newStr += word2[0]
                            word2 = word2[1:]
                        break
                    
                else:
                    if len(word1) > len(word2):
                        newStr += word1[0]
                        word1 = word1[1:]
                    else:  
                        newStr += word2[0]
                        word2 = word2[1:]
                    
        if word1:
            newStr += word1
        else:  
            newStr += word2

        return newStr