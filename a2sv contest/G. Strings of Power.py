s = input()

heavy = 0
amount = 0
for i in range(4, len(s)):
    if s[i] == 'l':
        if s[i-4:i] == 'meta':
            amount += heavy
    elif s[i-4:i+1] == 'heavy':
        heavy += 1

print(amount)
