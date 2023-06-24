t = int(input())  # Accept the number of test cases

test_cases = []

# Accept the test cases
for _ in range(t):
    matrix = []
    for _ in range(2):
        row = list(map(int, input().split()))
        matrix.append(row)
    test_cases.append(matrix)

# Print the test cases
for matrix in test_cases:
    print(matrix)
