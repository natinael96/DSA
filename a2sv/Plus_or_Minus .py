n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

for num in nums:
    if num[1] + num[0] == num[2]:
        print("+")
    else:
        print("-")
