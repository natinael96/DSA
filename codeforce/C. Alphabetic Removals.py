n, k = map(int, input().split())
str = input().strip()

for x in range(ord('a'), ord('z') + 1):
    x = chr(x)
    if k == 0:
        break
    
    
    for i in range(n):
        if k == 0:
            break

        if str[i] == x:
            str = str[:i] + ' ' + str[i + 1:]
            k -= 1

result = ''.join(char for char in str if not char.isspace())
print(result)
