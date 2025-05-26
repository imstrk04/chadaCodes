class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target + 1)

        dp[0] = 1

        for tar in range(1, target + 1):
            for num in nums:
                if tar - num >= 0:
                    dp[tar] += dp[tar - num]
        
        return dp[target]