class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float("inf") for _ in range(N)]
        dp[-1] = 0
        for start in range(N - 2, -1, -1):
            if nums[start] == 0:
                continue

            for end in range(start, min(N, start + nums[start] + 1)):
                dp[start] = min(dp[start], 1 + dp[end])
            
        return dp[0]
