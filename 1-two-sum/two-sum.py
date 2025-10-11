class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # number -> index

        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                return [hashmap[target - nums[i]], i]
            else:
                hashmap[nums[i]] = i
                