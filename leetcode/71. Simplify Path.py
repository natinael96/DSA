class Solution:
    def simplifyPath(self, path: str) -> str:
        Stack = []
        dirs = path.split("/")
        for dirr in dirs:
            if dirr == "." or not dirr:
                continue
            elif dirr == "..":
                if Stack:
                    Stack.pop()
            else:
                Stack.append(dirr)
                    
        return "/" + "/".join(Stack)