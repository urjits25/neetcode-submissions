"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heapify, heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        (0,8), (8,10) is not considered a conflict
        
        intrvs = [(0,40),(5,10),(15,20)]
        adjacent intrv : overlapping, inclusive, disjoint

        (0,40) -- (35,50), (1,5), (40,45)
        room 1     room 2   room 2  room 1


        - heap of interval end-times
        - for every interval:
            - if heaptop <= cur_int_start, pop it
            - push cur_int_end to heap
        '''
        eth = []
        heapify(eth)
        intervals.sort(key= lambda x: x.start)

        for intrvl in intervals: 
            st, et = intrvl.start, intrvl.end
            if not eth:
                heappush(eth, et)
                continue

            if eth[0] <= st:
                heappop(eth)
            heappush(eth, et)
        
        return len(eth)