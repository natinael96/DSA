n = int(input())
a = list(map(int, input().split()))
preS, out = 0, 0

a.sort()

for i in range(n):
    if a[i] >= preS:
        out += 1
        preS += a[i]

print(out)
