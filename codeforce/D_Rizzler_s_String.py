s = str(input())
s += 'b'
a = []
mod = 10 ** 9 + 7
cnt = 0
for i in s:
    if i == 'b':
        a.append(cnt+1)
        cnt = 0
    elif i == 'a':
        cnt += 1

tot = 1
for i in a:
    tot = (tot * i) % mod
print(tot - 1)