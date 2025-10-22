class Solution:
    # linear graph with no cycle is bipartite
    # any graph with even cycle length is bipartite
    # any graph with odd cycle length is not bipartite
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colour = [-1] * n

        def dfs(node, c):
            colour[node] = c
            for nei in graph[node]:
                if colour[nei] == -1:
                    if not dfs(nei, 1-c):
                        return False
                elif colour[nei] == c:
                    return False
            return True
        
        for start in range(n):
            if colour[start] == -1:
                if not dfs(start, 1):
                    return False
        
        return True