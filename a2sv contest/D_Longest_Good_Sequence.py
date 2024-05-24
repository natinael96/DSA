n = int(input())
a = list(map(int, input().split()))

mx = max(a) + 1
div = [0] * mx

#sieve
for i in range(2, mx):
    if div[i] == 0:
        div[i] = i
        if i * i < mx:
            for j in range(i * i, mx, i):
                if div[j] == 0:
                    div[j] = i
# print(mx)
# print(div)
dp = [0] * mx
ans = 0
for x in a:
    chain = 0
    temp = x
    while temp > 1:
        chain = max(chain, dp[div[temp]])
        temp //= div[temp]
    chain += 1
    ans = max(ans, chain)
    temp = x
    while temp > 1:
        dp[div[temp]] = max(chain, dp[div[temp]])
        temp //= div[temp]

print(ans)

