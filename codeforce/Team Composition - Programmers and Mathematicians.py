
t = int(input())

for i in range(t):
    
    a, b = map(int, input().split())
    
    if a < b: a, b = b, a
    
    dif = abs(a - b)
    three_and_one = dif // 2
    ans = min(three_and_one, b) + (b - min(three_and_one, b)) // 2
    print(ans)
    