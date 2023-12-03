from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n)]
        que = deque(arr)
        count = 0
        popped = []

        while que:
            if count == k:
                pp =que.pop()
                popped.append(pp)
                count = 0
            left = que.popleft()
            que.append(left)
            count += 1
                

        return popped[-1]

soln = Solution()
a = soln.findTheWinner(5,1)
print(a)