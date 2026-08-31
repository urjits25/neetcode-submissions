class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        
        def checkPal(l, r):
            count = 0
            while l > -1 and r < length and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        
        res = 0
        for m in range(length):
            res += checkPal(m, m)
            if m > 0:
                res += checkPal(m-1, m)
        return res