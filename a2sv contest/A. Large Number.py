t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    number = input().strip()
    
    max_number = list(number)
    for i in range(n):
        if number[i] < str(d):
            max_number.insert(i, str(d))
            break
    if len(max_number) == n:
        max_number.append(str(d))
    
    print(''.join(max_number))
