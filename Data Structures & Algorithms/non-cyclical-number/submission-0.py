class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumDigSquared(x):
            sum_sqr = 0
            while x:
                d = x % 10
                x = x // 10
                sum_sqr += d * d
            return sum_sqr
        if n == 1:
            return True
        slow = n 
        fast = sumDigSquared(sumDigSquared(n) )
        while fast != 1:
            if slow == fast:
                return False
            slow = sumDigSquared(slow)
            fast = sumDigSquared(sumDigSquared(fast) )
        return True