class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(nums, start):
            res.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(nums, i+1)
                subset.pop()

        backtrack(nums, 0)

        return res