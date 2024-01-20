# n card rows 

n = int(input())
cards = list(map(int, input().split()))

l, r = 0, n-1
ser = 0
dima = 0
counter = 0
while l <= r:
    counter += 1
    if counter%2 == 1:
        if cards[l] < cards[r]:
            ser += cards[r]
            r -= 1
        else:
            ser += cards[l]
            l+=1
    else:
        if cards[l] < cards[r]:
            dima += cards[r]
            r -= 1
        else:
            dima += cards[l]
            l+=1

print(ser,dima )
        
    