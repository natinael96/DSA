from collections import defaultdict
t = int(input())

for _ in range(t):
    
    dicT = defaultdict(list)
    
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(n):
        dicT[i%k].append(arr[i])
    for ke in dicT.keys():
        dicT[ke].sort()
    newArr = [0]*n
    for ke in dicT.keys():
        
        for j, val in enumerate(dicT[ke]):
            newArr[k *  j + ke] = val
    maxSm = 0
    
    for i in range(1, n):
        newArr[i] += newArr[i - 1]
    newArr = [0] + newArr
    for i in range(k, n+1):
        maxSm = max(maxSm, newArr[i] - newArr[i - k])
    print(maxSm)
