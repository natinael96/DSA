class Solution:
    def decodeString(self, s: str) -> str:
        Stack = []
        curr_num = 0
        new_s = ""
        for i in s:
            if i.isdigit():
                curr_num = curr_num * 10 + int(i)
            elif i == "[":
                Stack.append([new_s, curr_num])
                new_s = ""
                curr_num = 0
            elif i == "]":
                prevStr , prevNum = Stack.pop()
                new_s = prevStr + new_s*prevNum
            else:
                new_s += i
        return new_s