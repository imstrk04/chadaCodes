class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        seen = set(nums)

        for i in range(k, 1000, k):
            if i not in seen:
                return i

        return k