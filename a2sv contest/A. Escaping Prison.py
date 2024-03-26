for _ in range(int(input())):
    n, h = map(int,input().split())
    
    crSm = 0
    for i in range(n):
        w, l =map(int, input().split())
        crSm += max(w,l)
    if crSm >= h:
        print("YES")
    else:
        print("NO")