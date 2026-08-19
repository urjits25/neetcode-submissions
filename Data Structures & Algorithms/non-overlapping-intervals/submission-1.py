class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """ """
        intervals.sort()
        res = 0
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            si, ei = intervals[i]
            if si >= prev:
                prev = ei
            else:
                res += 1
                prev = min(ei, prev)
        return res
