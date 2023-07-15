lst = input().split()
messi = lst[:2]
ronaldo = lst[2:]

if (messi[0]*2 + messi[1]) ==  ronaldo[0]*2 + ronaldo[1]:
    print( "Equal")
elif (messi[0]*2 + messi[1]) >  ronaldo[0]*2 + ronaldo[1]:
    print( "Messi")
else:
    print("Ronaldo")