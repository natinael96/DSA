t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    total = sum(a)
    
    for i in range(1, n+1):
        a[i] += a[i - 1]
    
    l, mx = 0, -1
    
    for  i in range(1, n):
        mx  = max(mx, a[i] - a[l])
        if a[i] < a[l]:
            l = i
    
    l = 1
    
    for i in range(2, n+1):
        mx = max(mx, a[i] - a[l])
        if a[i] < a[l]:
            l = i
        
    if total > mx:
        print("YES")
    else:
        print("NO")
