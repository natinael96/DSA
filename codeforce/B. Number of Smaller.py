n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
m_arr = list(map(int, input().split()))


count = [0] * m

i = 0  # Pointer for the first array

for j in range(m):
    while i < n and n_arr[i] < m_arr[j]:
        i += 1
    count[j] = i
    j += 1

print(*count)