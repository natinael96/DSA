t = int(input())

for _ in range(t):
    n = int(input())

    if n % 3 == 1 or n % 3 == 2:
        print("First")
    else:
        print("Second")
