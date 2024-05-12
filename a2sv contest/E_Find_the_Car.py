import sys
from bisect import bisect_right

t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split())) + [n]
    b = list(map(int, input().split())) 
    queries = [int(input()) for _ in range(q)]
    times = [0] * (n + 1)
    
    for i in range(1, n + 1):
        times[i] = times[i - 1] + (a[i] - a[i - 1]) / (b[i] * 1.0)
    results = []
    
    for d in queries:
        if d == 0:
            results.append(0)
        else:
            i = bisect_right(a, d)
            if i == 0:
                results.append((d / (b[0])))
            else:
                results.append(times[i - 1] + (d - a[i - 1]) / (b[i - 1]))
                
    print(*results)
