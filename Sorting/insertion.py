A = [31, 41, 59, 26, 41, 58]

for i in range(1, len(A)):
    key = A[i]  # store the element at index k as key

    j = i - 1   # another var "j" to store the index before key

    while j >= 0 and A[j] > key:
        A[j+1] = A[j]

        j -= 1
    A[j+1] = key

print(A)