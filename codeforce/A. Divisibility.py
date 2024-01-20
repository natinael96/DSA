
n, a, b = map(int, input().split())
if a <= 0 and b >= 0:
    a = -a
    ans = 1 + (a // n) + (b // n)
    print(ans)

elif a <= 0 and b <= 0:
    a = -a
    b = -b
    a, b = b, a  # swap(a, b)
    ans = (b // n) - ((a - 1) // n)
    print(ans)
else:
    ans = (b // n) - ((a - 1) // n)
    print(ans)

