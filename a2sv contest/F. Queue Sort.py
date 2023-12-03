t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mn = min(a)
    mn_indx = a.index(mn)

    has_inv = any(a[i] < a[i - 1] for i in range(mn_indx, n))

    if has_inv:
        mn_indx = -1

    print(mn_indx)
