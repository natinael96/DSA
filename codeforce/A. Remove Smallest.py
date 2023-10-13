for _ in range(int(input())):
    length = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    if len(nums) != 1:
        for j in range(length-1, 0, -1):
            if nums[j] - nums[j-1] <= 1:
                del nums[j]
                
    if len(nums) == 1:
        print("YES")
    else:
        print("NO")