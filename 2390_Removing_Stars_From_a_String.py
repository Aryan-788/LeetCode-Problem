class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            stack.pop() if c == "*" else stack.append(c) 
        return "".join(stack)
