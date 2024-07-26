for _ in range(int(input())):
    n =  int(input())
    arr = list(map(int, input().split()))
    
    if arr == sorted(arr):
        print(0)
    else:
        cnt = 0
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                # print(arr)
                df = arr[i - 1] - arr[i]
                cnt += df
                arr[i] = arr[i - 1]
                
        print(cnt + 1)

    