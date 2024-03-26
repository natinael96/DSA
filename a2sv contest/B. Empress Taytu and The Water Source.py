import math


for _ in range(int(input())):
    n, k = map(int, input().split())
    dem = list(map(int, input().split()))
    time = list(map(int, input().split()))
    
    def isOkay(mid):
        sm = 0
        for i in range(n):
            sm += (math.ceil(dem[i] / mid) * time[i])
        return sm <= k
    
    avr = sum(dem)//n
    
    l, r = 1, sum(dem) + 1
    
    while l < r:
        mid = (l + r)//2
        #print(mid)
        if isOkay(mid):
            r = mid
        else:
            l = mid + 1
            
    print(l)  if l <= sum(dem) else print(-1)