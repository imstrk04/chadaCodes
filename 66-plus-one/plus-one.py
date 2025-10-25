class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for num in digits:
            number = number * 10 + num
        
        ans = str(number + 1)
        res = []
        for num in ans:
            res.append(int(num))

        return res
