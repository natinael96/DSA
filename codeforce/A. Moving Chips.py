t =int(input())

for _ in range(t):
    n = int(input())
    
    arr = list(map (int, input().split()))
    
    l = arr.index(1)
    
    r = 0
    for i in range(n):
        if arr[i] == 1:
            r = i
    
    leng = r - l + 1
    
    ans = leng - sum(arr[l:r+1])
    
    print(ans)
    
    