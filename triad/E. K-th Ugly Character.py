t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    out = ["a"] * n
    arr = [2]
    kk = 2
    while arr[-1] < (n * (n - 1) // 2):
        arr.append(arr[-1] + kk)
        kk += 1
    arr = arr[::-1]
    
    for i in range(len(arr)):
        if k >= arr[i]:
            out[i] = "b"
            out[k - arr[i]] = "b"
            break  # Break once k-th string is formed
    
    print("".join(out))
