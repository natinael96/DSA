for _ in range(int(input().strip())):
    n, m = map(int, input().strip().split())
    a = [list(map(int, input().strip().split())) for _ in range(2)]

    c = [0]*(n+m+1)

    res = 0
    cntA = cntB = 0
    for i in range(n+m+1):
        val = int(a[0][i] < a[1][i])
        if val:
            if cntB == m:
                t = i
                c[i] = 2
                break
            cntB += 1
        else:
            if cntA == n:
                t = i
                c[i] = 2
                break
            cntA += 1
        c[i] = val
        res += a[val][i]

    val ^= 1
    for i in range(t+1, n+m+1):
        c[i] = val
        res += a[val][i]

    ans = [str(res) if i == t else str(res-a[c[i]][i]+a[val][t]) for i in range(n+m+1)]
    print(' '.join(ans))