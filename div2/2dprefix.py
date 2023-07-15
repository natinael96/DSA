class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            self.prefixsum = 0
            return
        r, c = len(matrix), len(matrix[0])
        self.prefixsum = [[0] * (c + 1) for i in range(r + 1)]

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                self.prefixsum[i][j] = matrix[i - 1][j - 1] + self.prefixsum[i - 1][j] + \
                                       self.prefixsum[i][j - 1] - self.prefixsum[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.prefixsum:
            return 0

        return self.prefixsum[row2 + 1][col2 + 1] - self.prefixsum[row1][col2 + 1] - \
            self.prefixsum[row2 + 1][col1] + self.prefixsum[row1][col1]
