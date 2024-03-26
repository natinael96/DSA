n, k ,q = map(int, input().split())

reci = [0] * (200000 + 2)
out = [0]*q
for _ in range(n):
    l, r = map(int, input().split())
    reci[l] += 1
    reci[r+1] -= 1

cc = 0
for i in range(1, 200000 + 2):
    cc += reci[i]
    reci[i] = (cc >= k)
print(reci[90:101])    
for i in range(1, len(reci)):
    reci[i] += reci[i - 1]
print(reci[85:101])    
for j in range(q):
    a,b = map(int, input().split())
    out[j] = reci[b] - reci[a-1]

for i in out:
    print(i)
    