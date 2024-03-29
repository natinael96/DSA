class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) - 1
        ans = 0
        
        for i in range(n, 1, -1):
            right  = i - 1
            left = 0
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += (right - left)
                    right -= 1
                else:
                    left += 1
                    
        return ans