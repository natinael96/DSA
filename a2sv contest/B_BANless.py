for _ in range(int(input())):
    n = int(input())
    print((n+1)//2)
    ans = []
    for i in range((n+1)//2):
        ans.append([3*i + 2, 3*(n-i)])

    for a, b in ans:
        print(a, b)