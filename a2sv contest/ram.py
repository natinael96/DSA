def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    r = list(zip(a, b))
    r.sort()

    for i in range(n):
        if r[i][0] <= k:
            k += r[i][1]
        else:
            break

    print(k)

testcases = int(input())
for _ in range(testcases):
    solve()
