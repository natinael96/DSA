t = int(input())
for j in range(t):
    n, x = map(int, (input().split()))
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort(reverse=True)
    
    harmon = True
    for i in range(n):
        if a[i] + b[i] > x:
            harmon = False
    if harmon:
        print("YES")
    else:
        print("NO")
    if j < t - 1:
        c = input()