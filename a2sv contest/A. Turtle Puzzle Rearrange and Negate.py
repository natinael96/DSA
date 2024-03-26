for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sm = 0
    for i in range(n):
        if arr[i] < 0:
            sm += -1*arr[i]
        else:
            sm+= arr[i]
    print(sm)