class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        at every house, maintain the max money that can be gained:
            by robbing the current or 
            skipping the current
        
        for the next house:
            we maintain (max_money with house, max_money w/o house)
            max_money with house = (cur + prev_without)
            max_money w/o house = max(prev_with, prev_without)
        '''

        dp = [[0,0] for _ in range(len(nums)+1)]
        for i, n in enumerate(nums):
            # with current house
            dp[i+1][0] = n + dp[i][1]

            # without current house
            dp[i+1][1] = max(dp[i])

            
        return max(dp[-1])