class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # BS on answers
        low = 1
        high = max(piles)

        def k_works(k):
            hours = 0
            for p in piles:
                hours += ceil(p / k)
            return hours <= h

        while low < high:
            k = (low + high) // 2
            if k_works(k):
                high = k
            else:
                low = k + 1

        return low 