cont = True
allNums = []
while cont:
    n = input()
    if not n:
        break
    
    l, r = 0, len(n) - 1
    frst = None
    scnd = None
    
    while l <= r:
        if n[l].isdigit():
            frst = (n[l])
            break
        else:
            l += 1

    while r >= l:
        if n[r].isdigit():
            scnd = (n[r])
            break
        else:
            r -= 1
        
    if frst is not None and scnd is not None:
        allNums.append(int(frst + scnd))
        
print("Sum: ", sum(allNums))