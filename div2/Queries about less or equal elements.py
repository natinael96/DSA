import bisect
n, m = map(int, input().split())

a = (list(map(int, input().split())))
b = (list(map(int, input().split())))
a.sort()
b.sort()

for i in b:   
    l = 0    
    r = len(a)
    mid = l + (r - l)//2
    while l <= r:
        if a[mid] > i:
            r = mid - 1
        elif a[mid] <= i:
            l = mid + 1
            
        