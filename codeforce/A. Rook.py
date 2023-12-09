t = int(input())

for _ in range(t):
    n = input()
    horz = n[0]
    vert = int(n[1])
    
    hor = []
    ver = []
    
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h"]
    
    for i in range(8):
        if alpha[i] + str(vert) != n:
            hor.append(alpha[i] + str(vert))
        
    for i in range(1,9):
        if horz + str(i) != n:
            ver.append(horz + str(i))
        
    for i in hor:
        print(i)
    for i in ver:
        print(i)
