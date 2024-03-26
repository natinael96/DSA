for _ in range(int(input())):
    
    n, x = map(int, input().split())
    
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    l , r = 0, 0
    count  = 0
    while l < n and r < n:
        
        if arr[r] * (r - l + 1) >= x:
            count += 1
            l = r + 1
            r = l
        else:
            r += 1
            
    print(count)
        
            