def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return left


n = int(input())  # no of shop
x = list(map(int, input().split()))  # price of bottle
x.sort()  # Sort the prices in ascending order
q = int(input())  # no of days

for _ in range(q):
    m = int(input())  # no of coins
    count = binary_search(x, m)
    print(count)
