n = int(input())
nums = [list(map(int,input().split()))for _ in range(n)]

a = 0
for j in nums:
    for i in nums:
        if j[0] > i[0] and j[1] < i[1]:
            a = 1
            break
    if a == 1:
        print("Happy Alex")
        break
if a == 0:
    print("Poor Alex")
