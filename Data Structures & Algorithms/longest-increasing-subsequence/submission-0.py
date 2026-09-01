class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        LIS = [1 for _ in range(N)] 

        for start in range(N-1, -1, -1):
            for end in range(start+1, N):
                if nums[start] < nums[end]:
                    LIS[start] = max(LIS[start], 1 + LIS[end] )
        return max(LIS)

