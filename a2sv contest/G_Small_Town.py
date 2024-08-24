for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    # print(arr)
    # 1, 4, 4, 14, 19
    # 37, 59
    # 73, 98
    
    l, r = 0 , arr[-1]
    def can(mid):
        cnt = 0
        mx = arr[-1]
        for i in arr:
            if abs(i - mx) > mid:
                mx = i + mid
                cnt += 1
        if cnt <= 3:
            return True
        return False
                
    while l < r:
        mid = (l + r) // 2
        if can(mid):
            r = mid
        else:
            l = mid + 1
    print(r)
        
        
    
    
    
    
