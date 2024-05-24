n, k = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
sm = []
for i in range(n - 1, -1, -1):
    sum += a[i]
    sm.append(sum)

sm.pop()
sm.sort(reverse=True)

for i in range(k - 1):
    sum += sm[i]
    

print(sum)
#print(sm)
