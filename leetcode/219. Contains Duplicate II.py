class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()
        for r in range(len(nums)):
            if nums[r] in win:
                return True
            
            win.add(nums[r])
            
            if len(win) > k:
                win.remove(nums[r-k])
        return False
                