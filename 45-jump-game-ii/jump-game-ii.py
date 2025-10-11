class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)

        maxJump = float('inf')
        memo = {}
        def jumpRecur(i):
            nonlocal maxJump
            if i >= n:
                return 0
            if i == n -1:
                return 0

            if i in memo:
                return memo[i]
            j = nums[i]
            minJump = float('inf')

            for jump in range(i+1,i+j+1):
                minJump = min(minJump, 1 + jumpRecur(jump))
            
            memo[i] = minJump
            return minJump

        return jumpRecur(0)