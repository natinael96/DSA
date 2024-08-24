for _ in range(int(input())):
    s, t = map(str, input().split())
    st = set(t)
    nws = []
    for i in s:
        if i in st:
            nws.append(i)
    t = [i for i in t]
    
    flag = True
    
    idx = len(nws) - 1
    while idx > -1 and t:
        if t[-1] == nws[idx]:
            t.pop()
            idx -= 1
        else:
            if nws[idx] in t:
                flag = False
                break
            else:
                idx -= 1
        # print(t)
    
    if not flag or len(t) > 0:
        print('NO')
    else:
        print('YES')
                
        
    
        