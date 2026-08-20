class Trie:
    def __init__(self):
        self.is_end = False
        self.next_char = [None for _ in range(26)]
        self.word_so_far = ""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        - traverse the board in dfs
            - build the candidate strings
            - check if they match with the give `words`
                - can be put in a hashmap for instant retrieval
                    key: starting letter?
            - what if board contains [a a a a] * n times, and `words` contain "aa", "aaa"
        - optimized way to stop dfs early?
            - save words in a trie
            - if there are no words being built with the starting char or current list of chars, we stop early and move to the next dfs

        - how to diff between?
            - chr not in word --> assign False
            - last chr of word -> is_end flag is True
        """

        trie_of_words = Trie()
        for word in words:
            node = trie_of_words
            wsf = ""
            for ci in word:
                idx = ord(ci) - ord('a')
                if not node.next_char[idx]:
                    node.next_char[idx] = Trie()

                node = node.next_char[idx]
                wsf += ci
                node.word_so_far = wsf
            node.is_end = True

        ROWS, COLS = len(board), len(board[0])

        def dfs(x, y, cur):
            
            if x < 0 or x == ROWS or y < 0 or y == COLS or board[x][y] == "#" :
                return

            idx = ord(board[x][y]) - ord('a')
            if not cur.next_char[idx]:
                return 

            # if end of word
            if cur.next_char[idx].is_end:
                self.res.add(cur.next_char[idx].word_so_far)

            cur = cur.next_char[idx]
            tmp = board[x][y]
            board[x][y] = "#"
            dfs(x+1, y, cur)
            dfs(x-1, y, cur)
            dfs(x, y+1, cur)
            dfs(x, y-1, cur)
            board[x][y] = tmp

        self.res = set()
        for r in range(ROWS):
            for c in range(COLS):
                idx = ord(board[r][c]) - ord("a")
                if trie_of_words.next_char[idx]:
                    dfs(r, c, trie_of_words)

        return list(self.res)
