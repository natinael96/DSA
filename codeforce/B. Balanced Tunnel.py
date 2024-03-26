n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

preA = [0]*(n+1)
preB = [0]*(n+1)
sm = 0

for i,A in enumerate(a):
    preA[A] = i+1
for i,B in enumerate(b):
    preB[B] = i+1
for i in range(1,n+1):
    preA[i] += preA[i-1]
    preB[i] += preB[i-1]

for i in range(len(preA)):
    sm += (preA[i] - preB[i])
    
print(sm)