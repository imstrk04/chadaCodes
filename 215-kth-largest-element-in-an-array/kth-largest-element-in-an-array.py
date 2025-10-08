class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        arr = [-num for num in nums]
        heapq.heapify(arr)
        
        for i in range(k):
            ans = heapq.heappop(arr)
        
        return -ans