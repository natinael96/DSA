class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        new_str = ''
        i = 0
        while i < len(s):
            if len(spaces) != 0 and i == spaces[0]:
                new_str += ' '
                del spaces[0]
            else:
                new_str += s[i]
                i += 1
        return new_str                