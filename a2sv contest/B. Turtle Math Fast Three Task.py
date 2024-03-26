

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    totSm = sum(arr)
    if not totSm % 3:
        print(0)
    elif (totSm + 1) % 3 == 0:
        print(1)
    else:
        yes = False
        for i in arr:
            cur = totSm - i
            if cur % 3 == 0:
                yes =True
        if yes:
            print(1)
        else:
            print(2)
        
