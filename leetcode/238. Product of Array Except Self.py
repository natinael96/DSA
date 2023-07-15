def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    # Calculate prefix product
    prefix_product = 1
    for i in range(n):
        answer[i] *= prefix_product
        prefix_product *= nums[i]

    # Calculate suffix product and multiply with the prefix product
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix_product
        suffix_product *= nums[i]
        print(suffix_product)

    return answer

