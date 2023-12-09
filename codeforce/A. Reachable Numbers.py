n = int(input())
reachable_numbers = set()

while n not in reachable_numbers:
    reachable_numbers.add(n)
    n += 1

    while n % 10 == 0:
        n //= 10

print(len(reachable_numbers))


