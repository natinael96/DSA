class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # + - * /
        # each operand maybe int or other
        # no zero div
        # division == 0 
        
        stack = []
        
        for i in tokens:
            if i.isdigit() or (i[0] == "-" and i[1:].isdigit()):
                stack.append(int(i))
            elif i in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()
                if i == "/":
                    stack.append(int(num1 / num2))
                elif i == "+":
                    stack.append(num1+ num2)
                elif i == "-":
                    stack.append(num1 - num2)
                else:
                    stack.append(num1*num2)
        return stack.pop()
        
        