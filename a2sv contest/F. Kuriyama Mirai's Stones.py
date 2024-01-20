n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(arr[:])

prefix_sum_arr = [0] * n
prefix_sum_arr2 = [0] * n

prefix_sum_arr[0] = arr[0]
prefix_sum_arr2[0] = arr2[0]

for i in range(1, n):
    prefix_sum_arr[i] = prefix_sum_arr[i-1] + arr[i]
    prefix_sum_arr2[i] = prefix_sum_arr2[i-1] + arr2[i]

q = int(input())
for i in range(q):
    t, l, r = map(int, input().split())
    l -= 1
    r -= 1
    if t == 1:
        if l == 0:
            print(prefix_sum_arr[r])
        else:
            print(prefix_sum_arr[r] - prefix_sum_arr[l-1])
    else:
        if l == 0:
            print(prefix_sum_arr2[r])
        else:
            print(prefix_sum_arr2[r] - prefix_sum_arr2[l-1])
