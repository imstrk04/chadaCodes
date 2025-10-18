class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        vis = [[0] * n for i in range(m)]
        dist = [[0] *n for i in range(m)]

        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i,j,0])
                    vis[i][j] = 1
                    
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        print(queue)
        while queue:
            i, j, step = queue.popleft()
            dist[i][j] = step
            for dr, dc in dirs:
                r, c = i + dr, j + dc
                if ((r in range(m)) and (c in range(n)) and not vis[r][c]):
                    vis[r][c] = 1
                    queue.append([r,c, step + 1])
        
        return dist