'''
median
    middle elem in a sorted list of odd length OR
    average of middle elems in a sorted list of even length

most efficient data structure, where adding an elem takes O(log N)
and getting the median takes O(1)

two heaps: one min heap, one max heap, of equal lengths or off by one 
min heap -- all elements more than the middle: L//2 + 1
max heap -- all elements less than the middle: L// 2
where L is the count of elements processed so far
'''

from heapq import heapify, heappush, heappop
class MedianFinder:

    def __init__(self):
        self.lh = []
        self.rh = []
        heapify(self.lh)
        heapify(self.rh)
        self.size = 0

    def addNum(self, num: int) -> None:
        # edge case: first elem in the stream
        self.size += 1

        if not self.lh and not self.rh:
            heappush(self.lh, -num)
            return 
        
        if -num >= self.lh[0]:
            heappush(self.lh, -num)
        else:
            heappush(self.rh, num)
        
        self.balHeaps()
        # print(self.lh, self.rh )

    def findMedian(self) -> float:
        if self.size % 2 == 1:
            return -self.lh[0]
        else:
            return (-self.lh[0] + self.rh[0]) / 2 
        
    def balHeaps(self):
        if 0 <= len(self.lh) - len(self.rh) <= 1:
            return 
        
        while len(self.rh) > len(self.lh):
            n = heappop(self.rh)
            heappush(self.lh, -n)

        while len(self.lh) > len(self.rh) + 1:
            n = heappop(self.lh) 
            heappush(self.rh, -n)
        