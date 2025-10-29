class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        vis = set()

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or grid2[r][c] == 0 or (r, c) in vis:
                return True  
            
            vis.add((r, c))
            is_sub = True
            
        
            if grid1[r][c] == 0:
                is_sub = False
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                if not dfs(r+dr, c+dc):
                    is_sub = False
            
            return is_sub

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in vis:
                    if dfs(i, j):
                        count += 1

        return count
