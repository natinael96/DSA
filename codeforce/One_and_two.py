def mult(arr):
    multi = 1
    for i in arr:
        multi *= int(i)
    return multi


for j in range(int(input())):
    freq = int(input())
    nums = input().split()
    tot = mult(nums)

    L = 1
    for i in range(1,len(nums)):
        L *= int(nums[i-1])
        R = tot//L
        if L == R:
            print(i)
            break
        elif i+1 == len(nums):
            print(-1)
        else:
            i += 1

