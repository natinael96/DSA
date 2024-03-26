n, q = map(int, input().split())

price = list(map(int, input().split()))

price.sort()
price = [0] + price
for i in range(1, n+1):
    price[i] += price[i-1]
price.sort(reverse = True)
for i in range(q):
    x, y = map(int, input().split())
    
    buy = price[0] - price[x]
    maxfre = price[x-y] - price[x]
    print(maxfre)   