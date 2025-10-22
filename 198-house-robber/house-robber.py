class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # space optimised approach
        prev, prev2 = nums[0], 0

        for i in range(1, n):
            pick = nums[i] 
            if i > 1:
                pick += prev2
            notPick = prev

            cur_i = max(pick, notPick)
            prev2 = prev
            prev = cur_i
        
        return prev