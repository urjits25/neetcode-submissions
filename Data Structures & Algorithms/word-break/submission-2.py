class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        at every slice, check if it can be matched with word in word dict
        if it can:
            recurse from the next index to the end
            store the result at the current index
        continue the current level too
        '''

        dp = [False for _ in range(len(s)+1) ]
        dp[-1] = True
        wordDict = set(wordDict)

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w) ] == w:
                    dp[i] = dp[i + len(w)]
                    if dp[i]:
                        break
        return dp[0]