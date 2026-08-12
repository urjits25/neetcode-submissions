class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        brute-force: 
            crabt cat 
        if cur char matches, move both ptrs ahead
        
            rabt  at
        if first chars don't match, two options 
            abt at          rabt t
             bt t     |  abt t          |    rabt _
         b t    t  t  | bt t    abt _   | 
        
        Top-Down Dynamic Programming
        DFS down the two strings 
        at each match, incr both indexes
        at no-match, split the tree into removing from t1 and t2
            base condition: t1 or t2 is ""
            c r a b t 
        c   3 2 2 1 1
        a   2 2 2 1 1    
        t   1 1 1 1 1
        '''
        
        mem_array = [[None for _ in range(len(text2))] for _ in range(len(text1))]
        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if mem_array[i][j] is not None:
                return mem_array[i][j]

            if text1[i] == text2[j]:
                mem_array[i][j] = 1 + helper(i+1, j+1)
                return mem_array[i][j]
            
            left_max = helper(i+1, j)
            right_max = helper(i, j+1)
            mem_array[i][j] = max(left_max, right_max)
            return mem_array[i][j]

        return helper(0, 0)

            
