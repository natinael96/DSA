for _ in range(int(input())):
    n = int(input())
    a= list(map(int, input().split()))
    b= list(map(int, input().split()))
    s=0
    tgt = b[-1]
    mn=float('inf')
    for i in range(n):
        s+=abs(a[i] - b[i])
        if(a[i] <= tgt <=b[i] or b[i] <= tgt <= a[i]):
            mn = 1
        else:
            mn= min(mn, 1 + abs(tgt - a[i]), 1 + abs(tgt - b[i]))
        
    print(s+mn)