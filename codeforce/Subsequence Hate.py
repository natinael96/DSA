t = int(input())

while t > 0:
    s = input()
    n = len(s)

    # Calculate prefix sums for '0' and '1'
    prefix0 = [0] * (n + 1)
    prefix1 = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix0[i] = prefix0[i - 1] + (s[i - 1] == '0')
        prefix1[i] = prefix1[i - 1] + (s[i - 1] == '1')

    ans = min(prefix0[n], prefix1[n])

    for i in range(1, n + 1):
        # Calculate suffix counts
        suf0 = prefix0[n] - prefix0[i]
        suf1 = prefix1[n] - prefix1[i]

        # Calculate prefix counts
        pref0 = prefix0[i]
        pref1 = prefix1[i]

        # Update the answer
        ans = min(ans, pref1 + suf0, pref0 + suf1)

    print(ans)
    t -= 1
