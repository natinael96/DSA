for _ in range(int(input())):
    n = int(input())
    s = input()
    
    arr = []
    for i in s:
        arr.append(i)
        
    narr = sorted(arr)
    print("".join(narr))