class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row = [ False for _ in range(m) ]
        col = [ False for _ in range(n) ]

        # Mark rows and cols to be marked zero as True
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row[r] = col[c] = True
        
        for r in range(m):
            if row[r]:
                for c in range(n):
                    matrix[r][c] = 0
        
        for c in range(n):
            if col[c]:
                for r in range(m):
                    matrix[r][c] = 0
