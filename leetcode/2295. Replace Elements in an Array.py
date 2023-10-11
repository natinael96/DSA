class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        position = {num: i for i, num in enumerate(nums)}
        
        for operation in operations:
            i, j = operation
            if i in position:    
                pos = position[i]
                nums[pos] = j
                del position[i]
                position[j] = pos
            
        return nums