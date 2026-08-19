class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        [ 
            1 1 1 1  1  1
            1 2 3 4  5  6
            1 3 6 10 15 21 
        ]
        '''
        grid = [1 for _ in range(n) ] 
        for r in range(1, m):
            for c in range(1, n):
                grid[c] = grid[c-1] + grid[c]
        return grid[-1]
