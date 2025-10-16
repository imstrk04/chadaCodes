class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []

        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(i):
            state = states[i]

            if state == VISITING:
                return False
            elif state == VISITED:
                return True
            
            states[i] = VISITING

            for nei in graph[i]:
                if not dfs(nei):
                    return False
            
            states[i] = VISITED
            order.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return order
