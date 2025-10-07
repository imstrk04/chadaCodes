class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(map(int, str(n)))
        l = len(digits)

        i = l - 2
        while i >= 0 and digits[i] >= digits[i+1]:
            i -= 1
        
        if i < 0:
            return -1
        
        j = l - 1
        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]

        digits[i + 1: ] = reversed(digits[i+1: ])

        next_n = int(''.join(map(str, digits)))

        return next_n if next_n < 2 ** 31 else -1 