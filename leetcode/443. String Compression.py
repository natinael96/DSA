class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0

        while i < len(chars):
            j = i
            count = 0
            char = chars[i]
            
            while j < len(chars) and chars[j] == char:
                count += 1
                j += 1
            
            if count == 1:
                chars[i:j] = [char]
                i += 1
            else:
                if count >= 10:
                    countList = list(str(count))
                    chars[i:j] = [char] + countList
                    i += len(countList) 
                elif 1 <= count <= 9:
                    chars[i:j] = [char, str(count)]
                    i += 2

        return i