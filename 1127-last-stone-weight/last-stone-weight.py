class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        h = [-stone for stone in stones]
        heapq.heapify(h)

        while len(h) > 1:
            x = heapq.heappop(h)
            y = heapq.heappop(h)

            if x == y:
                continue
            elif x != y:
                heapq.heappush(h, -(y-x))
        
        return -1 * h[0] if h else 0