for _ in range(int(input())):
    n, x = map(int, input().split())
    cnt = 0
    for a in range(1, x - 1):
        for b in range(1, x - a):
            if a * b >= n:
                break
            mxc = min(x - a - b, (n - a * b) // (a + b))
            if mxc > 0:
                cnt += mxc
    print(cnt)