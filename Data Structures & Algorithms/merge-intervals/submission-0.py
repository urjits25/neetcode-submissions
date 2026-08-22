class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        [1,1],[4,5],[5,5], [5,6]]
        res = [[1,1], [4,6] ]
        '''
        
        intervals.sort()
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            si, ei = intervals[i]
            lsi, lei = res[-1]
            if si <= lei:
                res[-1][1] = max(ei, lei)
            else: 
                res.append([si, ei])
        return res
