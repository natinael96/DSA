def helper(l, r, arr):
    if r - l == 1:
        return 0
    mid = (l + r) // 2
    
    ans = 0
    if max(arr[l:mid]) > max(arr[mid:r]):
        arr[l:mid], arr[mid:r] = arr[mid:r], arr[l:mid]
        ans += 1
        
    lft = helper(l, mid, arr)
    rgt = helper(mid, r, arr)
    
    return lft + rgt + ans
    

for _ in range(int(input())):
    m = int(input())
    arr = list(map(int, input().split()))
    
    ans = helper(0, len(arr), arr)
    
    print(ans) if arr == sorted(arr) else print(-1)
    
