for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    preSm = 0
    mx = 0
    gd = 0
    for i in arr:
        preSm += i
        mx = max(mx, i)
        if preSm == 2 * mx:
            gd += 1
    print(gd)