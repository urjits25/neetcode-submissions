class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Vaccinate the cells that have `O` on the edges, dfs till no more `O`
        # Infect all others
        R, C = len(board), len(board[0])

        def vaccinate(x, y):
            if 0 <= x < R and 0 <= y < C and board[x][y] == 'O':
                board[x][y] = 'V'

                vaccinate(x+1, y)
                vaccinate(x-1, y)
                vaccinate(x, y+1)
                vaccinate(x, y-1)


        for i in range(R):
            if board[i][0] == 'O':
                vaccinate(i, 0)
            if board[i][C-1] == 'O':
                vaccinate(i, C-1)
        
        for j in range(C):
            if board[0][j] == 'O':
                vaccinate(0, j)
            if board[R-1][j] == 'O':
                vaccinate(R-1, j)
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
