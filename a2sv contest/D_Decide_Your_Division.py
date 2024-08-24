for _ in range(int(input())):
    n = int(input())
    cnt = 0
    # if n == 1:
    #     print(-1)
    
    while n % 5 == 0:
        n //= 5
        cnt += 3
        
    while n % 3 == 0:
        n //= 3
        cnt += 2
        
    while n % 2 == 0:
        n //= 2
        cnt += 1

    if n != 1:
        print("-1")
    else:
        print(cnt)
