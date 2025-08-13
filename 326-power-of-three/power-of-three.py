class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        @cache
        def f(num):
            if num == 1:
                return True
            if num <= 0 or num % 3:
                return False
            
            return f(num // 3)
        
        return f(n)