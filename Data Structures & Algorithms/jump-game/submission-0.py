class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        at any point, need to keep track of the first index 
            that can reach any other index that reaches the end
        
        if `i` has a jump potential to end
            - for any j < i, if we land anywhere between i and end from j ... 
            we can reach the end from j 
        
        to already know if jumps are reaching end, we'll start from the end
        '''
        N = len(nums)
        if N < 2:
            return True

        ce = N-1
        for cs in range(N-2, -1, -1):
            if nums[cs] + cs >= ce:
                ce = cs
        return ce == 0

