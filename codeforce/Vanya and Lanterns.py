

################################################
n, l = map(int, input().split())
lanterns = list(map(int, input().split()))
lanterns.sort()

r = max(lanterns[0], l - lanterns[-1])*2

for i in range(n-1):
    r = max(r,lanterns[i+1]-lanterns[i])

print("{:.20f}".format(r / 2))