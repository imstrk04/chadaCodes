class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        n = len(rooms)
        vis = [0] * n
        vis[0] = 1
        def dfs(chamber):
            nonlocal vis
            for nei in rooms[chamber]:
                if not vis[nei]:
                    vis[nei] = 1
                    dfs(nei)
        
        dfs(0)

        for visited in vis:
            if not visited:
                return False
            
        return True