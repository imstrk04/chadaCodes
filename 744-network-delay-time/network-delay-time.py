class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        min_heap = []
        for time in times:
            u = time[0]
            v = time[1]
            wt = time[2]
            edges[u].append([v, wt])
        
        minHeap = [(0, k)] # (path_len, node)
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [w2 + w1, n2])
        
        return t if len(visit) == n else -1
