n = int(input())

shows = []
for _ in range(n):
    l, r = map(int, input().split())
    shows.append([l,r])
shows.sort(key = lambda x: x[1])

minEnd = float('-inf')

can = True
for sh in shows:
    if sh[0] < minEnd:
        can = False
        break
    minEnd = sh[1]
if can:
    print("YES")
else:
    print("NO")
    
    
    
"""
can = True
tv1E, tv2E = 0, 0

for show in shows:
    strtT, endT = show

    if strtT >= tv1E:
        tv1E = endT
    elif strtT >= tv2E:
        tv2E = endT
    else:
        can = False 
if can:
    print("YES")
else:
    print("NO")
    """


    
