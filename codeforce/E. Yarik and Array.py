T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    f = [0] * (n + 1)

    for i in range(1, n + 1):
        f[i] = a[i - 1]

    ans = float('-inf')

    for i in range(n - 1, 0, -1):
        if abs(a[i - 1]) % 2 != abs(a[i]) % 2:
            f[i] = max(f[i], f[i] + f[i + 1])

    for i in range(1, n + 1):
        ans = max(ans, f[i])

    print(ans)
