class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()

        def dfs(i):
            if i == destination:
                return True
            
            for nei in graph[i]:
                if nei not in seen:
                    seen.add(nei)
                    if dfs(nei):
                        return True
            
            return False
        
        return dfs(source)