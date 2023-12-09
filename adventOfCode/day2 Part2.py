validGames = []
colors = ["red", "green", "blue"]

while True:
    n = input()
    if n.strip() == "":
        break
    gameId, record = n.split(":")

    recs = record.split(";")
    colCount = {"red": 0, "green": 0, "blue": 0}
    for k in range(len(recs)):
        curRec = recs[k].split(",")
        for i in range(len(curRec)):
            color = None
            numBall = 0
            for col in colors:
                if col in curRec[i]:
                    color = col

            for i in curRec[i]:
                if i.isnumeric():
                    numBall = numBall * 10 + int(i)
                    
            colCount[color] = max(numBall, colCount[color])

    appen = 1
    for col in colors:
        appen *= colCount[col]
    
    validGames.append(appen)


    
print("Sum of Valid IDS: ", sum(validGames))
