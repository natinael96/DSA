def sell_tickets(n, bills):
    change_25 = 0
    change_50 = 0

    for bill in bills:
        if bill == 25:
            change_25 += 1
        elif bill == 50:
            change_25 -= 1
            change_50 += 1
        elif bill == 100:
            if change_50 > 0:
                change_50 -= 1
                change_25 -= 1
            else:
                change_25 -= 3

        if change_25 < 0:
            return "NO"

    return "YES"

n = int(input())
bills = list(map(int, input().split()))

result = sell_tickets(n, bills)
print(result)
