class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        cur_max = 1
        cur_res = [0,0]
        for i in range(1, len(s) ):
            # odd palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r-l+1 > cur_max:
                        cur_max = r-l+1
                        cur_res = [l, r]
                    l -= 1
                    r += 1

            # even palindromes
            l, r = i-1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r-l+1 > cur_max:
                        cur_max = r-l+1
                        cur_res = [l, r]
                    l -= 1
                    r += 1
        l, r = cur_res
        return s[l:r+1]