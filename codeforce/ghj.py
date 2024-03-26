import math
from collections import defaultdict


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) == 1:
        print("NO")
        return
    else:
        print("YES")
        i = 0
        j = n - 1
        while i < j:
            print(a[i], a[j], end=" ")
            i += 1
            j -= 1
        if n % 2 != 0:
            print(a[i])
        else:
            print()


def main():
    testcases = int(input())
    for _ in range(testcases):
        solve()


if __name__ == "__main__":
    main()
