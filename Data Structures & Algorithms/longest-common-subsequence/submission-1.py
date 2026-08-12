class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        brute-force:
            crabt cat
        if cur char matches, move both ptrs ahead

            rabt  at
        if first chars don't match, two options
            abt at          rabt t
             bt t     |  abt t          |    rabt _
         b t    t  t  | bt t    abt _   |

        Top-Down Dynamic Programming
        DFS down the two strings
        at each match, incr both indexes
        at no-match, split the tree into removing from t1 and t2
            base condition: t1 or t2 is ""
            c r a b t
        c   3 2 2 1 1
        a   2 2 2 1 1
        t   1 1 1 1 1
        """

        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
