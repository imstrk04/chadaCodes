class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= res[-1][1]:
                oldStart, oldEnd = res.pop()
                res.append([oldStart, max(end, oldEnd)])
            else:
                res.append([start, end])
        
        return res