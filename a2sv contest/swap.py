n = int(input())
arr = list(map(int, input().split()))

swaps = []  # List to store the swaps

for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    if min_idx != i:
        swaps.append((i, min_idx))
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the elements

print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])
