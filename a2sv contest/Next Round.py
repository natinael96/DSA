n, k = map(int, input().split())
scores = list(map(int,input().split()))

count = 0

for score in scores:
    if score >= scores[k - 1] and score > 0:
        count += 1
    elif score <= 0:
        break

print(count)
