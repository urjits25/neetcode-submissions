class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        sort candidates
        all positive numbers, so sum will only increase
        - for i in range(len(candidates) )
            if cur_sum = target:
                add to the result
                break 
            if cur_sum > target:
                break
            
            if cur_sum < target:
                for j in range(i+1, len(candidates) )
                    recurse
                    ...

        '''
        candidates.sort()
        res = []
        def dfs(start, cur_sum, cur_comb):
            if cur_sum == target:
                res.append(cur_comb.copy() )
                return 

            for i in range(start, len(candidates) ):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if cur_sum + candidates[i] > target:
                    break 

                cur_comb.append(candidates[i] )
                dfs(i+1, cur_sum + candidates[i], cur_comb)
                cur_comb.pop()
        
        dfs(0, 0, [] )
        return res