from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # frequency Count
    dic = Counter(a)
    cnt = 0
    for i in range(n):
        # check single element exist??
        if dic[a[i]] < 2:
            cnt = 1
            break
    if cnt == 1: 
        # Find any single frequency cnt  print -1
        print(-1)

    else:
        ans = [x for x in range(1,n+1)]
        for i in range(n-1):
            if a[i] == a[i+1]:
                ans[i], ans[i+1] =  ans[i+1], ans[i]
        print(*ans)