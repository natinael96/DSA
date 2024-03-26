t = int(input())
for _ in range(t):
    l,r = map(int,input())
    num = 0
    luck = 0
    
    for i in range(l,r+1):
        lar = max(str(i))
        smal = min(str(i))