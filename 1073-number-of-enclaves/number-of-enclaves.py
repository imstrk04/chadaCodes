class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        # i will try to capture all the 1s from the boundary and make it 0
        # then in a double for loop i will count the number of 1s remaining

        ROWS, COLS = len(grid), len(grid[0])

        def capture(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != 1:
                return
            
            grid[r][c] = 0
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and ((r in [0, ROWS-1]) or (c in [0, COLS-1])):
                    capture(r, c)

        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    count += 1
        
        return count
