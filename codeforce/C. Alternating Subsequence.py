for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    pos = a[0]
    neg = 0
    
    i = 1
    while i < n and a[i] * a[i - 1] > 0:
        pos = max(pos + a[i], pos)
        i += 1
        
    if i < n:
        neg = pos +a[i]
        i += 1
    
               
         
            