class Solution:
    
    #Function to find minimum number of pages.
    # n - book
    # A - page
    # M - students
    def findPages(self,A, N, M):
        
        l, r, ans = max(A), sum(A), -1

        if N < M: return -1

        def isValid(A, M, mid):
            pageSum = 0
            reqStu = 1

        
            for p in A:
                pageSum += p
                if pageSum > mid:
                    reqStu += 1
                    pageSum = p
                
            if reqStu > M: return False
            else: return True

        while l < r:
            mid = l + (r - l)//2
            if isValid(A,M,mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans 