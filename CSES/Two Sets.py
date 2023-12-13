n = int(input())
tot = n * (n + 1) // 2

if tot % 2 != 0:
    print("NO")
else:
    print("YES")
    sumHalf = tot // 2
    first_set = []
    second_set = []

    current_sum = 0
    for i in range(n, 0, -1):
        if current_sum + i <= sumHalf:
            first_set.append(i)
            current_sum += i
        else:
            second_set.append(i)

    print(len(first_set))
    print(*first_set)
    print(len(second_set))
    print(*second_set)



