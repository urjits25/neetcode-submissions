class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        right -> down -> left -> up -> ri...
        maintain top, right, bottom, left bounds
        maintain directions for horizontal & vertical traversals
        stopping condition: 
        - till we have m*n elements OR
        - bounds are same or crossed
        '''
        m, n = len(matrix), len(matrix[0])
        t, r, b, l = 0, n-1, m-1, 0
        res = []

        i, j = 0, 0
        while l <= i <= r and t <= j <= b:
            
            # right
            while l <= j <= r and len(res) < m*n:
                res.append(matrix[i][j])
                j += 1
            t += 1
            i += 1
            j -= 1

            # down
            while t <= i <= b and len(res) < m*n:
                res.append(matrix[i][j])
                i += 1
            r -= 1
            j -= 1
            i -= 1

            # left
            while l <= j <= r and len(res) < m*n:
                res.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            b -= 1

            # up
            while t <= i <= b and len(res) < m*n:
                res.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1
            l += 1

            '''
            [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]]
            '''

        return res