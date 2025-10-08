class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        combinations = []

        def backtrack(nums, start, target):
            if target == 0:
                res.append(combinations.copy())
                return
            
            if target < 0:
                return
            
            for i in range(start, len(nums)):
                combinations.append(nums[i])
                backtrack(nums,i, target - nums[i])

                combinations.pop()
        
        backtrack(candidates, 0, target)

        return res