for _ in range(int(input())):
    n = int(input())
    password = input()
    
    dig = []
    let = []
    wasDig = False
    can = True
    for char in password:
        if char.isdigit():
            if wasDig == False:
                dig.append(char)
            else:
                can = False
        else:
            if not wasDig:
                wasDig = True
            let.append(char)
    
    if dig != sorted(dig):
        can = False
    
    if let != sorted(let):
        can = False

    if can:
        print('YES')
    else:
        print('NO')
    
    