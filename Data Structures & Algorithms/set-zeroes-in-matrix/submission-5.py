class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        Mark first row and first col, to make all elems in that line as Zero
        if matrix[0][0] is marked zero, it can mean 0 is present in the row or col 
            - maintain another var to keep track of whether the first row (or col) contains zero
        '''
        m, n = len(matrix), len(matrix[0])
        colZero = False
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    if c > 0:
                        matrix[0][c] = 0
                    else:
                        colZero = True

        # Mark all rows as zero
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for c in range(n):
                matrix[0][c] = 0

        if colZero:
            for r in range(m):
                matrix[r][0] = 0