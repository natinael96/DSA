"""n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
m_arr = list(map(int, input().split()))

count = [0] * m

for i in range(m):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if n_arr[mid] < m_arr[i]:
            count[i] = mid + 1
            left = mid + 1
        else:
            right = mid - 1

print(*count)"""

n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
m_arr = list(map(int, input().split()))


count = [0] * m

i = 0  # Pointer for the first array
j = 0  # Pointer for the second array

while j < m:
    while i < n and n_arr[i] < m_arr[j]:
        i += 1
    count[j] = i
    j += 1

print(*count)