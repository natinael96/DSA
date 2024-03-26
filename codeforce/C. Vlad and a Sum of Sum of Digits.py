def digit_sum(num):
    total_sum = 0
    while num > 0:
        total_sum += num % 10
        num //= 10
    return total_sum

def main():
    t = int(input())
    while t > 0:
        n = int(input())

        total_sum = 0
        for i in range(1, n + 1):
            total_sum += digit_sum(i)

        print(total_sum)
        t -= 1

main()
