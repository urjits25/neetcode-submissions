class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0, 1, 1, 2]
        if n < 4:
            return dp[ : n+1 ]
        
        cp2, ncp2 = 4, 8
        for cur in range(4, n+1):
            if cur < ncp2:
                dp.append(1 + dp[cur-cp2])
            elif cur == ncp2:
                dp.append(1)
                cp2, ncp2 = ncp2, ncp2 * 2
        return dp

