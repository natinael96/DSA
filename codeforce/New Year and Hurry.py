# n problems
# 1 - n difficulty increase
# 5 * i  minutes to solve one ith
# k minute to get to frnd house
# how many problem to make it to the party

n, k = map(int, input().split())

l, r = 0, n

def canSolve(mid):
    time = 240 - k
    tot = (mid * (mid + 1)) // 2 * 5
    return tot <= time
    
while l <= r:
    mid = l + (r - l)//2
    
    if canSolve(mid):
        l = mid + 1
    else:
        r = mid - 1

print(l - 1)