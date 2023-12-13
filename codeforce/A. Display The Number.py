t = int(input())
for _ in range(t):
    n = int(input())
    result = " "
    while n >= 4:
        result += "1"
        n -= 2
    if n == 3:
        result += "7"
        n -= 3
    elif n == 2:
        result += "1"
        n -= 2

    result = result[::-1]
    print(result)
