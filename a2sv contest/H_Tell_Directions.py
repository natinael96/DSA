from collections import deque

m, n, k = map(int, input().split())

if k % 2 == 1:
    print("IMPOSSIBLE")
else:
    grid = [[] for _ in range(m)]
    strR, strC = 0, 0
    
    for i in range(m):
        a = input()
        grid[i] = a
        for j in range(n):
            if grid[i][j] == 'X':
                strR, strC = i, j
    
    dxns = {'D': (1, 0), 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0)}
    q = deque([(strR, strC)])
    visited = set()
    visited.add((strR, strC))
    path = [[0 for _ in range(n)] for _ in range(m)]
    
    def inbound(x, y):
        return 0 <= x < m and 0 <= y < n
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in dxns.values():
            nr, nc = r + dr, c + dc
            if inbound(nr, nc) and grid[nr][nc] == '.' and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))
                path[nr][nc] = path[r][c] + 1
    
    ans = []
    r, c = strR, strC
    
    for i in range(k):
        for key, (dr, dc) in dxns.items():
            nr, nc = r + dr, c + dc
            if inbound(nr, nc) and grid[nr][nc] != '*' and path[nr][nc] <= k - i - 1:
                r, c = nr, nc
                ans.append(key)
                break
    
    if len(ans) != k:
        print('IMPOSSIBLE')
    else:
        print(''.join(ans))
