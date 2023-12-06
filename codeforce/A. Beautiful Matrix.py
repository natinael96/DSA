matrix = [[0]]*5
row1 = 0
for i in range(5):
    matrix[i] = list(map(int, input().split()))
    if 1 in matrix[i]:
        row1 = i
col1 = matrix[row1].index(1)

print(abs(3-(row1+1)) + abs(3-(col1+1)))