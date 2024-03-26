for _ in range(int(input())):
    n,k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    mnt = [0]*n
    for i in range(1,n-1):
        mnt[i] = ((arr[i] > arr[i-1]) and (arr[i] > arr[i+1]))
        mnt[i] += mnt[i-1]
    maxP = 0
    ind = 0
    for i in range(k-1,n):
        curP = mnt[i - 1] - mnt[i - k+1]
        if curP > maxP:
            maxP , ind = curP, i - k + 1
    print(maxP + 1, ind+1)
        