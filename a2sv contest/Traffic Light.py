t = int(input())  # Number of test cases

while t > 0:
    n, c = input().split()
    n = int(n)
    s = input().strip()
    k = -1
    ans = float('-inf')
    s += s
    for i in range(len(s)-1, -1, -1):
        if s[i] == 'g':
            k = i
        if s[i] == c:
            ans = max(ans, k - i)
    print(ans)
    t -= 1
