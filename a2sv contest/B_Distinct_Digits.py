for _ in range(int(input())):
    s = int(input())
    
    dig = []
    for i in range(9, 0, -1):
        if s >= i:
            dig.append(i)
            s -= i
        if s == 0:
            break
    dig.sort()
    print(''.join(map(str, dig)))

