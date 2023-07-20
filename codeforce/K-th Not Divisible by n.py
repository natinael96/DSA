# kth not div by n
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    
    l, r =  1, k*n       
        
    while l < r:
        mid = l + (r - l) // 2
        
        count = mid - (mid//n)
        
        if count < k:
            l = mid + 1
        else:
            r = mid
        
    print(l)