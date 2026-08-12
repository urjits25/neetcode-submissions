class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        [2, 5, 6, 9]
        target = 9

        at every num, we have three options:
        1) select and keep -> [2,5,6,9] t = 7
        2) select and drop -> [5,6,9]   t = 7
        3) drop             -> [5,6,9]  t = 9
        imp to check if nums are all positive

        exit condition 
        1) t < 0
        2) t = 0, add it to the candidate solutions
        
        how to return unique combinations?
        sort combination, tuple it, put it in a set
        '''
        nums.sort()
        res = set()
        def helper(start, cur_cmb, cur_target):
            if cur_target < 0:
                return
        
            if cur_target == 0:
                res.add(tuple(sorted(cur_cmb)) )
                return
            
            if start == len(nums):
                return

            # select & keep
            helper(start, cur_cmb + [nums[start]], cur_target-nums[start] )
            
            # drop
            helper(start+1, cur_cmb, cur_target)
        helper(0, [], target)
        return list(list(x) for x in res)