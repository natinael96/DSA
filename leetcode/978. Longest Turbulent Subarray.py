class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        maxLen = 1
        currLen = 1
        l = 0
        for i in range(1, len(arr)-1):
            
            if l%2 == 0 and ((i%2 == 1 and arr[i] > arr[i-1]) or (i%2 == 0 and arr[i] < arr[i-1])):
                currLen += 1
            elif l%2 == 1 and ((i%2 == 0 and arr[i] > arr[i-1]) or (i%2 == 1 and arr[i] < arr[i-1])):
                currLen += 1
            else:  
                maxLen = max(maxLen, currLen)
                currLen = 1
                l = i
            
        return max(maxLen, currLen)
        