class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Two pointer approach
        '''
        l, r = 0, len(heights)-1
        cur_max = 0
        while l < r:
            h = min(heights[l], heights[r])
            cur_area = h * (r-l) 
            cur_max = max(cur_max, cur_area)

            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return cur_max