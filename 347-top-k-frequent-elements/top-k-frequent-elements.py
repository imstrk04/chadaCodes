class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        heap = [[-cnt, num] for num, cnt in hashmap.items()]
        heapq.heapify(heap)
        res = []

        for i in range(k):
            cnt, num = heapq.heappop(heap)
            res.append(num)
        
        return res