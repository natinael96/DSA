N = int(input())
arr = list(map(float, input().split()))
DP = [0.0] * (N + 1)
DP[0] = 1.0

for i in range(N):
    for j in range(i + 1, -1, -1):
        if j == 0:
            DP[j] = DP[j] * (1 - arr[i])
        else:
            DP[j] = DP[j] * (1 - arr[i]) + DP[j - 1] * arr[i]

ans = 0.0
for i in range(N + 1):
    tails = N - i
    if i > tails:
        ans += DP[i]

print(ans)