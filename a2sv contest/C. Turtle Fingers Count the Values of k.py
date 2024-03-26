import math

for _ in range(int(input())):
    
    a,b,l = map(int, input().split())
     
    aa = int(math.log(l, a))
    bb = int(math.log(l, b))
    
    combo = set()
    count = 0
    for a1 in range(100):
        for b1 in range(100):
            combs = (a**a1) * (b ** b1)
            if combs > l: break
            if combs not in combo and l % combs == 0:
                count += 1
            combo.add(combs)
    
    print(count)
        
    