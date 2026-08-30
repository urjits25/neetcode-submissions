class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [1 for _ in range(len(s)+1 ) ]
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                memo[i] = 0
                continue
            
            memo[i] = memo[i+1]
            if i+1 < len(s) and "10" <= s[i:i+2] < "27":
                memo[i] += memo[i+2]
        return memo[0]