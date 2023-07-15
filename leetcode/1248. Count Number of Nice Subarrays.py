def numberOfSubarrays(nums: list[int], k: int) -> int:
    # Transform the array by replacing even numbers with 0 and odd numbers with 1
    for i in range(len(nums)):
        nums[i] = 0 if nums[i] % 2 == 0 else 1

    # Count the number of subarrays with sum k using prefix sum
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)
    print(nums)
    print(prefix_sum)

    count = 0
    occurrences = {}
    for i in prefix_sum:
        count += occurrences.get(i - k, 0)
        print(i, " ", count)
        occurrences[i] = occurrences.get(i, 0) + 1
        print(occurrences)

    return count


nums = [2,2,2,1,2,2,1,2,2,2]
k = 2

print(numberOfSubarrays(nums, k))
