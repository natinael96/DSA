a  = int(input())
b = int(input())
c = int(input())
for i in range(a, -1, -1):
    if i * 2 <= b and i * 4 <= c:
        print(i * 7)
        break