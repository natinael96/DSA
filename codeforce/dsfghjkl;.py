t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    s = [i for i in nums]
    count = 0
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - 1]:
            count += 1
        else:
            break
    print(count)