for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    count = {}

    for ch in s:
        chLow = ch.lower()
        if chLow not in count:
            count[chLow] = [0, 0]  
        if ch.islower():
            count[chLow][0] += 1
        else:
            count[chLow][1] += 1

    pairs = 0
    exc = 0

    for lCnt, uCnt in count.values():
        mn = min(lCnt, uCnt)
        pairs += mn
        exc += abs(lCnt - uCnt) // 2

    result = pairs + min(exc, k)
    print(result)
