for _ in range(int(input())):
    n, k = map(int, input().split())
    MOD = 10**9 + 7
    arr = list(map(int, input().split()))
    
    mx = 0
    curr = 0

    for i in range(n):
        curr = max(arr[i], curr + arr[i])
        mx = max(mx, curr)
    
    arrSm = sum(arr)
    out = (arrSm % MOD + (pow(2, k, MOD) - 1)* mx) % MOD
    print(out)
