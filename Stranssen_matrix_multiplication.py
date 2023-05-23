def square_matrix_multiply(A,B,C):
    n = A.rows

    for i in range(0,n):
        for j in range(0,n):
            C[i][j] = 0

            for k in range(0,n):
                C[i][j] += A[i][k]*B[k][j]
# naive