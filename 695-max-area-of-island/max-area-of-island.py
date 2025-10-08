class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        self.max_area = 0

        def bfs(r, c):
            count = 1
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))
            dirs = [[1,0], [-1, 0],[0,1],[0,-1]]
            while queue:
                row, col = queue.popleft()
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == 1 and (r, c) not in visited):
                        count += 1
                        queue.append((r, c))
                        visited.add((r, c))
            return count
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r, c)
                    self.max_area = max(self.max_area, area)   
                    visited.add((r,c))
        
        return self.max_area