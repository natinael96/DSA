class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com = strs[0]

        for i in range(1, len(strs)):
            temp = ""
            for j in range(min(len(com), len(strs[i]))):
                if com[j] == strs[i][j]:
                    temp = com[:j+1]
                else:
                    break
            com = temp
        return com