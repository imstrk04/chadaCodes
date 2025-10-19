class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adjRev = collections.defaultdict(list)
        indegrees = [0] * n

        for i in range(len(graph)):
            for nei in graph[i]:
                adjRev[nei].append(i)
                indegrees[i] += 1
        
        # now do topo sort on the reverse nodes
        queue = collections.deque()
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
        
        safeNodes = []
        while queue:
            node = queue.popleft()
            safeNodes.append(node)
            for nei in adjRev[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
    
        safeNodes.sort()

        return safeNodes