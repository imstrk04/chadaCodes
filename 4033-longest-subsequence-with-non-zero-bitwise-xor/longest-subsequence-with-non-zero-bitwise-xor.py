class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        numSet = list(set(nums))
        if len(numSet) == 1 and 0 in numSet:
            return 0
        for num in nums:
            res ^= num
        
        if res != 0:
            return n
        else:
            return n - 1