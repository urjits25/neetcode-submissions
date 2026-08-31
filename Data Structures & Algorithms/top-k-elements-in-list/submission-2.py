from heapq import heappush, heappop, heapify
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        create freq counter
        maintain min-heap of size k
        push freqs in there, pop when size > k
        return all elements in the final heap
        O(nlogn)
        '''
        cnt = Counter(nums)
        mh = []
        heapify(mh)
        
        for key, val in cnt.items():
            heappush(mh, (val, key) )
            if len(mh) > k:
                heappop(mh)
        
        res = []
        while mh:
            freq, num = heappop(mh)
            res.append(num)
        return res