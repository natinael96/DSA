n, m, a, b = map(int, input().split())
answer = 0

if m * a <= b:
    answer = n * a
else:
    answer = (n // m) * b + min((n % m) * a, b)

print(answer)