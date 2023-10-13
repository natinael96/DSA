def merge_sorted_arrays(arr1, arr2, n, m):

    merged = [0] * (n + m) 
    i = 0  # arr1
    j = 0  # arr2
    k = 0  # merged array

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged[k] = arr1[i]
            i += 1
        else:
            merged[k] = arr2[j]
            j += 1
        k += 1

    #  remaining from arr1
    while i < n:
        merged[k] = arr1[i]
        i += 1
        k += 1

    # remaining arr2
    while j < m:
        merged[k] = arr2[j]
        j += 1
        k += 1

    return merged

# Read input
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Merge the arrays
merged_array = merge_sorted_arrays(arr1, arr2, n, m)
print(*merged_array)
