for _ in range(int(input())):
    n, k = map(int, input().split())
    grid = [[] for i in range(n)]
    for i in range (n):
        a = input()
        for j in a:
            grid[i].append(j)
    
    ans = []
    for i in range(0, n, k):
        rw = []
        for j in range(0, n, k):
            rw.append(grid[i][j])
        ans.append(rw)
    for i in ans:
        print(''.join(i))