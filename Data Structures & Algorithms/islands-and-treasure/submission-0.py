from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        inf = pow(2, 31) - 1
        """
        - traverse from the treasure chests to the neighbors 
            - BFS for shortest path
            - in all four directions
        - breaking conditions:
            - if cell is water
            - if previous cell val is less than the current-computed one
            - out of bounds
        """

        treasure = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    treasure.append((i, j))

        
        dirn = [(-1, 0), (0, 1), (0, -1), (1, 0)]

        for tx, ty in treasure:
            bfs = deque([(tx, ty)])
            cur_val = 1
            
            while bfs:
                for _ in range(len(bfs) ):
                    x, y = bfs.popleft()
                    for dx, dy in dirn:
                        if 0 <= x+dx < m and 0 <= y+dy < n and \
                         grid[x+dx][y+dy] > cur_val:
                            grid[x+dx][y+dy] = cur_val
                            bfs.append((x+dx, y+dy) )
                cur_val += 1