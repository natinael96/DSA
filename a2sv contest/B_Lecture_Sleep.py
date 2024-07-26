
n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
t = [0] + list(map(int, input().split()))
s = 0
p, m = 0, 0
for i in range(n + 1):
    x, y = a[i], t[i]
    s += x * y
    p += x * (1 - y)
    p -= a[max(0, i - k)] * (1 - t[max(0, i - k)])
    m = max(p, m)
print(s + m)

