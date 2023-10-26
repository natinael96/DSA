class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if i == "(":
                stack.append(count)
                count = 0
            else:
                prev_count = stack.pop()
                count = prev_count + max(count * 2, 1)

        return count