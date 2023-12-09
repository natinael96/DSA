t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    l = n - 1
    r = 0
    for i in range(n):
        if s[i] == 'A':
            l = i
            break
    for i in range(n - 1, -1, -1):
        if s[i] == 'B':
            r = i
            break
    print(max(0, r - l))

