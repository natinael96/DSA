s = list(input().strip())
n = int(input())

cntr = [0]*(len(s))
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        cntr[i] += 1
    cntr[i] += cntr[i-1]
for _ in range(n):
    l, r = map(int, input().split())
    print(cntr[r-1] - cntr[l-1])
    

