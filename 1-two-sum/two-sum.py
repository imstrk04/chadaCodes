class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        index_dict = {}
        n = len(nums)
        for i in range(n):
            if (target - nums[i]) in index_dict:
                return [index_dict[target-nums[i]], i]
            index_dict[nums[i]] = i