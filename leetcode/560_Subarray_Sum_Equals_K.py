def subarraySum(nums: list[int], k: int) -> int:
    sum_freq = {}
    count = 0
    c_sum = 0

    for i in nums:
        c_sum += i

        if c_sum == k:
            count += 1

        if c_sum - k in sum_freq:
            count += sum_freq[c_sum - k]

        if c_sum in sum_freq:
            sum_freq[c_sum] += 1
        else:
            sum_freq[c_sum] = 1
    print(sum_freq)
    return count


a = subarraySum([1, 2, 3], 3)
print(a)
