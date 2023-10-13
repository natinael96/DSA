class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        def pasc(arr,row):
            if len(arr) == row + 1:
                return arr
            else:
                n_list = [1]
                for i in range(len(arr) - 1):
                    n_member = arr[i] + arr[i+1]
                    n_list.append(n_member)
                n_list.append(1)
                
                return pasc(n_list, row)
        
        return pasc([1], rowIndex)
    

solution = Solution()
a = solution.getRow(7)
print(a)