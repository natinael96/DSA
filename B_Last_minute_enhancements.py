t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    a.sort()
    s.add(a[0])
    for i in range(1, n):
        if a[i - 1] >= a[i]:
            a[i] += 1
        s.add(a[i])
    print(len(s))
