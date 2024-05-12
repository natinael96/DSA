for _ in range(int(input())):
    n = int(input())
    ans1 = ''
    ans2 = ''
    for i in range(1,n+1):
        if i % 2 == 1:
            ans1 += '#'*2
            ans2 += '.'*2
        else:
            ans1 += '.'*2
            ans2 += '#'*2
    out = []
    for i in range(1, n+1):
        if i % 2 == 1:
            out.append(ans1)
            out.append(ans1)
        else:
            out.append(ans2)
            out.append(ans2)
    for a in out:
        print(a)