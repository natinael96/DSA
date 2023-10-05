from math import ceil
t = int(input())

for i in range(t):
    n, s = map(int, input().split())
    count = n // 2 + 1
    print(s // count)
    
    