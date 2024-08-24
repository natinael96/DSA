n = int(input())
arr = list(map(int, input().split()))

arr =arr[::-1]

ans = [arr[0]]

for i in range(1, n):
    ans.append(arr[i - 1] + arr[i])
    
print(*ans[::-1])
        
