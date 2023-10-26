from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        
        # one ticket at a time 
        # at index k
        # if other are zero leave the line
        
        que = deque([i for i in range (len(tickets))])
        
        count = 0
        while que:
            point = que.popleft()
            tickets[point] -= 1
                
            if tickets[point] >= 1:
                que.append(point)
                
            count += 1
            if tickets[k] == 0:
                return count                
            
    
solution = Solution()
a = solution.timeRequiredToBuy([2,3,2], 2)
print(a)        