for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    smal = min(arr)
    
    indx = arr.index(smal)
    
    if arr[indx:] == sorted(arr[indx:]):
        print(indx)
    else:
        print(-1)
    