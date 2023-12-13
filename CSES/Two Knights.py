n = int(input())
print(0)
for k in range(2,n+1):
    soln = ((k**2 *(k**2 - 1))//2) - (4*(k - 2)*(k - 1))
    print(soln)