if __name__ == '__main__':
    n = int(input())
    list = []
    for _ in range(n):
        command = input().split()
        
       
        if command[0] == 'insert':
            position = int(command[1])
            element = int(command[2])
            list.insert(position, element)
            
        elif command[0] == 'print':
            print(list)
            
        elif command[0] == 'remove':
            element = int(command[1])
            list.remove(element)
            
        elif command[0] == 'append':
            element = int(command[1])
            list.append(element)
            
        elif command[0] == 'sort':
            list.sort()
            
        elif command[0] == 'pop':
            list.pop()
            
        elif command[0] == 'reverse':
            list.reverse()