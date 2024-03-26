def subarray(arr, t, n):
    i, j = 0, 0
    count = 0
    while i < n:
        while j < n and arr[i] == arr[j]:
            j += 1
            count += 1

        t[arr[i]] = max(count, t[arr[i]])
        i = j
        count = 0

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    fa = [0] * 2*(n + 1)
    fb = [0] * 2*(n + 1)
    subarray(a, fa, n)
    subarray(b, fb, n)
    sum1 = 0
    for i in range(len(fa)):
        sum1 = max(sum1, fa[i] + fb[i])
    print(sum1)
