t = int(input())

for _ in range(t):
    
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    l, r = 0, n/2
    maxSum = 0
    while l < r:
        maxSum += (arr[n-l-1] - arr[l])
        l += 1       
        
    print(maxSum)
    