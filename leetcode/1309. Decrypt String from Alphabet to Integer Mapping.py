class Solution:
    def freqAlphabets(self, s: str) -> str:
        out = []
        
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                curr = int(s[i: i + 2])
                out.append(chr(curr + 96)) 
                i += 3
            else:
                out.append(chr(int(s[i]) + 96))
                i += 1

        return ''.join(out)
