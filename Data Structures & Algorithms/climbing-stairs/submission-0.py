class Solution:
    def climbStairs(self, n: int) -> int:
        if 0 < n < 3:
            return n
        one, two = 1, 2
        for cur in range(3, n+1):
            one, two = two, one+two
        return two