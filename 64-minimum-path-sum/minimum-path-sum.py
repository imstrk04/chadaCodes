class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}

        def f(i, j):
            
            if i >= m or j >= n:
                return float('inf')
            
            if i == m - 1 and j == n - 1:
                memo[(i,j)] = grid[i][j]
                return grid[i][j]

            if (i, j) in memo:
                return memo[(i,j)]

            right = grid[i][j] + f(i, j + 1)
            down = grid[i][j] + f(i + 1, j)

            memo[(i,j)] = min(right, down) 
            return memo[(i,j)]
        return f(0,0)