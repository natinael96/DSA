
n, q= map(int, input().split())

arr = list(map(int, input().split()))
maxm = max(arr)
maxPos = arr.index(maxm) 
A = ''
B = ''
for i in range(q):
    q = int(input())
            
    if q >= maxPos:
        A = maxm
        B = q  - (maxPos +1 ) % (n - 1) + 1
    else:
        A = maxm - (maxPos - arr[q - 1])
        B = A + 1
    print(A, B)
