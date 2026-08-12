class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        if not to be done in O(n), sort and count
        
        for O(n):
        [s1, e1]
        [s2, e2]

        for every new x:
            it can either be s1-1, e1+1
            it can be the connecting number between s1e1 & s2e2 
                x == e1+1 == s2-1
            it can be neither -- x will have it's own seq
        '''
        if not nums:
            return 0

        num_set = set(nums)
        max_count = 0
        for cur in nums:
            if cur-1 in num_set:
                continue
            else:
                cur_count = 1
                ncur = cur
                while ncur+1 in num_set:
                    cur_count += 1
                    ncur += 1
                max_count = max(max_count, cur_count)
        return max_count