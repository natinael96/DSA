
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    """if sorted(arr) == arr:
        print("NO")
        continue"""
    maxx = arr[0]
    nxtmx = arr[0]
    for i in arr:
        if i < nxtmx:
            nxtmx = i
            break
        
    result = "YES" if arr[0] > sum(arr[arr.index(nxtmx):]) else "NO"
    
    print(result)


