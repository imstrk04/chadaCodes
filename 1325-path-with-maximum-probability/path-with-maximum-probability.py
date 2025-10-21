import collections
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            p = succProb[i]
            adj[u].append([v, p])
            adj[v].append([u,p])
        
        prob = [float('-inf')] * n
        min_heap = []
        heapq.heappush(min_heap, [-1, start_node])
        prob[start_node] = 1
        while min_heap:
            p, node = heapq.heappop(min_heap)
            p = -1 * p
            if prob[node] > p:
                continue
            
            for nei_node, oldProb in adj[node]:
                
                if (oldProb * p) > prob[nei_node]:
                    prob[nei_node] = oldProb * p
                    heapq.heappush(min_heap, [-1 * oldProb * p, nei_node])
        return prob[end_node] if prob[end_node] != float('-inf') else 0.0
        # TC: O(V+E log(V))
        # SC: O(V+E)