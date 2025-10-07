import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(p):
            x, y = p

            return math.sqrt((x) ** 2 + (y) ** 2)
        
        heap = []

        for p in points:
            distance = getDistance(p)
            heapq.heappush(heap, (distance, p))
            

        res = []
        print(heap)
        for i in range(k):
            dist, point = heapq.heappop(heap)
            res.append(point)
        
        return res

        