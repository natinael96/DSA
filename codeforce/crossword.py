from collections import defaultdict

n, m = map(int, input().split())
s = []
a = []

for _ in range(n):
    s.append(input())
    a.append(s[-1])

row_freq = [defaultdict(int) for _ in range(n)]
col_freq = [defaultdict(int) for _ in range(m)]

for i in range(n):
    for j in range(m):
        row_freq[i][s[i][j]] += 1
        col_freq[j][s[i][j]] += 1

for i in range(n):
    for j in range(m):
        if row_freq[i][s[i][j]] == 1 and col_freq[j][s[i][j]] == 1:
            print(s[i][j], end='')

print()
