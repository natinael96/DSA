t = int(input())

for _ in range(t):
    n = int(input())
    nums = set(map(int, input().split()))
    
    if len(nums) == 1:
        print(n)
    else:
        print(1)