class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        out = []
        if target in nums:
            indx = nums.index(target)
            indices = nums.count(target)
            for i in range(indx, indx+indices):
                out.append(i)
        return out