class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """ """
        intervals.sort()
        res = 0

        # print(intervals)
        # [[-73, -26], [-65, -11], [-63, 2], [-62, -49], [-52, 31], [-40, -26], [-31, 49], [30, 47], [58, 95], [66, 98], [82, 97], [95, 99]]

        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            pei = prev
            si, ei = intervals[i]
            
            if si < pei:
                # overlapping, keep the interval that ends sooner
                res += 1
                if ei < pei:
                    prev = ei
            else:
                prev = ei
        return res
