class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        curMax = maximum product ending at the current index
        curMin = minimum product ending at the current index

        compare against, curMin, curMax, cur
        '''

        res, cur_min, cur_max = nums[0], 1, 1
        
        for x in nums:
            tmp = cur_min
            cur_min = min([cur_min * x, cur_max * x, x])
            cur_max = max([tmp * x, cur_max * x, x])
            res = max(res, cur_max)
            if x == 0:
                cur_min = cur_max = 1
        return res