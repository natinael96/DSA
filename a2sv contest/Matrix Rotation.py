def rotate(matr):
    n_matrix = [[0, 0], [0, 0]]
    n_matrix[0][0] = matr[1][0]
    n_matrix[0][1] = matr[0][0]
    n_matrix[1][0] = matr[1][1]
    n_matrix[1][1] = matr[0][1]
    return n_matrix


n = int(input())  # Accept the number of test cases

mat = []

# Accept the test cases
for _ in range(n):
    matrix = []
    for _ in range(2):
        row = list(map(int, input().split()))
        matrix.append(row)
    mat.append(matrix)

for mat0 in mat:
    for _ in range(4):
        if mat0[0][0] < mat0[0][1] < mat0[1][1] and mat0[1][1] > mat0[1][0] > mat0[0][0]:
            print("YES")
            break
        mat0 = rotate(mat0)
    else:
        print("NO")
