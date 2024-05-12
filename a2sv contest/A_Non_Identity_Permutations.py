for _ in range(int(input())):
    n = int(input())
    arr = [i for i in range(1, n + 1)]
    
    arr = sorted(arr,reverse = True)
    if len(arr) % 2 == 1:
        mid = len(arr)//2
        arr[mid], arr[-1] = arr[-1], arr[mid]

    print(*arr)        
    
    