from typing import Counter


n, k = map(int, input().split())
s = input()

cnt = Counter(s)

if len(cnt) < k:
    print(0)
else:
    print(sorted(cnt.values())[0] * k)