n , k  = map(int, input().split())

nums = [0] + list(map(int, input().split()))
for i in range(1, n+1):
    nums[i] += nums[i-1]
minL = nums[k]
indx = 0
for i in range(k,n+1):
    
    curWin = nums[i] - nums[i-k]
    if curWin < minL:
        indx = i-k
        minL = curWin
print(indx+1) 

"""
1 1
100
"""