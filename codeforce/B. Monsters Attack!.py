def solve():
    m, s = map(int, input().split())
    rest = 0
    mp = {}

    v = []
    for _ in range(m):
        x = int(input())
        a = int(input())
        v.append((a, x))

    for i in v:
        if i[0] < 0:
            mp[abs(i[0])] = (i[1], 0)
        else:
            mp[i[0]] = (0, i[1])

    last = 0
    for key, value in sorted(mp.items()):
        rest += (key - last) * s
        last = key
        total = sum(value)
        rest -= total
        if rest < 0:
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
