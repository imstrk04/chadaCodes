from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if m < n:
            return []
        
        cnt1 = Counter(p)
        cnt2 = Counter(s[:n-1]) # for now till the len(p)
        ans = []
        for i in range(n-1, m):
            cnt2[s[i]] += 1
            if cnt1 == cnt2:
                ans.append(i - n + 1)
            cnt2[s[i-n+1]] -= 1
        
        return ans