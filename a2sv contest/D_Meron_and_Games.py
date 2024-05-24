"""from typing import Counter


n = int(input())
arr = list(map(int, input().split()))
cnt = Counter(arr)
v = sorted(cnt.items())
#print(v)
dp = [0] * len(v)

for i in range(len(v)):
    pr = i - 1
    while pr >= 0 and v[pr][0] + 1 == v[i][0]:
        pr -= 1
    if pr == -1:
        dp[i] = v[i][0] * v[i][1]
    else:
        dp[i] = dp[pr] + v[i][0] * v[i][1]
    if i != 0:
        dp[i] = max(dp[i], dp[i - 1])
#print(dp)
print(dp[-1])"""


from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

cnt = Counter(arr)
max_value = max(arr)
dp = [0] * (max_value + 1)
#print(cnt)
for i in range(1, max_value + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + i * cnt[i])
    #print(dp, i, cnt[i])

print(dp[-1])
