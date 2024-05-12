cnt = 0
for n in range(int(input()) + 1):
    
    fact = set()
    
    i = 2
    while(i * i <= n) : 
        
        while n % i == 0:
            
            fact.add(i)
            n //= i
            
        i += 1
        
    if n > 1:
        fact.add(n)
        
    if len(fact) == 2:
        cnt += 1
  
print(cnt)