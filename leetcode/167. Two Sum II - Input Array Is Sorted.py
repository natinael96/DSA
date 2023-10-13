class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] in numbers:
                return [i+1, numbers.index(target - numbers[i], i+1)+1]