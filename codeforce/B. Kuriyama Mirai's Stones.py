n = int(input())
m = list(map(int, input().split()))

mS = sorted(m)
t1 = [0]*(n+1)
t2 = [0]*(n+1)

for i in range(1,n+1):
    t1[i] = t1[i - 1] + m[i - 1]
    
    t2[i] = t2[i - 1] + mS[i - 1]
for i in range(int(input())):
    t,l,r = map(int,input().split())
    if t == 1:
        print(t1[r] - t1[l-1])
    else:
        print(t2[r] - t2[l-1])