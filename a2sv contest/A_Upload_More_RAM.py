for _ in range(int(input())):
    n, k = map(int, input().split())
        
    print(n + (n  - 1)* (k - 1))