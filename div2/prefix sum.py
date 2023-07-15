class NumArray:
    def __init__(self, nums: list[int]):
        self.per_sum = [0]
        summ = 0
        for i in nums:
            summ += i

            self.per_sum.append(summ)
        print(self.per_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.per_sum[right + 1] - self.per_sum[left]


a = [3, 1, 7, 0, 4, 1, 6]

b = NumArray(a)

print(b.sumRange(1, 4))
