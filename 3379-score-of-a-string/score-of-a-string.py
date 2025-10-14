class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            ch1 = s[i]
            ch2 = s[i+1]

            v1 = ord(ch1)
            v2 = ord(ch2)

            score += abs(v1 - v2)

        return score
