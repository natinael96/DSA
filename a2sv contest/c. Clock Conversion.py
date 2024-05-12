t = int(input())
 
for _ in range(t):
    h, m = map(int, input().split(":"))
    
    new_hour = h % 12
    if h == 12:
        new_hour = 12
    elif h == 0:
        new_hour = 12
 
    if new_hour < 10:
        new_hour = "0" + str(new_hour)
 
    if m < 10:
        m = "0" + str(m)
    
    if h < 12:
        print(str(new_hour) + ":" + str(m) + " AM")
    else:
        print(str(new_hour) + ":" + str(m) + " PM")
