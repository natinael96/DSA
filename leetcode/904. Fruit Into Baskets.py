class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        dict = {}
        maxFruit = 0
        for r in range(len(fruits)):
            if fruits[r] not in dict:
                dict[fruits[r]] = 0
            dict[fruits[r]] += 1
            
            if len(dict) <= 2:
                maxFruit = max(maxFruit, r - l + 1)
            else:
                dict[fruits[l]] -= 1
                if not dict[fruits[l]]:
                    dict.pop([fruits[l]])
                l += 1
        return maxFruit
    