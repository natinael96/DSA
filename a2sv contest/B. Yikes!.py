n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    arr[i] += arr[i-1]

m = int(input())
qr = list(map(int, input().split()))

for i in range(m):
    targ = qr[i]
    
    l, r = 0, n - 1
    ans = ''
    while l < r:
        mid = (l + r) // 2
        if arr[mid] == targ:
            ans = mid + 1
            break
        elif arr[mid] > targ:
            r = mid
        else:
            l = mid + 1
    print(r + 1) if ans == '' else print(ans) 
            