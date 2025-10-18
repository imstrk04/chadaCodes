class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]].append(i)
            else:
                hashmap[s[i]] = [i]
        
        hashmap = dict(sorted(hashmap.items(), key = lambda x: x[1]))

        for key, val in hashmap.items():
            if len(val) == 1:
                return val[0]
        
        return -1