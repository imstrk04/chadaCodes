class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def f(i):
            if i == 0:
                return nums[i]


            if dp[i] != -1:
                return dp[i]

            pick = nums[i] + f(i - 2) if i - 2 >= 0 else nums[i]
            notPick = f(i-1) if i - 1 >= 0 else float('-inf')

            dp[i] = max(pick, notPick)
            return dp[i]
        
        return f(n-1)