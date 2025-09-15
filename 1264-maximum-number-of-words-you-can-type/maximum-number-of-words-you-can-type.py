class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = text.split(" ")
        broken = set(brokenLetters)
        count = 0
        for word in arr:
            for ch in word:
                if ch in broken:
                    count += 1
                    break
                 
        return len(arr) - count