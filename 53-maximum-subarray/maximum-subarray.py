class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        max_sum = 0

        for num in nums:
            max_sum += num
            if max_sum > maxi:
                maxi = max_sum
            if max_sum < 0:
                max_sum = 0
            
        return maxi