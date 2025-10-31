class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        res = []
        for key, val in counter.items():
            if val == 2:
                res.append(key)
        return res