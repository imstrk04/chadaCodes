class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(openCount, closedCount):
            if openCount == closedCount == n:
                res.append("".join(stack))
            
            if openCount < n:
                stack.append("(")
                dfs(openCount + 1, closedCount)
                stack.pop()
            
            if closedCount < openCount:
                stack.append(")")
                dfs(openCount, closedCount + 1)
                stack.pop()
            
        dfs(0, 0)
    
        return res