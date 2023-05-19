A = []

for k in range(1,len(A)):
    key = A[k]  # store the element at index k as key

    j = k - 1   # another var "j" to store the index before key

    while j > -1 and A[j] > key:
        A[j+1] = A[j]

        j += 1
    A[j+1] = key
