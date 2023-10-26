class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        return nums
    ###########################
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:   # need to keep this 0 at low's place
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
                
            elif nums[mid] == 1: # 1 in correct place 
                mid += 1
            
            elif nums[mid] == 2: # need to keep 2 this 2 at high's place
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
        return nums

        