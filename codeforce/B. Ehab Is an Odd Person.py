n = int(input())
nums = list(map(int, input().split())) 
even , odd = 0,0
for i in nums:
    if i% 2 == 0:
        even += 1
    else:
        odd += 1
if even and odd:
    print(*(sorted(nums)))
else:
    print(*nums)
