class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        for every cell:
            if the first char matches the word's first chr:
                dfs and explore all paths

        dfs function

        if current cell matches the word[i]
            mark current as visited
            dfs at its four neighbors
        """

        m, n = len(board), len(board[0])
        def dfs(x, y, wi, visited):
            if 0 <= x < m and 0 <= y < n and \
            word[wi] == board[x][y] and \
            (x,y) not in visited:
                if wi == len(word)-1:
                    return True
                visited.add((x,y))
                down = dfs(x+1, y, wi+1, visited)
                right = dfs(x, y+1, wi+1, visited)
                left = dfs(x, y-1, wi+1, visited)
                up = dfs(x-1, y, wi+1, visited)
                visited.remove((x,y))
                return left or right or up or down
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        return False

        