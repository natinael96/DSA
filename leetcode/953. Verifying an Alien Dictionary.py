class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ordr = {char: i for i, char in enumerate(order)}

        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            min_len = min(len(word1), len(word2))
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if ordr[word1[j]] > ordr[word2[j]]:
                        return False
                   
                    break
            else:
                
                if len(word1) > len(word2):
                    return False
        return True