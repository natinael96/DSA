for _ in range(int(input())):
    
    n = map(int, input().split())
    a = list(map(int, input().split()))
    mod = 998244353
    
    
    b = [(-1, 1), (a[0], 1, 1)]
    s = 1
    for i in a:
        x = y = 0
        while i < b[-1][0]: 
            i, j = b.pop()[1:]
            
            x, y = (x + i), (y+j)
        b.append((i,(s + y), (x + y)))
        s = (2 * s - x + y)%mod
    print(s)