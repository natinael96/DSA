from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        l = 0 
        maxLen = 0
        
        for r in range(len(s)):
            
            if s[r] not in chars:
                chars[s[r]] = 0
            chars[s[r]] += 1
            
            window_size = r - l + 1
            
            if window_size - max(chars.values()) <= k:
                maxLen = max(maxLen, window_size)
            else:
                chars[s[l]] -= 1

                if not chars[s[l]]:
                    chars.pop(s[l])
                l += 1
            
        return maxLen