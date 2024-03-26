sts = list(map(str, input().strip()))
n = int(input())

preS = [0]*(len(sts) + 1)

for i in range(1,len(sts)):
    preS[i] = (sts[i] == sts[i-1])

for i in range(1,len(preS)):   
    preS[i] += preS[i-1]


for _ in range(n):
    l,r = map(int, input().split())
    
    print(preS[r-1] - preS[l-1] )
    