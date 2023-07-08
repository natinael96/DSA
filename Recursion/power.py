def power(b, n):
    if n == 0:
        return 1
    elif n > 0:
        return b * power(b, n - 1)
    else:
        return power(b, n + 1) / b
