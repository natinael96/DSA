def find_max_crossing_subarray(arr, low, high):
    left_sum = float('-inf')
    mid = len(arr) // 2
    sum_ = 0

    for i in range(mid, low - 1, -1):
        sum_ += arr[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i

    right_sum = float('-inf')
    sum_ = 0
    for j in range(mid + 1, high+1):
        sum_ += arr[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j

    return max_left, max_right, left_sum + right_sum


