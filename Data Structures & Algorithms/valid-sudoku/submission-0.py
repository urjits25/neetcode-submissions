class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R, C = 9, 9
        # check each row
        for r in range(R):
            cur = set()
            for c in range(C):
                x = board[r][c]
                if x in cur and x != '.':
                    return False
                cur.add(x)
        print("Rows good")

        # check each col
        for c in range(C):
            cur = set()
            for r in range(R):
                x = board[r][c]
                if x in cur and x != '.':
                    return False
                cur.add(x)
        print("Cols good")

        # check each 3x3 grid
        for r in range(0, R, 3):
            for c in range(0, C, 3):
                print(r, c)
                cur = set()
                for x in range(r, r+3):
                    for y in range(c, c+3):
                        if board[x][y] in cur and board[x][y] != '.':
                            return False
                        cur.add(board[x][y] )
        return True