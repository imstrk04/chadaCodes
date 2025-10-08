class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combinations = []

        def backtrack(nums, start, target):
            if target == 0:
                res.append(combinations.copy())
                return
            
            if target < 0:
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                combinations.append(nums[i])
                backtrack(nums, i+1, target - nums[i])

                combinations.pop()
            
        
        backtrack(candidates, 0, target)
    
        return res