class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def compare(num1,num2):
            if num1 == num2: 
                return 0
            if num1 > num2 : 
                return 1
            return -1
        maxLen = 1
        l = 0
        for r in range(1,len(arr)):
            cond = compare(arr[r-1],arr[r])
            if cond == 0:
                l = r
            elif r == len(arr)-1 or cond * compare(arr[r],arr[r+1]) != -1:
                maxLen = max(maxLen, r - l + 1)
                l = r
        return maxLen
    
    
