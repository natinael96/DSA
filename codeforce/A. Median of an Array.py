from collections import Counter
import math
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    mid = (math.ceil(n/2))
    cnt= Counter(arr[mid-1:])
    nm = arr[mid - 1]
    print(cnt[nm])
    