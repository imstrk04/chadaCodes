class Solution:
    # linear graph with no cycle is bipartite
    # any graph with even cycle length is bipartite
    # any graph with odd cycle length is not bipartite
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colour = [-1] * n

        for start in range(n):
            if colour[start] == -1:
                queue = collections.deque([start])
                colour[start] = 0

                while queue:
                    node = queue.popleft()

                    for nei in graph[node]:
                        if colour[nei] == -1:
                            colour[nei] = 1 - colour[node]
                            queue.append(nei)
                        elif colour[nei] == colour[node]:
                            return False
            
        return True