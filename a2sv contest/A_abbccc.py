
n = int(input())
t = input().strip()
s = ""
i = 0
length = 1  
while i < n:
    s += t[i]
    i += length
    length += 1

print(s)
