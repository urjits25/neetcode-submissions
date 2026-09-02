class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        minute = 0
        bfs = []
        R, C = len(grid), len(grid[0]) 
        fresh = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    bfs.append((i, j) )
                elif grid[i][j] == 1:
                    fresh += 1
        
        dirn = [(0,1), (1,0), (0, -1), (-1, 0) ]

        while fresh > 0 and bfs:
            minute += 1
            nbfs = []
            for (i, j) in bfs:

                for dx, dy in dirn:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                        nbfs.append((nx, ny) )
                        grid[nx][ny] = 2
                        fresh -= 1
            bfs = nbfs
        
        return minute if fresh == 0 else -1 
