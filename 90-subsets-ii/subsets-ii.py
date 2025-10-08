class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        subset = []

        def backtrack(nums, start):
            res.append(subset.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                subset.append(nums[i])
                backtrack(nums, i + 1)

                subset.pop()
            
        backtrack(nums, 0)

        return res