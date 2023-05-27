num = int(input())

nums = input().split()

numls = nums

single = []

for i in numls:
    if i not in single:
        single.append(i)

tower = [0] * len(single)
for i in numls:
    tower[single.index(i)] += 1

maxx = tower[0]
for k in tower:
    if int(k) >= int(maxx):
        maxx = k

print(maxx, len(tower))
