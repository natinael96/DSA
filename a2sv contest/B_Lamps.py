from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    d = defaultdict(list)
    for i in range(0, n):
        x, y = map(int, input().split())
        d[x].append(y)
        
    ans = 0
    for i in d:
        d[i] = sorted(d[i], reverse=True)
        ans += sum(d[i][:i])
    print(ans)