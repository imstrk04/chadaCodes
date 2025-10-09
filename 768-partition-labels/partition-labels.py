class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastPos = {}
        
        for i in range(len(s)-1, -1, -1):
            ch = s[i]        
            if ch not in lastPos:
                lastPos[ch] = i
        
        start = 0
        end = 0
        print(lastPos)
        for i in range(len(s)):
            ch = s[i] # a
            getIndex = lastPos[ch] # 8
            end = max(end, getIndex)
            if end == i:
                res.append(end - start + 1)
                start = i + 1
            lastPos[ch] = end
            
        return res