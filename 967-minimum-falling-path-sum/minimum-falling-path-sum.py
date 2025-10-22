class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        @cache
        def f(i, j):
            if j < 0 or j >= n:
                return float('inf')
            
            if i == 0:
                return matrix[0][j]

            up = matrix[i][j] + f(i-1, j)
            ld = matrix[i][j] + f(i-1, j-1)
            rd = matrix[i][j] + f(i-1, j + 1)

            return min(up, ld, rd)
        
        ans = float('inf')
        for j in range(n):
            ans = min(ans, f(n-1, j))
        
        return ans