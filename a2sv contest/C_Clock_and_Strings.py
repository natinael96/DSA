def cw(a, b, c):
    return (b - a) % 12 < (c - a) % 12

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    if cw(a, b, c) != cw(a, b, d) and cw(c, d, a) != cw(c, d, b):
        print("YES")
    else:
        print("NO")
