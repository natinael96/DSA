for _ in range(int(input())):   
    n, k, x = map(int, input().split())

    if x != 1:
        print("Yes")
        print(n)
        print(*([1] * n))
    elif k == 1 or (k == 2 and n % 2 == 1):
        print("No")
    else:
        print("Yes")
        print(n // 2)
        
        ans = []
        if n % 2 == 1:
            ans.append(3)
        else:
            ans.append(2)
        ans += [2] * (n // 2 - 1)
        print(*ans)
        