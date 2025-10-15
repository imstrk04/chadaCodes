class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        cache = {}

        def wordBreakRecur(s, pos):
            if pos == n:
                return True
            if pos in cache:
                return cache[pos]

            for i in range(pos, n):
                if s[pos: i + 1] in wordSet and wordBreakRecur(s, i + 1):
                    cache[pos] = True
                    return True
                
            cache[pos] = False
            return False
    
        return wordBreakRecur(s, 0)