cardi = [0]
while True:
    n = input()
    if n.strip() == "":
        break
    cardId,cardNums = map(str.strip ,n.split(":"))
    
    guess, winning = map(str.strip, cardNums.split("|"))
    
    pts = 0
    
    winn = set()
    for i in winning.split():
        winn.add(int(i))
    
    gss = set()
    for j in guess.split():
        gss.add(int(j))
        
    for k in gss:
        if k in winn:
            pts = 1 if pts == 0 else pts*2
    
    cardi.append(pts)

print("Sum: ", sum(cardi))
