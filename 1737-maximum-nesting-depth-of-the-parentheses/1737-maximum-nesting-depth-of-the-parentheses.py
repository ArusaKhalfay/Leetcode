class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []

        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(s[i])
                res = max(res, len(stack))
            elif s[i] == ')':
                stack.pop()
            else:
                continue

        return res
        