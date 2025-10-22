class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def f(i1, i2): 
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            
            if text1[i1] == text2[i2]:
                return 1 + f(i1 + 1, i2 + 1)
            else:
                return max(f(i1 + 1, i2), f(i1, i2 + 1))

            
        return f(0,0)