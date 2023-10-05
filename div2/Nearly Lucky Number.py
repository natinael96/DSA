num = int(input())
arr = list(map(int, input().split()))

arr.sort()

if arr[num - 1] >= arr[num - 2] + arr[num - 3]:
    print("NO")
else:
    print("YES")
    print(arr[num - 3], arr[num - 1], arr[num - 2], end=' ')
    for i in range(num - 3):
        print(arr[i], end=' ')
