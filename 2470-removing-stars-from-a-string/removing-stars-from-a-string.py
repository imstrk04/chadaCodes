class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch != "*":
                stack.append(ch)
            
            if ch == "*":
                stack.pop()
        
        return "".join(stack)