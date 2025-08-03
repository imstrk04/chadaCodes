class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        MOD = 10 ** 9 + 7

        memo = {}

        def f(i,j, s):
            if i == n - 1 and j == m - 1:
                if (grid[i][j] + s) % k == 0:
                    return 1
                else:
                    return 0
            if i >= n or j >= m:
                return 0

            if (i, j, s) in memo:
                return memo[(i, j, s)]
            
            down = f(i + 1, j, (s + grid[i][j]) % k)
    
            right = f(i, j + 1, (s + grid[i][j]) % k)
            
            memo[(i, j, s)] = (down + right) % MOD

            return memo[(i, j, s)]
        
        return f(0,0, 0)
        
        