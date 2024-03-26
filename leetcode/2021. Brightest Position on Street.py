from collections import defaultdict


def brightestPosition(arr):
    
    begin = [v[0] - v[1] for v in arr]
    end = [v[0] + v[1] for v in arr]
    
    events = defaultdict(int)
    
    for i in begin:
        events[i] += 1
    for i in end:
        events[i +1] -= 1
    
    curr = maxBri = 0
    ans = 0
    print(events)
    for pos in sorted(events):
        curr += events[pos]
        
        if maxBri <curr:
            maxBri = max(curr, maxBri)
            ans = pos
    return ans

a = brightestPosition([[-3,2],[1,2],[3,3]])
print(a)