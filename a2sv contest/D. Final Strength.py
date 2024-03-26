def compare(mid, l, r):
    temp = arr[l:r+1]
    mid -= l
    for i in range(mid+1):
        cmp = temp[i]
        for j in range(mid+1, len(temp)):
            if cmp > temp[j]:
                arr[l+i] += 1
            elif cmp < temp[j]:
                arr[l+j] += 1

def divide(l, r):
    if r - l == 0:
        return

    mid = l + (r-l) // 2

    divide(l, mid)
    divide(mid + 1, r)
    compare(mid, l, r)

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    divide(0, len(arr) - 1)

    print(" ".join(map(str, arr)))
