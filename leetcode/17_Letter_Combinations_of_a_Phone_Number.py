class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []

        combo = []

        def backtrack(combination,index):
            if index == len(digits):
                combo.append(combination)
                return
            digit = digits[index]
            letters = dic[digit]

            for l in letters:
                backtrack(combination+l,index+1)
        backtrack("",0)
        return combo