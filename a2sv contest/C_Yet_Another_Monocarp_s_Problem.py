for _ in range(int(input())):
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    
    def can(mid):
        cur = 0
        for i in range(n - 1):
            cur += min(arr[i + 1] - arr[i], mid)
        
        return cur + mid >= h
    
    l, r = 0, h
    while l < r:
        mid = (l + r)//2
        
        if can(mid):
            r = mid
        else:
            l = mid + 1
    
    print(l)