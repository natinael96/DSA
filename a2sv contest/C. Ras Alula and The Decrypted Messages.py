for _ in range(int(input())):
    
    n, m = map(int, input().split())
    
    mess = input()
    wrd = input()
    
    arr= [ord(i) for i in mess]
    wd = sum([ord(i) for i in wrd])
    print(arr )
    print(wd)
    #print(arr)
    
    sm = 0
    l = 0
    ans = 'NO'
    for r in range(n):
        sm += arr[r]
        #print(sm)
        if (r - l + 1) >= m:
            if sm == wd:
                ans = 'YES'
                break
            sm -= arr[l]
            l += 1
        
    print(ans) 
            