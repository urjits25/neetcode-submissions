class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        dp = nums[:] 
        for i in range(1, len(dp) ):
            dp[i] = max(dp[i], dp[i-1] + dp[i] )
        return max(dp)
