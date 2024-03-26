t = int(input())

for _ in range(t):
    st  = input()
    n = len(st)
    pre0 = [0]*(n+1)
    pre1 = [0]*(n+1)
    ans = 0
    for i in range(1, n+1):
        pre0[i] = pre0[i-1] + (st[i-1] == "0")
        pre1[i] = pre1[i-1] + (st[i-1] == "1")
        
        ans = min(pre0[n], pre1[n])
        
    for i in range(1,n+1):
        suf0 = pre0[n] - pre0[i]
        suf1 = pre1[n] - pre1[i]
        
        ans = min(ans, suf0 + pre1[i] , suf1 + pre0[i])
        
    print(ans)
        