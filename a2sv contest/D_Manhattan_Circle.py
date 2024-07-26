
for _ in range(int(input())):
    n, m = map(int, input().split())
    pts = []
    for i in range(n):
        row = input()
        for j in range(m):
            if row[j] == '#':
                pts.append((i+1, j+1))
        
    pts.sort()
    x = pts[len(pts)//2][0]
    pts.sort(key=lambda x: x[1])
    
    y = pts[len(pts)//2][1]
    print(x, y)