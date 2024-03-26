for _ in range(int(input())):
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    stack = []
    count = 0
    last = 0
    for i in range(n):
        if len(stack) == 0:
            stack.append(arr[i])
        else:
            while stack and arr[i] < stack[-1]:
                count += 1
                stack.pop()
            stack.append(arr[i])
    print(count)
        
