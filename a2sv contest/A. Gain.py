for _ in range(int(input())):
    n = int(input())
    
    stg = list(map(int, input().split()))
    
    compare = stg[:]
    compare.sort(reverse=True)

    out = [0]*n
    for i in range(n):

        if stg[i] == compare[0]:
            out[i] = stg[i] - compare[1]
        else:
            out[i] = stg[i] - compare[0]
        
    print(*out)