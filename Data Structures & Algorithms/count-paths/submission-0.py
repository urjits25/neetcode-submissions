class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        [ 
            1 1 1 1  1  1
            1 2 3 4  5  6
            1 3 6 10 15 21 
        ]
        '''
        grid = [[1 for _ in range(n) ] for _ in range(m) ]

        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
        return grid[-1][-1]
