for _ in range(int(input())):
    
    n = int(input())
    a = list(map(int,input().split()))
    dist = len(set(a))
    arr = [max(dist,k) for k in range(1,n+1)]
    print(*arr)
