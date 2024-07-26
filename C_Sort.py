for _ in range(int(input())):
    n, q = map(int, input().split())
    a = input()
    b = input()
            
    pre_a = [[0] * (n + 1) for _ in range(26)]
    pre_b = [[0] * (n + 1) for _ in range(26)]
    
    for i in range(n):
        for j in range(26):
            pre_a[j][i + 1] = pre_a[j][i]
            pre_b[j][i + 1] = pre_b[j][i]
        pre_a[ord(a[i]) - ord('a')][i + 1] += 1
        pre_b[ord(b[i]) - ord('a')][i + 1] += 1
    
    for k in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        
        operations = 0
        for j in range(26):
            freq_a = pre_a[j][r + 1] - pre_a[j][l]
            freq_b = pre_b[j][r + 1] - pre_b[j][l]
            operations += abs(freq_a - freq_b)
            
        print(operations // 2)