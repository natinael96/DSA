class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # n x n matrix
        row, column = len(matrix), len(matrix[0])
        
        def isValid(num):
            count = 1
            for i in range(row):
                left, right = 0, column - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    
                    if matrix[i][mid] <= num:
                        left = mid + 1
                    else: 
                        right = mid - 1
                count += left
            return count <= k
        
        low,high = matrix[0][0], matrix[0][-1]
        for i in range(row):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][-1])
            
        left, right = low, high
        
        while left <= right:        
            mid = left + (right - left) // 2
            
            if isValid(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return left
            