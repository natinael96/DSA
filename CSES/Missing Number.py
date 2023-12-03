n = int(input())
arr = list(map(int, input().split()))
arr.sort()
l = 0
r = len(arr) - 1

while l <= r:
    mid = (l + r)//2
    if arr[mid] != mid + 1:
        r = mid - 1
    else:
        l = mid + 1
        
print(l + 1)