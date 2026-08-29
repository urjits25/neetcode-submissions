class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        mark cells that can go to pacific and atlantic already
        iterate through the island: at each cell check if they can reach P or A, mark it as such
        
        how to check?
        pacific : up or left - won't work because there could be a crater or bend 
        atlantic: down or right
        
        - dfs bc we want the shortest path to meet ocean
            - keep track of path, if meets to the ocean
            - mark all elems in the path as ocean meetable
        - at every cell, check if its neighbor is reachable and which oceans they're flowing into
        '''

        R, C = len(heights), len(heights[0])
        atlantic = set()
        pacific = set()

        for i in range(R):
            pacific.add((i, 0) )
            atlantic.add((i, C-1) )
        
        for j in range(C):
            pacific.add((0, j) )
            atlantic.add((R-1, j) )

        # dfs from each ends to mark all the cells that can flow into that end
        def dfs(x, y, ocean):
            # check all four directions
            dirn = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            
            for dx, dy in dirn:
                if (x+dx, y+dy) in ocean or not (0 <= x+dx < R and 0 <= y+dy < C):
                    continue
                if heights[x+dx][y+dy] >= heights[x][y]:
                    ocean.add((x+dx, y+dy) )
                    dfs(x+dx, y+dy, ocean)
        
        for (x, y) in list(pacific):
            dfs(x, y, pacific)
        
        for (x, y) in list(atlantic):
            dfs(x, y, atlantic)

        return list([x, y] for x, y in (pacific & atlantic) )