def ch10(x1,y1,x2,y2):
    
    if x1 > x2 or y1 > y2:
        return False
    
    if x1 == x2 and y1 == y2:
        return True
    else:
        return ch10(x1, x1 + y1, x2, y2) or ch10(x1 + y1, y1,x2,y2)
    