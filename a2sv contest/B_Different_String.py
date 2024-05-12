import random
from collections import Counter

for i in range(int(input())):
    s = input()
    c = Counter(s)
    if len(c) == 1:
        print('NO')
    else:
        print("YES")
        ans = ""
        while True:
            sh = list(s)
            random.shuffle(sh)
            sh = ''.join(sh)
            if sh != s:
                ans = sh
                break
                
        print(ans)
