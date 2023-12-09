validGames = []
colors = ["red", "green", "blue"]
setNumBall = {"red": 12, "green": 13, "blue": 14}

while True:
    n = input()
    if n.strip() == "":
        break
    valid = True
    gameId, record = n.split(":")
    gId = 0
    for i in gameId:
        if i.isnumeric():
            gId = gId * 10 + int(i)

    recs = record.split(";")

    for k in range(len(recs)):
        colCount = {"red": 0, "green": 0, "blue": 0}
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
            colCount[color] = numBall

        for co in colors:
            if colCount[co] > setNumBall[co]:
                valid = False
                break

    if valid:
        validGames.append(gId)

print("Valid Games: ", validGames)
print("Sum of Valid IDS: ", sum(validGames))
