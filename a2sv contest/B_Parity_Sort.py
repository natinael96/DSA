for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    l = [i % 2 for i in arr]
    y = [i % 2 for i in sorted(arr)]
    
    if l == y:
        print("YES")
    else:
        print("NO")