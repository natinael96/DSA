for _ in range(int(input())):
    
    n = int(input())
    
    ana = list(map(int, input().split()))
    ana.sort(reverse = True)
    bis = list(map(int, input().split()))
    bis.sort()
    
    for i in range(n+1):
        
        ana[i-1] -= 1
        bis[i-1] = 0

        bis[i - 1] -= 1
        ana[i - 1] = 0
            
    print(ana)
    print("  " ,sum(ana) - sum(bis))
        