class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getListNotation(s):
            res = [0] * 26

            for ch in s:
                res[ord(ch) - 97] += 1
            
            return res
        
        groupedAnagrams = {}

        for word in strs:
            notation = tuple(getListNotation(word))
            if notation in groupedAnagrams:
                groupedAnagrams[notation].append(word)
            else:
                groupedAnagrams[notation] = [word]
        \
        groups = []

        for key, val in groupedAnagrams.items():
            groups.append(val)
        
        return groups